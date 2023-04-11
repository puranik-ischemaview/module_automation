Feature: Verify the expected outputs for the standalone ICH module are achieved

  Background:
    Given module is set as "ich"
    And working directory is set for "ich3.0"
    And script path is set for "ich3.0"

  @ich
  Scenario: ICH - Verify Suspected ICH without Motion
    Given the file list for "ich_ncct_hem_no_motion" is generated
    And the motion detection script is executed
    When ich is executed for the dataset
    Then the results directory "ich_ncct_hem_no_motion" is created
    And the main result directory contains the following files
      | directory_content    | type |
      | debugSummary.png     | file |
      | output.json          | file |
      | rapid_processing.log | file |
      | rawInput.mhd         | file |
      | rawInput.raw         | file |
      | results/             | directory |
    And the results sub-directory contains the following files
      | directory_content    | type |
      | overviewImage.dcm    | file |
      | overviewImage.jpg    | file |
      | overviewImage.png    | file |
      | overviewImage.th.jpg | file |
      | summaryImage.dcm     | file |
      | summaryImage.jpg     | file |
      | summaryImage.png     | file |
      | summaryImage.th.jpg  | file |
    And output.json contains the following
      | key                   | value             |
      | ReturnCode            | 0                 |
      | ReturnCodeDescription | No error          |
      | HemorrhageDetected    | true              |
      | HemorrhageVolume      | 4.398292999267578 |
      | ICHSuspected          | true              |
    # Use the following in lieu of second part of the Expected result 2 where presence of different sections is verified
    And the structure of the output.json matches the output json for "ich_ncct_hem_no_motion"
    And verify the summary and overview images for "ich_ncct_hem_no_motion"
    And verify the rawInput.mhd file for "ich_ncct_hem_no_motion" contains all source images


  @ich
  Scenario: ICH - Verify Non-Suspected ICH without Motion
  Given the file list for "ich_ncct_no_hem_no_motion" is generated
  And the motion detection script is executed
  When ich is executed for the dataset
  Then the results directory "ich_ncct_no_hem_no_motion" is created
  And the main result directory contains the following files
    | directory_content    | type      |
    | output.json          | file      |
    | rapid_processing.log | file      |
    | rawInput.mhd         | file      |
    | rawInput.raw         | file      |
    | results/             | directory |
  And the results sub-directory contains the following files
    | directory_content    | type |
    | overviewImage.dcm    | file |
    | overviewImage.jpg    | file |
    | overviewImage.png    | file |
    | overviewImage.th.jpg | file |
    | summaryImage.dcm     | file |
    | summaryImage.jpg     | file |
    | summaryImage.png     | file |
    | summaryImage.th.jpg  | file |
  And output.json contains the following
    | key                   | value    |
    | ReturnCode            | 0        |
    | ReturnCodeDescription | No error |
    | HemorrhageDetected    | false    |
    | HemorrhageVolume      | 0.0      |
    | ICHSuspected          | false    |
#  # Use the following in lieu of second part of the Expected result 2 where presence of different sections is verified
  And the structure of the output.json matches the output json for "ich_ncct_no_hem_no_motion"
  And verify the summary and overview images for "ich_ncct_no_hem_no_motion"
  And verify the rawInput.mhd file for "ich_ncct_no_hem_no_motion" contains all source images

  @ich
  Scenario: ICH - Verify Suspected ICH with Motion
    Given the file list for "ich_ncct_hem_motion" is generated
    And the motion detection script is executed
    When ich is executed for the dataset
    Then the results directory "ich_ncct_hem_motion" is created
    And the main result directory contains the following files
      | directory_content    | type |
      | debugSummary.png     | file |
      | output.json          | file |
      | rapid_processing.log | file |
      | rawInput.mhd         | file |
      | rawInput.raw         | file |
      | results/             | directory |
    And the results sub-directory contains the following files
      | directory_content    | type |
      | overviewImage.dcm    | file |
      | overviewImage.jpg    | file |
      | overviewImage.png    | file |
      | overviewImage.th.jpg | file |
      | summaryImage.dcm     | file |
      | summaryImage.jpg     | file |
      | summaryImage.png     | file |
      | summaryImage.th.jpg  | file |
    And output.json contains the following
      | key                    | value             |
      | ReturnCode             | 0                 |
      | ReturnCodeDescription  | No error          |
      | HemorrhageDetected     | true              |
      | HemorrhageVolume       | 3.505456631836483 |
      | ICHSuspected           | true              |
      | ArtifactsDetected      | true              |
      | NumberOfSlicesAffected | 15                |
    # Use the following in lieu of second part of the Expected result 2 where presence of different sections is verified
    And the structure of the output.json matches the output json for "ich_ncct_hem_motion"
    And verify the summary and overview images for "ich_ncct_hem_motion"
    And verify the rawInput.mhd file for "ich_ncct_hem_motion" contains all source images

  @ich
  Scenario: ICH - Verify Non-Suspected ICH without Motion
  Given the file list for "ich_ncct_no_hem_motion" is generated
  And the motion detection script is executed
  When ich is executed for the dataset
  Then the results directory "ich_ncct_no_hem_motion" is created
  And the main result directory contains the following files
    | directory_content    | type      |
    | output.json          | file      |
    | rapid_processing.log | file      |
    | rawInput.mhd         | file      |
    | rawInput.raw         | file      |
    | results/             | directory |
  And the results sub-directory contains the following files
    | directory_content    | type |
    | overviewImage.dcm    | file |
    | overviewImage.jpg    | file |
    | overviewImage.png    | file |
    | overviewImage.th.jpg | file |
    | summaryImage.dcm     | file |
    | summaryImage.jpg     | file |
    | summaryImage.png     | file |
    | summaryImage.th.jpg  | file |
  And output.json contains the following
    | key                    | value               |
    | ReturnCode             | 0                   |
    | ReturnCodeDescription  | No error            |
    | HemorrhageDetected     | false               |
    | HemorrhageVolume       | 0.27108755918996263 |
    | ICHSuspected           | false               |
    | ArtifactsDetected      | true                |
    | NumberOfSlicesAffected | 17                  |
#  # Use the following in lieu of second part of the Expected result 2 where presence of different sections is verified
  And the structure of the output.json matches the output json for "ich_ncct_no_hem_motion"
  And verify the summary and overview images for "ich_ncct_no_hem_motion"
  And verify the rawInput.mhd file for "ich_ncct_no_hem_motion" contains all source images
