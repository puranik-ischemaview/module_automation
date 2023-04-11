import os
import subprocess
from conftest import *
import logging


def ssh_activate_conda():
    logging.info("Method: ssh_activate_conda")
    argsexec = "conda activate ich_scripts"
    os.system(argsexec)


def ssh_generate_file_list(dir_name):
    logging.info("Method: ssh_generate_file_list")
    argsexec = 'rm -rf ' + os.environ['WORKING_DIR']
    return_code = os.system(argsexec)

    if return_code != 0:
        logging.info("Error while deleting the working directory\n")

    argsexec = 'python3 ' + os.environ['SCRIPT_PATH'] + '01_get_file_lists.py ' \
                                                        '/test_data/test_cases/ich_cases/cases/' + dir_name
    os.system(argsexec)


def ssh_run_motion_detector():
    logging.info("Method: ssh_run_motion_detector")
    argsexec = 'python3 ' + os.environ['SCRIPT_PATH'] + '02_run_motion_detector.py'
    os.system(argsexec)


def ssh_run_ich():
    logging.info("Method: ssh_run_ich")
    argsexec = 'python3 ' + os.environ['SCRIPT_PATH'] + '03_run_ich_3.py'
    os.system(argsexec)


def ssh_verify_directory_present(dir_name):
    logging.info("Method: ssh_verify_directory_present")
    # argexec = 'test -d ' + os.environ['WORKING_DIR'] + 'results_ich_3/' + dir_name
    argexec = 'test -d "' + os.environ['WORKING_DIR'] + 'results_ich_3/' + dir_name + '"'
    dir_path = os.environ['WORKING_DIR'] + 'results_ich_3/' + dir_name

    # test_var = os.listdir('"' + os.environ['WORKING_DIR'] + '"')
    # logging.info('"' + os.environ['WORKING_DIR'] + 'results_ich_3/' + dir_name + '"')
    # return_status = os.path.exists('"' + os.environ['WORKING_DIR'] + 'results_ich_3/' + dir_name + '"')
    result = subprocess.run(['test', '-d', dir_path])
    return_status = result.returncode
    return return_status


def ssh_copy_output_json_to_temp():
    logging.info("Method: ssh_copy_output_json_to_local")

    cmd = 'cp ' + os.environ['WORKING_DIR'] + 'results_ich_3/' + os.environ["DATASET_NAME"] + '/output.json ' + \
          os.environ["ROOT_DIR"] + '/temp_json/'
    return_code_copy = os.system(cmd)
    return return_code_copy


def ssh_verify_result_directory_content(context):
    logging.info("Method: ssh_verify_result_directory_content")
    results_root = os.environ['WORKING_DIR'] + 'results_ich_3/' + os.environ["DATASET_NAME"] + "/results/"
    file_count_matched = 0
    results_content_matched = False
    return_status = None
    return_code_dir = None

    for entry in context.table:
        name_to_check = entry['directory_content']
        argsexec = (results_root + name_to_check)
        if entry['type'] == "file":
            return_status = os.path.isfile(argsexec)
        else:
            return_status = os.path.exists(argsexec)

        if return_status is not None:
            if return_status == 0:
                logging.info("Found " + entry['type'] + ": " + entry['directory_content'])
                file_count_matched += 1
            else:
                logging.info("Not found " + entry['type'] + ": " + entry['directory_content'])

        if return_code_dir is not None:
            if return_code_dir.returncode == 0:
                logging.info("Found " + entry['type'] + ": " + entry['directory_content'])
                file_count_matched += 1
            else:
                logging.info("Not found " + entry['type'] + ": " + entry['directory_content'])

    if file_count_matched == len(context.table.rows):
        results_content_matched = True

    return results_content_matched


def ssh_verify_result_sub_directory_content(context):
    logging.info("Method: ssh_verify_result_sub_directory_content")
    results_root = os.environ['WORKING_DIR'] + 'results_ich_3/' + os.environ["DATASET_NAME"] + "/results/"
    file_count_matched = 0
    results_content_matched = False
    return_status = None
    return_code_dir = None

    for entry in context.table:
        name_to_check = entry['directory_content']
        argsexec = (results_root + name_to_check)
        if entry['type'] == "file":
            return_status = os.path.isfile(os.environ['WORKING_DIR'] + 'results_ich_3/' + argsexec)
        else:
            return_status = os.path.exists(os.environ['WORKING_DIR'] + 'results_ich_3/' + argsexec)

        if return_status is not None:
            if return_status == 0:
                logging.info("Found " + entry['type'] + ": " + entry['directory_content'])
                file_count_matched += 1
            else:
                logging.info("Not found " + entry['type'] + ": " + entry['directory_content'])

        if return_code_dir is not None:
            if return_code_dir.returncode == 0:
                logging.info("Found " + entry['type'] + ": " + entry['directory_content'])
                file_count_matched += 1
            else:
                logging.info("Not found " + entry['type'] + ": " + entry['directory_content'])

    if file_count_matched == len(context.table.rows):
        results_content_matched = True

    return results_content_matched
