import subprocess

from flatten_json import flatten
import json
from conftest import *
import re
from deepdiff import DeepDiff
import os
import logging

__REFERENCE_JSON_DIR__ = os.environ["ROOT_DIR"] + '/reference_jsons/ich'
__TEMP_JSON__ = os.environ["ROOT_DIR"] + '/temp_json/output.json'


def output_json_verify_key_value(context):
    key_value_found = False

    with open(__TEMP_JSON__, "rb") as read_file:
        actual_json = json.load(read_file)

    destination = os.environ["EVIDENCE_PATH"] + '/'
    subprocess.run(['cp', __TEMP_JSON__, destination])

    list_entry_comparisons = []

    for entry in context.table:
        expected_result = None
        match entry['key']:
            case 'ReturnCode' | 'ReturnCodeDescription':
                # case 'ReturnCodeDescription':
                # if entry['key'] in actual_json and str(actual_json[entry['key']]) == (str(entry['value'])):
                if entry['key'] in actual_json:
                    if entry['value'].isnumeric():
                        expected_result = int(entry['value'])
                    elif type(entry['value']) == bool:
                        expected_result = bool(entry['value'])
                    else:
                        expected_result = str(entry['value'])
                if actual_json[entry['key']] == expected_result:
                    list_entry_comparisons.append("match")
                    # logging.info("Key-value pair found and matched: ", entry)
                    logging.info("Key-value pair found and matched: " + entry['key'] + "-" + entry['value'])
                else:
                    list_entry_comparisons.append("mismatch")
                    # logging.error("Key-value pair not found or not matched: ", entry)
                    logging.error("Key-value pair not found or not matched: " + entry['key'] + "-" + entry['value'])
            case 'HemorrhageDetected':
                # case 'HemorrhageVolume':
                if entry['key'] in actual_json['Results']['Hemorrhage']:
                    if entry['value'].isnumeric():
                        expected_result = int(entry['value'])
                    elif type(entry['value']) == bool:
                        expected_result = bool(entry['value'])
                    elif entry['value'] == 'true':
                        expected_result = True
                    elif entry['value'] == 'false':
                        expected_result = False
                    else:
                        expected_result = str(entry['value'])

                if actual_json['Results']['Hemorrhage'][entry['key']] == expected_result:
                    list_entry_comparisons.append("match")
                    # logging.info("Key-value pair found and matched: ", entry)
                    logging.info("Key-value pair found and matched: " + entry['key'] + "-" + entry['value'])
                else:
                    list_entry_comparisons.append("mismatch")
                    # logging.error("Key-value pair not found or not matched: ", entry)
                    logging.error("Key-value pair not found or not matched: " + entry['key'] + "-" + entry['value'])
            case 'HemorrhageVolume':
                try:
                    expected_result = float(entry['value'])
                except ValueError:
                    expected_result = str(entry['value'])
                if actual_json['Results']['Hemorrhage'][entry['key']] == expected_result:
                    list_entry_comparisons.append("match")
                    # logging.info("Key-value pair found and matched: ", entry)
                    logging.info("Key-value pair found and matched: " + entry['key'] + "-" + entry['value'])
                else:
                    list_entry_comparisons.append("mismatch")
                    # logging.error("Key-value pair not found or not matched: ", entry)
                    logging.error("Key-value pair not found or not matched: " + entry['key'] + "-" + entry['value'])
            case 'ICHSuspected':
                if entry['value'] == 'true':
                    expected_result = True
                elif entry['value'] == 'false':
                    expected_result = False
                if entry['key'] in actual_json['Results'] and actual_json['Results'][entry['key']] == expected_result:
                    list_entry_comparisons.append("match")
                    # logging.info("Key-value pair found and matched: ", entry)
                    logging.info("Key-value pair found and matched: " + entry['key'] + "-" + entry['value'])
                else:
                    list_entry_comparisons.append("mismatch")
                    # logging.error("Key-value pair not found or not matched: ", entry)
                    logging.error("Key-value pair not found or not matched: " + entry['key'] + "-" + entry['value'])
            case 'NumberOfSlicesAffected':
                if entry['key'] in actual_json['NCCTArtifacts']['Results']['MotionArtifacts']:
                    if entry['value'].isnumeric():
                        expected_result = int(entry['value'])
                    elif type(entry['value']) == bool:
                        expected_result = bool(entry['value'])
                    else:
                        expected_result = str(entry['value'])
                if actual_json['NCCTArtifacts']['Results']['MotionArtifacts'][entry['key']] == expected_result:
                    list_entry_comparisons.append("match")
                    # logging.info("Key-value pair found and matched: ", entry)
                    logging.info("Key-value pair found and matched: " + entry['key'] + "-" + entry['value'])
                else:
                    list_entry_comparisons.append("mismatch")
                    # logging.error("Key-value pair not found or not matched: ", entry)
                    logging.error("Key-value pair not found or not matched: " + entry['key'] + "-" + entry['value'])
            case 'ArtifactsDetected':
                if entry['value'] == 'true':
                    expected_result = True
                elif entry['value'] == 'false':
                    expected_result = False
                if entry['key'] in actual_json['NCCTArtifacts']['Results']['MotionArtifacts'] and actual_json['NCCTArtifacts']['Results']['MotionArtifacts'][entry['key']] == expected_result:
                    list_entry_comparisons.append("match")
                    # logging.info("Key-value pair found and matched: ", entry)
                    logging.info("Key-value pair found and matched: " + entry['key'] + "-" + entry['value'])
                else:
                    list_entry_comparisons.append("mismatch")
                    # logging.error("Key-value pair not found or not matched: ", entry)
                    logging.error("Key-value pair not found or not matched: " + entry['key'] + "-" + entry['value'])
            case _:
                logging.info("Invalid key provided: ", entry['key'])

        list_entry_comparisons.append(key_value_found)

    if list_entry_comparisons.count("mismatch") > 0:
        key_value_found = False
    else:
        key_value_found = True

    return key_value_found


def match_json(context, dir_name):
    match_status = 1
    expected_json_path = os.path.join(__REFERENCE_JSON_DIR__, dir_name, 'output.json')
    with open(__TEMP_JSON__,
              "rb") as read_file:
        json_actual = json.load(read_file)

    with open(expected_json_path,
              "rb") as read_file:
        json_expected = json.load(read_file)

    # context.attach("application/json", json_actual)

    exclude_paths = re.compile(r"\'ProcessingBegin\'|\'ProcessingEnd\'|\'ProcessingTimeInSeconds\'")
    match_status = DeepDiff(json_expected, json_actual, exclude_regex_paths=[exclude_paths], verbose_level=0)

    if len(match_status.tree) == 0:
        logging.info("The structure of output.json matches the expected structure.")
    else:
        logging.error("The structure of output.json does not match the expected structure. The following values do "
                      "not match: ", match_status.tree)

    return len(match_status.tree)