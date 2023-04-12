#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 16:04:59 2022

@author: sdivel
"""

import os
import subprocess

dir_base = '/test_data/working_dir/ich3.0/'
dir_lists = dir_base + 'file_lists/'
dir_output = dir_base + 'results_motion_detector/'

# get all lists
files = os.listdir(dir_lists)
files.sort()

# run for all lists, except for ones that already have results
for file in files:
    if file.endswith('.list'):
        case_name = os.path.splitext(file)[0]
        print(case_name)
        run_case = False

        od = dir_output + case_name + '/'
        if not os.path.exists(od):
            os.makedirs(od)
            run_case = True
        elif not os.path.exists(od + 'artifact_output.json'):
            run_case = True

        if run_case:
            argsexec = ('/opt/rapid4/bin/ct-motion-artifact-detector/ncct_artifacts/ncct_artifacts',
                        'predict',
                        '-v', '3',
                        '-od',  od,
                        '-op', 'artifact',
                        '--filelist', dir_lists + file)

            logfile = open(od +'rapid_processing.log','w')
            returncode = subprocess.call(argsexec, stdout=logfile, stderr=logfile)
            logfile.close()

            if returncode != 0:
                print('error\n')
