import os
import logging
from conftest import *
import cv2
import subprocess
import SimpleITK as sitk
import numpy as np

__REFERENCE_IMAGE_DIR__ = os.environ["ROOT_DIR"] + '/reference_images'
__MODULE__ = 'ich'
__DCM_CMP__ = os.environ["ROOT_DIR"] + '/utilities/dcmicmp'


def compare(context, dir_name):
    ref_images_location = __REFERENCE_IMAGE_DIR__ + '/' + __MODULE__ + '/' + dir_name + '/'
    match_status = 1
    actual_image_location = os.environ['WORKING_DIR'] + 'results_ich_3/' + dir_name + '/results/'
    list_entry_comparisons = []

    for im in os.listdir(actual_image_location):

        actual_image = actual_image_location + im
        ref_image = ref_images_location + im

        destination = os.environ["EVIDENCE_PATH"] + '/'
        result = subprocess.run(['cp', actual_image, destination])

        if im.lower().endswith(('.jpg', '.png')):

            act1 = cv2.imread(actual_image)
            exp1 = cv2.imread(ref_image)

            if act1.shape == exp1.shape:
                logging.info("The images have same size and channels for image " + im)

            difference = cv2.subtract(act1, exp1)
            b, g, r = cv2.split(difference)

            if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                logging.info("Actual image matches expected - " + im)
                list_entry_comparisons.append("match")
            else:
                logging.error("Actual image does not match expected - " + im)
                list_entry_comparisons.append("mismatch")

        elif im.lower().endswith('.dcm'):
            pass
            cmd = os.environ["ROOT_DIR"] + '/dcmicmp'
            result = subprocess.run([cmd, ref_image, actual_image])
            if result.returncode == 0:
                logging.info("Actual image matches expected - " + im)
                list_entry_comparisons.append("match")
            else:
                logging.error("Actual image does not match expected - " + im)
                list_entry_comparisons.append("mismatch")

    if list_entry_comparisons.count("mismatch") > 0:
        match_status = 1
    else:
        match_status = 0

    return match_status


def verify_raw_input_mhd(context, dir_name):
    match_status = 1
    list_entry_comparisons = []
    raw_input_mhd_file = os.environ['WORKING_DIR'] + 'results_ich_3/' + dir_name + '/rawInput.mhd'
    itk_volume = sitk.ReadImage(raw_input_mhd_file)

    destination = os.environ["EVIDENCE_PATH"] + '/'
    subprocess.run(['cp', raw_input_mhd_file, destination])

    match __MODULE__:
        case 'ich':
            # Image PixelType: 32-bit float
            if sitk.GetPixelIDValueAsString(itk_volume.GetPixelID()) == '32-bit float':
                logging.info(f"Image PixelType as expected: {sitk.GetPixelIDValueAsString(itk_volume.GetPixelID())}")
                list_entry_comparisons.append(0)
            else:
                logging.error(f"Image PixelType does not match expected. Expected: '32-bit float', Actual: {sitk.GetPixelIDValueAsString(itk_volume.GetPixelID())}")
                list_entry_comparisons.append(1)

            # Image Size: (512, 512, 33)
            size_vector = itk_volume.GetSize()
            if 200 < size_vector[0] < 800 and 200 < size_vector[1] < 800 and 1 < size_vector[2] < 1000:
                logging.info(f"Image size as expected: {size_vector}")
                list_entry_comparisons.append(0)
            else:
                logging.error(f"Image size does not match expected. Actual: {size_vector}")
                list_entry_comparisons.append(1)

            images = sitk.GetArrayFromImage(itk_volume)
            if np.amax(images) > 10 and (np.amax(images) - np.amin(images) > 100):
                logging.info(f"Difference in minimum and maximum pixel intensity is greater than 100: {np.amax(images) - np.amin(images)} and the maximum pixel intensity is greater than 10: {np.amax(images)}")
                list_entry_comparisons.append(0)
            else:
                logging.error(f"Difference in minimum and maximum pixel intensity and/or maximum pixel intensity is "
                              f"not in the expected range. Actual Difference: {np.amax(images) - np.amin(images)}, "
                              f"Actual maximum pixel intensity: {np.amax(images)}")
                list_entry_comparisons.append(1)

    if list_entry_comparisons.count(1) > 0:
        match_status = 1
    else:
        match_status = 0

    return match_status
