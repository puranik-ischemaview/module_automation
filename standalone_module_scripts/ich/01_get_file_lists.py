#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 11:10:19 2021

@author: sdivel
"""

import os
import sys
import pathlib

dir_cases = sys.argv[1]
print("test data directory: " + dir_cases)

# case_names = os.listdir(dir_cases)
# case_names.sort()

dir_lists = '/test_data/working_dir/ich3.0/file_lists'
if not os.path.exists(dir_lists):
    os.makedirs(dir_lists)
    
# get file names
files = os.listdir(dir_cases)
files.sort()

if '.DS_Store' in files:
	files.remove('.DS_Store')

case_name = pathlib.PurePath(dir_cases).name
print("case name: " + case_name)

# open list file
f = open(dir_lists + "/" +  case_name + '.list', 'w')

for file in files:
	f.write('%s\n' % (dir_cases + '/' + file))

f.close()
