#!/usr/bin/env python
import sys

n_cites = 0
old_article = None

for line in sys.stdin:
    article, author, cites = line.split(',')

    is_cite = False
    if author == '-1':
        is_cite = True

    if article == old_article:
        if is_cite:
            n_cites += 1
        else:
            print('{0},{1}'.format(author, n_cites))
    elif article != old_article and is_cite:
        n_cites = 1

    old_article = article

if old_article is not None:
    print("{0},{1}".format(old_article, n_cites))
