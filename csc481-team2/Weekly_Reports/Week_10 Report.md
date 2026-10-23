# Team 2 Week 10 Progress Report

## Comprehensive Web-Based Steganography Sandbox 

**Team:** Bryan Goodman, Kendra Pelzer, Jamaal Spratley
#
**Reporting period:** Week 10
## 1. Milestones achieved
- Completion of the image steganography decryption process. The backend can now extract an encrypted message from a PNG image, decrypt it with the correct passphrase, and safely reject an incorrect passphrase.
- 
- 

## 2. Subtasks completed
| Subtask | Owner | Completed work |
| --- | --- | --- |
| Team Leader | Jamaal Spratley | Implemented audio into the app and ran the first test for encoding and now decoding |
| Member A (Backend) | Bryan Goodman | Ensured the audio steganography communicates with the main branch. Completed Pytest for audio steganography and make sure there are no warnings. |
| Member B (Frontend/QA) | Kendra Pelzer | Developed the audio steganography decryption interface, including status feedback and a read-only message output field. Created and successfully completed three automated Pytest. |

## 3. Test evidence

### 3.1 Bryan

**Purpose:** Verify image steganography can extract encrypted message from PNG image and decrypt correctly with proper passphrase. 

**Expected Result:** Pytest completion with no errors or expected warnings. 

**Result:**  Pytest completed with no warnings and 100% passed. 


**Completed Pytest**

![Test_audio_lsb.py Pytest](Pytest_test_audio.png)

*Image 1: 

![Audio_lsb.py Pytest](Pytest_audio_passed.png)

*Image 2: 

#
### 3.2 Frontend Audio Decryption - Kendra

**Frontend Tests:**


**Expected result:**


**Result:** 


![Audio_Decryption PyTest](Audio_Decryption_Automation_Week9.png)

*Image 3:*


#
### 3.3 Jamaal

**Purpose:** 

**Expected result:** 

**Result:** 

![audio encryption](audioin.png)
![audio decryption](audioout.png)


## 4. Lessons learned

- I learned that testing both the correct and incorrect passphrase paths are important. Features are not secure unless it is able to have the authorized message recovered safely while rejecting unauthorized access. 
- 
- 

## 5. Progress against the plan

The Week 10 the plan required completing and testing image steganography decryption, including correct and incorrect passphrase handling. 

The Week 11 will focus on working towards
