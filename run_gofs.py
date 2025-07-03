import os 
import fnmatch
import hashlib
import subprocess

from rich_argparse_plus import RichHelpFormatterPlus
RichHelpFormatterPlus.styles["argparse.syntax"] = "#88C0D0"

import logging
import click
from rich.logging import RichHandler
from rich.progress import (
    Progress,
    TextColumn,
    BarColumn,
    MofNCompleteColumn,
    TimeRemainingColumn,
    TimeElapsedColumn,
    SpinnerColumn,
)
from rich.prompt import Confirm
from rich.traceback import install
install(show_locals=False)

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected.")

def find_directories_with_file(root_dir, target_file):
    directories = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in fnmatch.filter(filenames, target_file):
            directories.append(os.path.join(dirpath, filename))
    return directories

if __name__ == "__main__":
    import os
    import argparse
    parser = argparse.ArgumentParser(formatter_class=RichHelpFormatterPlus, description="Run Goodness of Fit tests on matching combin workspaces/models in all subdirectories.")
    parser.add_argument("--ws", type=str, default="model_combined.root", help="t2w.py output name(s), ie. `model_combined.root`, also accepts a list of patterns like `'model*.root,custom_name.root'`")
    parser.add_argument(
        "--run",
        dest="run",
        type=str2bool,
        nargs="?",
        const=True,
        default=False,
        choices=[True, False],
        help="Batch run GoFs.",
    )
    parser.add_argument(
        "--merge",
        dest="merge",
        type=str2bool,
        nargs="?",
        const=True,
        default=False,
        choices=[True, False],
        help="Merge GoF outputs.",
    )
    parser.add_argument(
        "--plot",
        dest="plot",
        type=str2bool,
        nargs="?",
        const=True,
        default=False,
        choices=[True, False],
        help="Make plots (calculate gofs).",
    )
    parser.add_argument(
        "--dry",
        "--dryrun",
        dest="dryrun",
        type=str2bool,
        nargs="?",
        const=True,
        default=False,
        choices=[True, False],
        help="Make plots (calculate gofs).",
    )
    parser.add_argument("-p", '--parallel', type=int, default=10, help="Number of workers")
    parser_combine = parser.add_argument_group("COMBINE Options")
    parser_combine.add_argument("-t", type=int, default=2, help="Number of toys")
    parser_combine.add_argument("-s", "--seed", type=str, default='1:2:1', help="Random seed")
    parser_combine.add_argument("--toysFrequentist", action="store_true", help="Use toysFrequentist")

    parser_debug = parser.add_argument_group("DEBUG Options")
    parser_debug.add_argument(
        "--verbose", "-v", "-_v", action="store_true", help="Verbose logging"
    )
    parser_debug.add_argument(
        "--debug", "-vv", "--vv", action="store_true", help="Debug logging"
    )
    
    full_args = parser.parse_known_args()
    args = full_args[0]

    os.environ['CMSSW_BASE'] = ""  #ugh
    os.environ['SCRAM_ARCH'] = ""  #ugh

    basedir = os.getcwd()
    if "," in args.ws:
        args.ws = args.ws.split(",")
    else:
        args.ws = [args.ws]

    # Logging
    from functools import partial, partialmethod
    logging.DRY = 15  # betweeen INFO (20) and DEBUG (10)
    logging.addLevelName(logging.DRY, 'DRY-RUN')
    logging.Logger.dry = partialmethod(logging.Logger.log, logging.DRY)
    logging.dry = partial(logging.log, logging.DRY)
    log_level = logging.WARNING

    if args.verbose:
        log_level = logging.INFO
    if args.debug:
        log_level = logging.DEBUG
    if args.dryrun:
        log_level = logging.DRY
    logging.getLogger("matplotlib").setLevel(logging.WARNING)
    logging.getLogger("fsspec").setLevel(logging.WARNING)
    logging.getLogger("ROOT").setLevel(logging.WARNING)
    class CustomRichHandler(RichHandler):
        def get_level_text(self, record):
            level_name = record.levelname
            if level_name == "DRY-RUN":
                return f"[plum4]{level_name}[/plum4]"
            elif level_name == "DEBUG":
                return f"[dim blue]{level_name}[/dim blue]"
            elif level_name == "INFO":
                return f"[green]{level_name}[/green]"
            elif level_name == "WARNING":
                return f"[yellow]{level_name}[/yellow]"
            elif level_name == "ERROR":
                return f"[red]{level_name}[/red]"
            elif level_name == "CRITICAL":
                return f"[bold red]{level_name}[/bold red]"
            return level_name
    logging.basicConfig(
        level=log_level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[CustomRichHandler(rich_tracebacks=True, tracebacks_suppress=[click])],
    )

    passthrough_args = full_args[1]
    passthrough_args = [f"'{arg}'" if not arg.startswith('-') else arg for arg in passthrough_args]
    logging.debug(f'Passthrough args: {r" ".join(passthrough_args)}')

    parallel = 6

    model_paths = sorted(list(set(sum([find_directories_with_file(basedir, args.ws[i]) for i in range(len(args.ws))], []))))
    # Soft model_paths, by nesting - shorter paths first, subdirectoriestogether
    model_paths = sorted(model_paths, key=lambda x: (len(x), x))
    model_paths = sorted(model_paths, key=lambda x: (x.count("/"), x))
    bag_toys = {}
    bag_data = {}
    hash_map = {}
    logging.info(f"Finding workspaces in {basedir}")
    for i in range(len(model_paths)):
        logging.info(f"  Found {model_paths[i]}")
        model_path, model_dir = model_paths[i], os.path.split(model_paths[i])[0]
        hash_string = hashlib.md5(model_path.encode()).hexdigest()[:8]
        hash_map[hash_string] = model_path

        sstart, sstop, sstep = args.seed.split(":")
        for s in range(int(sstart), int(sstop)+1, int(sstep)):
            seed = str(s)
            base_cmd = f"combineTool.py  -M GoodnessOfFit --algo saturated " \
                f"-d {model_path} -n {hash_string} " 
            base_cmd += f'{r" ".join(passthrough_args)}'
            cmd = base_cmd + f"-t {args.t} -s {seed} --toysFrequentist  "
            bag_toys[f"{hash_string}_{seed}"] = {
                'cmd': cmd,
                'model_dir': model_dir,
            }
        bag_data[f"{hash_string}"] = {
            'cmd': base_cmd,
            'model_dir': model_dir,
        }

    def run_command(cmd, model_dir):
        try:
            os.chdir(model_dir)
            if args.dryrun:
                logging.dry(f"{cmd}")
                return {}
            else:
                import subprocess
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True) 
                os.chdir(basedir)
                return {
                    "model_path": model_path,
                    "success": result.returncode == 0,
                    "stdout": result.stdout,
                    "stderr": result.stderr
                }
        except Exception as e:
            os.chdir(basedir)
            return {
                "model_path": model_path,
                "success": False,
                "stdout": "",
                "stderr": str(e)
            }
    
    import concurrent.futures
    max_workers = args.parallel
    
    def run_bag(bag, data=False, executor=None):
        results = []
            # Submit all jobs
        if args.dryrun:
            _ = [run_command(run['cmd'], run['model_dir']) for key, run in bag.items()]
            return
        futures = {executor.submit(run_command, run['cmd'], run['model_dir']): key for key, run in bag.items()}
        
        # Set up Rich progress display
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]{task.description}"),
            BarColumn(bar_width=50),
            MofNCompleteColumn(),
            TimeElapsedColumn(),
            TimeRemainingColumn(),
        ) as progress:
            # Create a task for overall progress
            task = progress.add_task("[cyan]Waiting on jobs", total=len(futures))
            
            # Track running futures
            running = set(futures.keys())
            success_count = 0
            fail_count = 0
            
            # Loop until all futures are done
            while running:
                # Check for futures that are complete (use a small timeout)
                done, running = concurrent.futures.wait(
                    running, timeout=0.5, 
                    return_when=concurrent.futures.FIRST_COMPLETED
                )
                
                # Process completed futures
                for future in done:
                    key = futures[future]
                    try:
                        result = future.result()
                        results.append(result)
                        
                        # Update progress description based on success/failure
                        if result["success"]:
                            success_count += 1
                            # progress.console.print(f"[green]✓[/green] {key}: Completed successfully")
                            _s = key.split("_")[-1]
                            if data:
                                pass
                                # progress.console.print(f"[green]✓[/green] Data Fit {bag[key]['model_dir']}/model_combined.root: Completed successfully")
                            else:
                                progress.console.print(f"[green]✓[/green] Toy Fit (-t {args.t} -s {_s}) {bag[key]['model_dir']}/model_combined.root: Completed successfully")
                        else:
                            fail_count += 1
                            error_msg = result.get('stderr', 'Unknown error').split('\n')[0]
                            progress.console.print(f"[red]✗[/red] {key}: Failed - {error_msg}")
                            
                    except Exception as exc:
                        fail_count += 1
                        progress.console.print(f"[red]✗[/red] {key}: Exception - {exc}")
                    
                    # Update the progress bar
                    if data:
                        progress.update(task, advance=1, description=f"[cyan]Running GoF data... ([green]{success_count}[/green]/[red]{fail_count}[/red])")
                    else:
                        progress.update(task, advance=1, description=f"[cyan]Running GoF toys... ([green]{success_count}[/green]/[red]{fail_count}[/red])")
        
        # Summarize results
        successful = sum(1 for r in results if r["success"])
        print(f"\nCompleted {successful} of {len(bag)} models successfully")

    if args.run:
        with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
            run_bag(bag_data, data=True, executor=executor)
            run_bag(bag_toys, executor=executor)

    # Collate 
    if args.merge:
        for hash, path in hash_map.items():
            model_dir = os.path.split(path)[0]
            logging.info(f"Collating {model_dir}")
            os.chdir(model_dir)
            cmd = f"hadd -f gof_toys.root higgsCombine{hash}.GoodnessOfFit.mH120.*.root " 
            if args.dryrun:
                logging.dry(f"{cmd}")
            else:
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True) 
            cmd = f"mv higgsCombine{hash}.GoodnessOfFit.mH120.root gof_data.root  " 
            if args.dryrun:
                logging.dry(f"{cmd}")
            else:
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True) 
            os.chdir(basedir)


    if args.plot:
        from utils_single_gof import gofplot
        plot_dir = os.path.join(basedir, "gof_plots")
        pvals = {}
        for hash, path in hash_map.items():
            model_dir = os.path.split(path)[0]
            logging.info(f"Plotting {model_dir}")
            if args.dryrun:
                continue
            dfile = os.path.join(model_dir, "gof_data.root")
            tfile = os.path.join(model_dir, "gof_toys.root")
            rel_path = os.path.relpath(model_dir, basedir)
            savename = os.path.join(plot_dir, f'gof{hash}_{rel_path.replace("/", "_")}.pdf')
            pval = gofplot(dfile, tfile, 
                           savename=savename, 
                           algo='saturated', 
                        #    year=args.year, 
                           title=rel_path)
            pvals[path] = pval
        

        def display_gof_pvalues(pvalue_dict):
            """
            Pretty print p-values from GoF tests with color coding:
            - Red for p < 0.05 (potentially significant)
            - Green for p ≥ 0.05 (consistent with null hypothesis)
            """
            from rich.console import Console
            from rich.table import Table
            
            console = Console()
            
            # Create a table with appropriate columns
            table = Table(title="Goodness of Fit p-values", show_header=True, header_style="bold")
            table.add_column("Model Path", style="dim")
            table.add_column("p-value", justify="right")
            
            # Add rows with color coding based on p-value
            for model_path, pvalue in sorted(pvalue_dict.items()):
                style = "red" if pvalue < 0.05 else "green"
                table.add_row(
                    model_path, 
                    f"[{style}]{pvalue:.3f}[/{style}]"
                )
            
            # Print the table
            console.print(table)

        # Example usage with your dictionary
        display_gof_pvalues(pvals)
        from rich.pretty import pprint
        pprint(pvals)
