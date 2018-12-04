#!/usr/bin/env python
import sys

old_author = None
n_cites = 0

for line in sys.stdin:
    try:
        author, cites = line.split(',')

        if author == old_author:
            n_cites += int(cites)
        else:
            print('{0},{1}'.format(old_author, n_cites))
            n_cites = int(cites)
        old_author = author
    except:
        pass

if old_author is not None:
    print('{0},{1}'.format(old_author, n_cites))
