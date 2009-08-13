# Change Runner
# 
# Script to launch a command when files change in a watched directory
#
# Copyright (c) 2009 Tim Disney
# Licensed under the MIT license
import os, time
from optparse import OptionParser

sleep_time = 1

def watch_loop(command, path_to_watch):
    before = dict ([(f, os.stat(f).st_mtime) for f in sum([ [d + lf for lf in os.listdir(d) if lf[0] != '.' and lf[len(lf)-1] != "~"] for d in path_to_watch], [] )])
    while 1:
        time.sleep(sleep_time)
        after = dict ([(f, os.stat(f).st_mtime) for f in sum([ [d + lf for lf in os.listdir(d) if lf[0] != '.' and lf[len(lf)-1] != "~"] for d in path_to_watch], [] )])
        changed = [f for f in after if not f in before or after[f] != before[f]]
        if changed:
            print "---- Files changed: Running ----"
            os.system(command)
            print "---- Files changed: Finished ----"

        before = after

def main():
    usage = "usage: %prog [options] path_to_watch1 path_to_watch_2 ... path_to_watch_n"
    parser = OptionParser(usage)
    parser.add_option("-c", "--command", dest="command", help="Command to run when files change")
    (options, args) = parser.parse_args()
    watch_loop(options.command, args)
    
if __name__ == "__main__":
    main()
