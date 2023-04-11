from behavex import *
from behave import *
from utilities import *
import os


@given(u'module is set as "{module_name}"')
def set_module_name(context, module_name):
    os.environ["MODULE_NAME"] = module_name


@given(u'working directory is set for "{module_name}"')
def set_working_dir(context, module_name):
    os.environ["WORKING_DIR"] = '/test_data/working_dir/' + module_name + '/'


@given(u'script path is set for "{module_name}"')
def set_script_path(context, module_name):
    os.environ["SCRIPT_PATH"] = '/test_data/scripts/ich_scripts/ich_test/test/'


@given(u'the file list for "{dir_name}" is generated')
def generate_file_list(context, dir_name):
    print("Step: Generate file list for dataset - ", dir_name)
    os.environ["DATASET_NAME"] = dir_name
    remote_operations.ssh_generate_file_list(dir_name)


@given('the motion detection script is executed')
def run_motion_detector(context):
    print("Step: Run the motion detection script.")
    remote_operations.ssh_run_motion_detector()


@when('ich is executed for the dataset')
def run_ich(context):
    print("Step: Run ich script.")
    remote_operations.ssh_run_ich()


@then('output.json contains the following')
def verify_output_json(context):
    print("Step: Verify key value pairs in output.json.")
    return_code_copy = 1
    return_code_copy = remote_operations.ssh_copy_output_json_to_temp()
    all_key_value_matched = False
    all_key_value_matched = json_operations.output_json_verify_key_value(context)
    print("Output json result: ", all_key_value_matched)
    assert all_key_value_matched == True, 'At least one key-value pair was not found or did not match the expected result'


@then('the main result directory contains the following files')
def verify_result_directory_contents(context):
    print("Step: Verify contents of the main results directory.")
    match_status = False
    match_status = remote_operations.ssh_verify_result_directory_content(context)
    assert match_status == True, 'At least one of the files was not found'


@then('the results directory "{dir_name}" is created')
def verify_results_directory(context, dir_name):
    print("Step: Verify results directory is created.")
    return_code_actual = 1
    return_code_actual = remote_operations.ssh_verify_directory_present(dir_name)
    assert return_code_actual == 0, 'Results directory was not found'


@then('the results sub-directory contains the following files')
def verify_results_sub_directory(context):
    print("Step: Verify contents of the results sub-directory.")
    match_status = False
    match_status = remote_operations.ssh_verify_result_sub_directory_content(context)
    assert match_status == True, 'At least one of the files was not found'


@then('the structure of the output.json matches the output json for "{dir_name}"')
def json_match_structure(context, dir_name):
    print("Step: Verify output.json matches the expected format.")
    match_status = 1
    match_status = json_operations.match_json(context, dir_name)
    assert match_status == 0, 'Actual output.json structure does not match the expected'


@then('verify the summary and overview images for "{dir_name}"')
def verify_output_images(context, dir_name):
    print("Step: Verify the output images.")
    match_status = 1
    match_status = image_operations.compare(context, dir_name)
    assert match_status == 0, 'At least one of the output image(s) does not match expected'


@then('verify the rawInput.mhd file for "{dir_name}" contains all source images')
def verify_raw_input_mhd(context, dir_name):
    print("Step: Verify the rawInput.mhd file contains all source images")
    match_status = 1
    match_status = image_operations.verify_raw_input_mhd(context, dir_name)
    assert match_status == 0, 'rawInput.mhd does not contain all source images'
