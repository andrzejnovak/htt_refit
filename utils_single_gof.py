

import ROOT as r
import rhalphalib as rl
import hist
import mplhep as hep
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import logging
from rich.logging import RichHandler
from scipy.stats import chi2
import click
import os

from rich_argparse_plus import RichHelpFormatterPlus
RichHelpFormatterPlus.styles["argparse.syntax"] = "#88C0D0"

# FORMAT = "%(message)s"
# logging.basicConfig(
#     level=logging.WARNING, format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
# )

# log = logging.getLogger("rich")

hep.style.use("CMS")

def get_vals(fname):
    rfile = r.TFile.Open(fname)
    rtree = rfile.Get("limit")
    vals = []
    for i in range(rtree.GetEntries()):
        rtree.GetEntry(i)
        mu = rtree.limit
        vals.append(mu)
    return vals

def gofplot(datafile, mcfile, savename='fplotX',  algo='saturated', title=None, year=""):
    gofs = np.array(get_vals(mcfile))
    gof_data = get_vals(datafile)[0]

    logging.debug(f"GoF plot: {datafile}")
    logging.debug(f"  Gof data: {gof_data}")
    logging.debug(f"  Gaussian thresholds {np.array([np.around(np.mean(gofs) + x * np.std(gofs), 3) for x in [-3,-2,-1,0,1,2,3]])}")

    x_lim = np.max(gofs) * 1.2
    x_low = np.min(gofs) * 0.9
    x = np.linspace(x_low, x_lim, 200)
    bins = np.linspace(0, x_lim, 50)
    width = bins[1] - bins[0]

    pval = round(float(len(gofs[gofs > gof_data]))/len(gofs), 3)

    fig, ax = plt.subplots()
    if algo == 'saturated':
        ax.plot(x, len(gofs) * width * chi2.pdf(x, np.mean(gofs)), color='red', label='$\chi^2 fit$, ndf = {:.2f}'.format(np.mean(gofs)))
    h, _, _ = ax.hist(gofs, bins, facecolor='none', edgecolor='black', histtype='stepfilled', lw=2,
            label="Toys, N = {}".format(len(gofs)))
    ax.hist(gofs[gofs > gof_data], bins, facecolor='steelblue', edgecolor='gray', histtype='stepfilled', alpha=0.3,
            label='p-value = {}'.format(pval));
    
    logging.debug(f"P-value = {pval}")
    ax.annotate("", xy=(gof_data, 0),
                xytext=(gof_data, 0.4*max(h)),
                # arrowprops=dict(lw='4', color='b', arrowstyle="->,head_length=1.5,head_width=0.5"),
                arrowprops=dict(color='blue', lw=4, arrowstyle="->,head_length=0.5,head_width=0.2"),
                )
    ax.plot([], [], color='blue', lw=2, label="Observed = {:.2f}".format(gof_data))

    ax.legend(title=title)
    hep.cms.label(llabel='Private Work', data=True, year=year, ax=ax)
    xwidthlo, xwidthhi = np.mean(gofs)-np.std(gofs)*3, np.mean(gofs)+np.std(gofs)*3
    ax.set_xlim(min(xwidthlo, gof_data*1.2), max(xwidthhi, gof_data*1.2))
    ax.set_ylim(0, max(h) * 1.4)
    if algo == 'saturated':
        xlab = r"$-2log(\lambda)$"
    else:
        xlab = "KS"
    ax.set_xlabel(xlab , x=1, ha='right')
    ax.set_ylabel("Pseudoexperiments", y=1, ha='right')

    savedir = os.path.dirname(savename)
    if len(savedir) > 0:
        os.makedirs(savedir, exist_ok=True)
    if not savename.endswith(".pdf") or not savename.endswith(".png"):
        savename += ".png"
    fig.savefig(f"{savename}", dpi=300, transparent=False, bbox_inches='tight')
    return pval


if __name__ == "__main__":
    import argparse
    import os
    parser = argparse.ArgumentParser(formatter_class=RichHelpFormatterPlus, 
                description="Run a Goodness-of-Fit plot.")
# With these lines
    parser.add_argument('ref', type=str, nargs='?', help='Data file (positional)')
    parser.add_argument('toys', type=str, nargs='?', help='MC file (positional)')
    parser.add_argument('--ref', type=str, dest='ref_flag', help='Data file (with flag)')
    parser.add_argument('--toys', type=str, dest='toys_flag', help='MC file (with flag)')
    parser.add_argument('--year', type=int, default=None, help='Year of data taking')
    parser.add_argument('--savename', type=str, default='gofs/gof_X', help='Save name for the plot')
    parser.add_argument('--algo', type=str, default='saturated', choices=['saturated', 'ks'], help='Algorithm to use for the plot')
    parser_debug = parser.add_argument_group("DEBUG Options")
    parser_debug.add_argument(
        "--verbose", "-v", "-_v", action="store_true", help="Verbose logging"
    )
    parser_debug.add_argument(
        "--debug", "-vv", "--vv", action="store_true", help="Debug logging"
    )
    args = parser.parse_args()
    log_level = logging.WARNING
    if args.verbose:
        log_level = logging.INFO
    if args.debug:
        log_level = logging.DEBUG
    logging.getLogger("matplotlib").setLevel(logging.WARNING)
    logging.getLogger("fsspec").setLevel(logging.WARNING)
    logging.getLogger("ROOT").setLevel(logging.WARNING)
    logging.basicConfig(
        level=log_level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True, tracebacks_suppress=[click])],
    )

    # Resolve positional vs flag arguments
    if args.ref_flag is not None:
        args.ref = args.ref_flag
    if args.toys_flag is not None:
        args.toys = args.toys_flag
    # Ensure required arguments are provided
    if args.ref is None or args.toys is None:
        parser.error("Both data file (ref) and MC file (toys) must be specified")


    gofplot(args.ref, args.toys, savename=args.savename, algo=args.algo, year=args.year, title="GoF plot")
    