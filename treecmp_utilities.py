"""
treecmp utility functions + the accumulated statistics class def'n
"""
from time import localtime, strftime

def logger(arg_format, *arg_list):
    """
    Time-stamp logger using sprintf-style argument passing.
    """
    now = strftime("%Y-%m-%d %H:%M:%S ", localtime())
    fmt = "{nstr} {fstr}".format(nstr=now, fstr=arg_format)
    print(fmt %arg_list)

def oops(arg_format, *arg_list):
    """
    Report an error and exit to the O/S.
    Use sprintf-style argument passing.
    """
    logger("*** Oops, " + arg_format, *arg_list)
    raise UserWarning("Execution aborted")

class AccStats:
    def __init__(self):
        self.counter_d_total = 0
        self.counter_d_absent = 0
        self.counter_f_total = 0
        self.counter_f_absent = 0
        self.counter_f_diff = 0
