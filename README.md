# treecmp
Compare 2 directory trees, specified on the command line.  Neither tree or its leaves are altered.  Inconsistencies are flagged in standard output.

The comparison is done in 2 phases: 
1. The first argument is the baseline tree and the 2nd argument is the comparand tree.
2. The comparison is run with reversed roles.

Sample invocation:

     python3   treecmp_main.py   $HOME/baseline   /mnt/my_usb_disk/another_copy_of_baseline

Yes, it will run with Python2 as well as Python3.

A perfect match will produce output like this:

```
2019-01-16 17:36:55  treecmp_main: Begin
2019-01-16 17:36:55  reporter: Baseline: /home/elkins/log/aa, Comparand: /home/elkins/log/bb
2019-01-16 17:36:55  reporter: Total of 0 subdirectories and 10 files
2019-01-16 17:36:55  reporter: No inconsistencies detected
2019-01-16 17:36:55  reporter: Baseline: /home/elkins/log/bb, Comparand: /home/elkins/log/aa
2019-01-16 17:36:55  reporter: Total of 0 subdirectories and 10 files
2019-01-16 17:36:55  reporter: No inconsistencies detected
2019-01-16 17:36:55  treecmp_main: End
```

If anything is inconsistent, then the output is more verbose.  For example, if directory aa has one more file (yy_extraneous.png) than bb, then output like what follows will appear:

```2019-01-16 17:39:15  treecmp_main: Begin
2019-01-16 17:39:15  treecmp_walker: *Not found* in comparand: /home/elkins/log/bb/yy_extraneous.png
2019-01-16 17:39:15  reporter: Baseline: /home/elkins/log/aa, Comparand: /home/elkins/log/bb
2019-01-16 17:39:15  reporter: Total of 0 subdirectories and 11 files
2019-01-16 17:39:15  reporter: Subdirectories missing in comparand: 0
2019-01-16 17:39:15  reporter: Files missing in comparand: 1
2019-01-16 17:39:15  reporter: File miscompares: 0
2019-01-16 17:39:15  reporter: Baseline: /home/elkins/log/bb, Comparand: /home/elkins/log/aa
2019-01-16 17:39:15  reporter: Total of 0 subdirectories and 10 files
2019-01-16 17:39:15  reporter: No inconsistencies detected
2019-01-16 17:39:15  treecmp_main: End
```
Feel free to contact richard.elkins@gmail.com for inquiries and issues, especially if you find any bugs. I'll respond as soon as I can.

Richard Elkins

Dallas, Texas, USA, 3rd Rock, Sol, ...
