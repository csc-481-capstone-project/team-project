# Team 2 Week 6 Progress Report

## Comprehensive Web-Based Steganography Sandbox 

**Team:** Bryan Goodman, Kendra Pelzer, Jamaal Spratley
#
**Reporting period:** Week 6

## 1. Milestones achieved
- Bryan
- Updated and verified automated frontend test suites for the integrated image and audio steganography interfaces and developed the initial frontend interface for zero-width text steganography.
- Jamaal

## 2. Subtasks completed
| Subtask | Owner | Completed work |
| --- | --- | --- |
| Team Leader | Jamaal Spratley |  |
| Member A (Backend) | Bryan Goodman |  |
| Member B (Frontend/QA) | Kendra Pelzer | Updated image and audio frontend automated tests, verified all eight tests passed, and developed the initial zero-width text steganography HTML interface. |

## 3. Test evidence

### 3.1 Bryan

**Purpose:**

**Expected Result:**

**Result:** 

**Completed Pytest**

*insert image here*

*Image 1:*

#
### 3.2 Frontend Integration Testing and Zero-Width Text Interface - Kendra

**Frontend Tests:**
Existing Pytest frontend tests were updated to support the current integrated image and audio steganography workflows.

**Expected result:**
Image and audio frontend interfaces correctly validate required inputs and successfully complete automated tests against the current integrated workflow.

**Result:** 
PASS. All four audio frontend tests and all four image frontend tests passed after the test suites were updated. An initial zero-width text steganography frontend interface was also developed with required Cover Text and Secret Message fields, an Embed Message button, and a status area for future backend integration.

![Audio PyTest](Audio_Test_Validation.png)

*Image 2: Audio Steganography frontend automated testing with all four Pytests passing*

![Image PyTest](Image_Test_Validation.png)

*Image 3: Image Steganography frontend automated testing with all four Pytests passing*

![Zero Width](Zero_Width_Skeleton.png)

*Image 4: Initial Zero-Width Text Steganography frontend interface*

#
### 3.3 Jamaal

**Purpose:**

**Expected result:**

**Result:**

*insert image here*

*Image 5:*

## 4. Lessons learned

- Bryan
- I learned how frontend tests may need to be updated when application integration changes file locations and expected behavior. I also gained experience using mocked API responses to test frontend functionality independently of backend availability and reinforced the importance of using reliable file paths in automated tests.
- Jamaal

## 5. Progress against the plan

The Week 5 plan required...

The Week 7 will focus on...
