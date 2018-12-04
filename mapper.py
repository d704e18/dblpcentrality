#!/usr/bin/env python
import sys

article_key = ''
for line in sys.stdin:
    line = line.strip()
    if line.startswith('</'):
        line = line[line.find('>') + 1:]
    if line.startswith(('<article', '<inproceedings', '<proceedings', '<book', '<incollection', '<phdthesis',
                        '<mastersthesis', '<www', '<person', '<data')):
        key_start_index = line.find('key="') + 5
        key_end_index = line[key_start_index:].find('"') + key_start_index
        article_key = line[key_start_index:key_end_index]
    if line.startswith('<author'):
        author_start_index = line.find('>') + 1
        author_end_index = line[author_start_index:].find('<') + author_start_index
        author = line[author_start_index:author_end_index]
        print('{0},{1},-1'.format(article_key, author))
    if line.startswith(('<cite', '<crossref')):
        cite_start_index = line.find('>') + 1
        cite_end_index = line[cite_start_index:].find('<') + cite_start_index
        cite = line[cite_start_index:cite_end_index]
        if cite != '...':
            print('{0},-1,{1}'.format(cite, 1))
