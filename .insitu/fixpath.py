#!/usr/bin/env python3
import os
import sys
def path_remove(target):
    """Remove target from PATH"""
    delim = ':'
    old_path = os.environ['PATH']
    old_parts = old_path.split(delim)
    new_parts = [xx for xx in old_parts if not xx==target ]
    new_path = delim.join(new_parts)
    return new_path

def main():
    target = sys.argv[1]
    new_path = path_remove( target )
    print( new_path )
if __name__=='__main__':
    main()

