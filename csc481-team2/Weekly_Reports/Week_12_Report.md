# Team 2 Week 12 Progress Report

## Comprehensive Web-Based Steganography Sandbox 

**Team:** Bryan Goodman, Kendra Pelzer, Jamaal Spratley
#
**Reporting period:** Week 12
## 1. Milestones achieved
- 
- 
- 

## 2. Subtasks completed
| Subtask | Owner | Completed work |
| --- | --- | --- |
| Team Leader | Jamaal Spratley | Full implementation of statistical detection for app.py|
| Member A (Backend) | Bryan Goodman | Ensured the audio steganography communicates with the main branch. Completed Pytest for audio steganography and made sure there are no warnings. |
| Member B (Frontend/QA) | Kendra Pelzer | Developed statistical detection frontend sections for image, audio, and zero-width text steganography. Updated the zero-width page layout and created automated frontend tests to verify the new elements. |

## 3. Test evidence

### 3.1 Bryan

**Purpose:** 

**Expected Result:** 

**Result:** 


**Completed Pytest**

![Statisical Detection Test_detection.py](Testservicespytest(full).png)

*Image 1: *

![Full Pytest All Passed after testing](CompletePytest.png)

*Image 2:*

#
### 3.2 Frontend Statistical Detection - Kendra

**Frontend Tests:**
Verify that the new statistical detection interfaces for image, audio, and zero-width text steganography display the required elements correctly.

**Expected result:**
All three interfaces should display their respective detection forms and input fields, with the results sections initially hidden until analysis via backend is available.

**Result:**
PASS. All three automated frontend Pytests passed. The tests confirmed that the detection forms, input fields, and status elements were present and the results sections were hidden.

![Statistical_Detection PyTest](Statistical_Detection_Week11.png)
*Image 3: All three statistical detection frontend tests passed successfully*


#
### 3.3 Jamaal

**Purpose:** Create and implement a statistical detection module for the app.py.
**Expected result:** the app.py accepts any png,wave or zero-width file and determines if it has a hidden message already embedded in it.

**Result:**  The statistical detection is working and running.

![Statistical detection audio](stataudio.png)
*Image 4:
![statistical detection image](statdettest.png)
*Image 5:
![statistical detection zero-width](statzero.png)
*Image 6:

## 4. Lessons learned

- 
- 
- 

## 5. Progress against the plan

The Week 12 the plan required 


The Week 13 plan will be to  
