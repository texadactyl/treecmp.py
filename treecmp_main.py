"""
treecmp main program

	python3   treecmp.py   tree-1   tree-2

"""
import os
import sys
import time
import treecmp_utilities as util
import treecmp_walker

MYNAME = "treecmp_main"
REPORTER = "reporter"

#==================================================================================================

def reporter(arg_elapsed_time, arg_acc_stats, arg_baseline, arg_comparand):
    if arg_elapsed_time > 0.01:
        util.logger("%s: Elapsed seconds = %.2f", REPORTER, arg_elapsed_time)
    util.logger("%s: Baseline: %s, Comparand: %s", REPORTER, arg_baseline, arg_comparand)
    util.logger("%s: Total of %d subdirectories and %d files", \
                REPORTER, arg_acc_stats.counter_d_total, arg_acc_stats.counter_f_total)
    errs = arg_acc_stats.counter_d_absent + arg_acc_stats.counter_f_absent + arg_acc_stats.counter_f_diff
    if errs == 0:
        util.logger("%s: No inconsistencies detected", REPORTER)
    else:
        util.logger("%s: Subdirectories missing in comparand: %d", REPORTER, arg_acc_stats.counter_d_absent)
        util.logger("%s: Files missing in comparand: %d", REPORTER, arg_acc_stats.counter_f_absent)
        util.logger("%s: File miscompares: %d", REPORTER, arg_acc_stats.counter_f_diff)

#==================================================================================================

if __name__ != "__main__":
    util.oops("%s: Must be run as a main program", MYNAME)

util.logger("%s: Begin", MYNAME)
nargs = len(sys.argv)

if nargs != 3:
    util.oops("%s: Needs 2 arguments: Treetop-1 and Treetop-2", MYNAME)

TT1 = sys.argv[1]
TT2 = sys.argv[2]

### Make sure the treetops exist and are accessible
if not os.path.exists(TT1):
    util.oops("%s: Treetop 1 {%s} does not exist or is inaccessible",
              MYNAME, TT1)
if not os.path.exists(TT2):
    util.oops("%s: Treetop 2 {%s} does not exist or is inaccessible",
              MYNAME, TT2)

### Walk TT1
epoch_time_start = time.time()
acc_stats = treecmp_walker.execute(TT1, TT2)
epoch_time_stop = time.time()
elapsed_time = epoch_time_stop - epoch_time_start
reporter(elapsed_time, acc_stats, TT1, TT2)
acc_stats = None

### Walk TT2
epoch_time_start = time.time()
acc_stats = treecmp_walker.execute(TT2, TT1)
epoch_time_stop = time.time()
elapsed_time = epoch_time_stop - epoch_time_start
reporter(elapsed_time, acc_stats, TT2, TT1)

util.logger("%s: End", MYNAME)
