"""
Module which walks the baseline tree and:

    If a directory is found which does not exist
    at the corresponding position in the comparand tree,
        note this.

    If an individual file is found which does not exist
    at the corresponding position in the comparand tree,
        note this.

    If an individual file is found which is not equal
    to the corresponding file in the comparand tree,
        note this.
	Equality is determined by filecmp.cmp(f1, f2, shallow=True)
		which uses the os.stat() function to retrieve the os.stat_result
		structure of both files.  All fields uf the structure must match.

    This has no write/modify/delete effect on either tree.

    Entry point: execute.
"""
import os
from filecmp import cmp
import treecmp_utilities as util

MYNAME = "treecmp_walker"
TRACING = False # Keep quiet when starting traverse()
SHALLOW = True # Faster comparison since it only looks at fstat!

# === Entry point 'execute' called from treecmp_main.py =======================
def execute(arg_baseline_tree, arg_comparand_tree):

    ### Perform first traverse (recursive).
    acc_stats = util.AccStats()
    acc_stats = traverse(acc_stats, arg_baseline_tree, arg_comparand_tree)

    ### Return final counters.
    return acc_stats

def traverse(arg_acc_stats, arg_baseline_tree, arg_comparand_tree):
    """
    This is the mechanics of the target tree traverse.
    Note that this function is RECURSIVE.
    """
    if TRACING:
        util.logger("DEBUG %s/traverse: d-tot=%d, f-tot=%d, d-absent=%d, f-absent=%d, f-diff=%d, base=%s, comp=%s", \
                    MYNAME, arg_acc_stats.counter_d_total, arg_acc_stats.counter_f_total, \
                    arg_acc_stats.counter_d_absent, arg_acc_stats.counter_f_absent, \
                    arg_acc_stats.counter_f_diff, arg_baseline_tree, arg_comparand_tree)
    try:
        leaves = os.listdir(arg_baseline_tree)
    except EnvironmentError as ex:
        util.oops("%s/traverse: os.listdir {%s} failed, reason=%s",
                  MYNAME, arg_baseline_tree, ex.strerror)
    for leaf in leaves:
        path_baseline = os.path.join(arg_baseline_tree, leaf)
        path_comparand = os.path.join(arg_comparand_tree, leaf)
        if os.path.isdir(path_baseline):
            ### It's a Directory
            arg_acc_stats.counter_d_total += 1
            if TRACING:
                util.logger("%s: Visited baseline directory: %s", MYNAME, path_baseline)
            ### If the corresponding comparand path exists and is a directory
            ### then traverse
            ### Else flag a missing comparand directory
            if os.path.isdir(path_comparand):
                ### Ok, Traverse
                arg_acc_stats = traverse(arg_acc_stats, path_baseline, path_comparand)
            else: #Flag missing directory in comparand
                util.logger("%s: *Not found* %s", MYNAME, path_comparand)
                arg_acc_stats.counter_d_absent += 1
        else: # It's a file, not a directory.
            ### Skip this baseline file name if not a regular file (E.g. links, sockets, devices)
            if not os.path.isfile(path_baseline):
                continue
            arg_acc_stats.counter_f_total += 1
            if TRACING:
                util.logger("%s: Visited baseline file: %s", MYNAME, path_baseline)
            ### If the corresponding comparand file path exists and is a regular file
            ### then compare it to baseline file;
            ### Else flag a missing comparand file
            if os.path.isfile(path_comparand):
                if not cmp(path_baseline, path_comparand, shallow=SHALLOW):
                    util.logger("%s: *Unequal* comparand: %s", MYNAME, path_comparand)
                    arg_acc_stats.counter_f_diff += 1
            else:
                util.logger("%s: *Not found* comparand: %s", MYNAME, path_comparand)
                arg_acc_stats.counter_f_absent += 1

    return arg_acc_stats
