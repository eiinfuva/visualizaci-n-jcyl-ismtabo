#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:30:08 2015

@author: ismtabo
"""

import csvunicode
import itertools
from sys import argv
from sys import exit
import sys
from os import path
from os import popen
import json
import simplejson

if len(argv) < 2:
    exit('Usage: %s path-csv-file destination-path' % argv[0])

# Verify all arguments are introduce
if not path.exists(argv[1]):
    exit('Error: csv file, %s doesn\'t exists' % argv[1])

if not path.exists(argv[1]):
    exit('Error: destination path, %s doesn\'t exists' % argv[1])

file_path = argv[1]
dest_path = argv[2]

# Read source CSV
reader = csvunicode.UnicodeReader(file(file_path,'r'),delimiter=';')

# Define de header of the table
reader.next()
# header = reader.next()
header = ['year']
# header[0] = 'Energia'
data = {}

# Separate each row
for row in reader:
    if row[0] not in data.keys():
        data[row[0]]=[[int(row[1]),int(row[2].replace('.',''))]]
    else:
        data[row[0]].append([int(row[1]),int(row[2].replace('.',''))])


jsonArray = []

for k,v in data.iteritems():
    jsonArray.append({"key":k, "values":v})

print jsonArray

with open(dest_path+'/'+argv[1].split('/')[-1].split('.')[0]+".json","w") as json_file:
    # json.dump(jsonArray,json_file)
    json_file.write(simplejson.dumps(jsonArray,indent=4,skipkeys=True, sort_keys=True))



# print 'Total %d rows readed' % (len(rows)+1)

# # Group csv tuples by its first value name
# groups = itertools.groupby(rows,lambda x: x[1].split('. ')[0])
# keys = []
# mini_groups = []
# for k,g in groups:
#     keys.append(k)
#     mini_groups.append(list(g))
#
# # Rewrite each group in its own file
# for key, group in zip(keys,mini_groups):
#     writer = csvunicode.UnicodeWriter(file(dest_path+'/'+key.lower()+'_mod.csv','w'),delimiter=';')
#     # writer.writerow(header)
#     writer.writerow(header)
#     for elem in list(group):
#         # elem[0] = file_path.split('/')[-1].split('.')[0] #file name(type of energy)
#         writer.writerow(elem)
#         # writer.writerow(elem)
#
# print 'Total %d files created' % (len(keys))
