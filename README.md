# module_automation

This framework is intended to be used for testing standalone modules. The test framework is written in Python and uses the behaveX plugin for Gherkin support. All tests are written in Given-When-Then format. The framework must be executed on a Rapid server. 

The framework is self-contained and once setup, it is capable of executing tests without needing any manual intervention.

Due to the file size limitations in github, reference images are maintained in Dropbox https://www.dropbox.com/s/6jfd64gyx7trau3/reference_images.zip

Also a dcmtk binary for comparing dcm files is maintained in Dropbox https://www.dropbox.com/s/gh7fgzp99ujo2u1/dcm_compare.zip

**NOTE**: If this repository retires, we will move the files to the new repository that is implemented in it's lieu. The framework code takes care of downloading and setting up the appropriate folder structure for these files from Dropbox.

If the test requires verifying output images, it is expected that the test engineer will manually review the output images and then place them in the directory structure defined for the reference images to be used by the automation framework. We don't anticipate too many changes to the reference images in Dropbox unless a new version/release changes image definitions or new datasets are introduced. Anytime a change is made to the reference images we should raise a corresponding PR in this repository to ensure changes were peer-reviewed.

Follow the instructions mentioned below to setup local framework code:

1. On the Rapid server, install a conda package (preferably Miniconda).

2. Fork this github repository to create your remote copy.

3. Clone your fork onto the Rapid server. Alternatively, you may clone it on your laptop, compress, and copy to your Rapid server.

4. SSH to the Rapid server terminal and change directory to the automation code.

5. Create a new environment using conda. Environments can be reused and will not need to be created every time.

***e.g. conda create -n module_automation python=3.10***

**NOTE**: Make sure the python version is 3.10. Our code uses switch statements which are not supported in older versions of python.

6. Activate the newly created environment.

***e.g. conda activate module_automation***

7. Install python packages required by the automation code. From the project's main directory execute the following command:

***pip install -r requirements.txt***

8. Execute tests using a command like below:

***behavex  -t @ich --no-capture***

@t is the tag parameter. This command will execute all scenarios that have the ich tag.

9. Once the test is completed, a report.html will be generated in the output directory. The report contains summary of test results, individual tests with results for each step, and captured evidence.

For sharing purposes, the entire output folder must be copied to ensure correct rendering of the report.html file

## TEST DATA
1. On your Rapid server, the test data must be maintained in the following directory structure

|module  | test data directory |
|--|--|
| ich | /test_data/test_cases/ich_cases/cases/ |

## REFERENCES

1. behaveX: https://behavex.readthedocs.io/

2. behave: https://behave.readthedocs.io/en/stable/

## REPOSITORY GOOD PRACTICES
1. Always fork the repository and make any changes to your fork.

2. Once the changes have been made and are tested to ensure they work as expected and do not break anything else in the framework, raise a PR (Pull Request) to merge the changes into the upstream branch. **PR template, approver requirements soon to follow**

3. Once a release is completed, create a new branch for that release. It will make it easier to maintain test changes between releases and anytime a RAR needs to be performed on an older release.

4. The main branch will always be used for the newest release.
