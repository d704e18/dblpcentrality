#!/usr/bin/env python
import sys

article_key = ''
for line in sys.stdin:
    if '<article' in line:
        key_start_index = line.find('key=') + 4
        key_end_index = line[key_start_index:].find('>') + key_start_index
        article_key = line[key_start_index:key_end_index]
    if '<author' in line:
        author_start_index = line.find('>') + 1
        author_end_index = line[author_start_index:].find('<') + author_start_index
        author = line[author_start_index:author_end_index]
        print('{0}\t{1}'.format(article_key, author))
