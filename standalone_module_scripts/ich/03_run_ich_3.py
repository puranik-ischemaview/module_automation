#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 11:24:32 2021

@author: sdivel
"""

import os
import subprocess
import numpy as np

dir_base = '/test_data/working_dir/ich3.0/'
dir_lists = dir_base + 'file_lists/'
dir_output = dir_base + 'results_ich_3/'

# get all lists
files = os.listdir(dir_lists)
files.sort()

os.chdir('/test_data/rapid_builds/ich_builds/ich3.0/product/hemorrhage_app')

# run for all lists, except for ones that already have results
for file in files:
    if file.endswith('.list'):
        case_name = os.path.splitext(file)[0]
        print(case_name)
        rerun_case = False

        artifact_file = dir_base + 'results_motion_detector/' + case_name + '/artifact_output.json'

        od = dir_output + case_name + '/'
        if not os.path.exists(od):
            os.makedirs(od)

        if os.path.exists(od + 'results/'):
            if len(os.listdir(od + 'results/')) == 0:
                rerun_case = True

        if rerun_case or not os.path.exists(od +'output.json'):
            if os.path.exists(artifact_file):
                argsexec = ('./hemorrhage_app',
                            '-od', od,
                            '-fl', dir_lists + file,
                            '-c', '/test_data/rapid_builds/ich_builds/ich3.0/product/hemorrhage_params.json',
                            '-v', '3',
                            '-af', artifact_file)
            else:
                argsexec = ('./hemorrhage_app',
                            '-od', od,
                            '-fl', dir_lists + file,
                            '-c', '/test_data/rapid_builds/ich_builds/ich3.0/product/hemorrhage_params.json',
                            '-v', '3')

            logfile = open(od +'rapid_processing.log','w')
            returncode = subprocess.call(argsexec, stdout=logfile, stderr=logfile)
            if returncode != 0:
                print('error. return code: {}\n'.format(np.uint8(returncode).view('int8')))
                logfile.write('error. return code: {}'.format(np.uint8(returncode).view('int8')))
            else:
                logfile.write('Processing finished with no error.')
            logfile.close()
