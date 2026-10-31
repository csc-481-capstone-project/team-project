# Team 2 Week 11 Progress Report

## Comprehensive Web-Based Steganography Sandbox 

**Team:** Bryan Goodman, Kendra Pelzer, Jamaal Spratley
#
**Reporting period:** Week 11
## 1. Milestones achieved
- Implemented an image LSB Statistical Detection Module that analyzes the balance of least-significant-bit values in PNG images, returning with low, medium, or high suspicion level.
- 
- Iplementation of image statistical Detection 

## 2. Subtasks completed
| Subtask | Owner | Completed work |
| --- | --- | --- |
| Team Leader | Jamaal Spratley | Full implementation of image statistical detection for app.py|
| Member A (Backend) | Bryan Goodman | Ensured the audio steganography communicates with the main branch. Completed Pytest for audio steganography and make sure there are no warnings. |
| Member B (Frontend/QA) | Kendra Pelzer | Developed the image steganography decryption interface with PNG upload, passphrase input, extraction button, status feedback, and read-only message field. Created and successfully completed three automated Pytests to verify input validation and output field configuration. |

## 3. Test evidence

### 3.1 Bryan

**Purpose:** Create and implement statistical detection module for the backend services. 

**Expected Result:** Creation of script that has no errors when the pytest is implemented. 

**Result:** Completion of two pytest. One for the testing of the module and the other is full pytest to ensure everything is communicating. 


**Completed Pytest**

![Statisical Detection Test_detection.py](statisticaldetectionpytest.png)

*Image 1: test_dection.py pytest*

![Full Pytest All Passed after testing](FullStatisticalDetectionPytest.png)

*Image 2: Completion of Full pytest to ensure complete communication with other services. 

#
### 3.2 Frontend Audio Decryption - Kendra

**Frontend Tests:**


**Expected result:**


**Result:** 


![Image_Decryption PyTest](Image_Decryption_Automation_Week10.png)

*Image 3: 


#
### 3.3 Jamaal

**Purpose:** Create and implement statistical detection module for the app.py.
**Expected result:** the app.py accepting any image and determining if the images have a hidden message already embedded in it.

**Result:**  The statistical detection is working and running.

![Statistical detection in](statdet.png)
*Image 4:
![statistical detection out](statdettest.png)
*Image 5:

## 4. Lessons learned

- I learned that a statistical detection result is a helpful indicator, but it does not prove that hidden data is within the image. Testing the module with different LSB patterns helps ensure that the detection values act accordingly.
- 
- I learned that statistical detection is not always accurate since smaller messages change the image's pixel data less

## 5. Progress against the plan

The Week 11 the plan required the creation of the statistical detection module for backend services, ensure that complete communication occurred with a completed full pytest, and full implementation of the module with the other services. 


The Week 12 plan will be to implement the PDF export. 
