# # -- FILE:features/environment.py
#
#
# def before_all(context):
#     # -- SET LOG LEVEL: behave --logging-level=ERROR ...
#     # on behave command-line or in "behave.ini".
#     # context.config.setup_logging(configfile="behave.ini")
#     # context.config.setup_logging(configfile="behave_logging.ini")
#     context.config.setup_logging()
# # -- ALTERNATIVE: Setup logging with a configuration file.
# # context.config.setup_logging(configfile="behave_logging.ini")

import logging
import os


def before_all(context):
    print("Executing before all")
    cmd = 'wget wget https://www.dropbox.com/s/gh7fgzp99ujo2u1/dcm_compare.zip'
    os.system(cmd)
    cmd = 'unzip dcm_compare.zip'
    os.system(cmd)
    cmd = 'cp dcm_compare/dcmicmp .'
    os.system(cmd)

    cmd = 'wget https://www.dropbox.com/s/6jfd64gyx7trau3/reference_images.zip'
    os.system(cmd)
    cmd = 'unzip reference_images.zip'
    os.system(cmd)

    cmd = 'rm -rf dcm_compare'
    os.system(cmd)

    cmd = 'rm -rf dcm_compare.zip'
    os.system(cmd)

    cmd = 'rm -rf reference_images.zip'
    os.system(cmd)


def before_feature(context, feature):
    print("Before feature\n")
    # Create logger
    context.logger = logging.getLogger('automation_tests')
    context.logger.setLevel(logging.INFO)


def before_scenario(context, feature):
    print("Before scenario\n")
    # Set evidence path
    os.environ["EVIDENCE_PATH"] = context.evidence_path + '/'

# def before_scenario(context, scenario):
    # print("User data:", context.config.userdata)
    # logging.INFO("Test Details: " + context.scenario.name)

# def after_scenario(context, scenario):
#     print("scenario status" + scenario.status)
#     context.browser.quit()
#
#
# def after_feature(context, feature):
#     print("\nAfter Feature")
#
#
# def after_all(context):
#     print("Executing after all")
