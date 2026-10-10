# TEAM 2 MIDTERM REPORT
## Project: Comprehensive Web-Based Steganography Sandbox

### Team Lead:
#### Team Member: Jamall Spratley

### 1. Milestones Achieved

### 2. Completed Subtasks

### 3. Testing and Validation

### 4. Lessons Learned

### 5. Individual Contribution Summary

##
### Member A:
#### Team Member: Bryan Goodman

### 1. Milestones Achieved

### 2. Completed Subtasks

### 3. Testing and Validation

### 4. Lessons Learned

### 5. Individual Contribution Summary

##
### Member B: Frontend Development & Quality Assurance
#### Team Member: Kendra Pelzer

### 1. Milestones Achieved

The frontend development and quality assurance portion of the project has progressed from initial planning and design to functional interfaces for image, audio, and zero-width text steganography.

The following milestones have been achieved:

-	Frontend Planning & Design: Established the initial user workflow, accessibility requirements, low-fidelity wireframes, QA checklist, and anticipated frontend API requirements.
-	Image Steganography Interface: Developed the initial Image LSB frontend interface with required input validation, user feedback, and automated browser tests.
-	Audio Steganography Interface: Developed the Audio LSB frontend interface with WAV file selection, input validation, and status feedback.
-	Frontend Integration Testing: Updated the existing image and audio automated test suites to accommodate changes introduced during application integration.
-	Zero-Width Text Interface: Developed the initial zero-width text embedding interface, including cover-text and secret-message fields.
-	Zero-Width Decryption Interface: Extended the zero-width frontend to support encoded-text-input, passphrase entry, message extraction, and read-only decoded-message output.

### 2. Completed Subtasks
#### Frontend Planning & Documentation

Developed initial design documentation outlining the application’s proposed user workflow, accessibility requirements, interface structure, and anticipated backend interactions. This includes requirements for experiment submission, job-status tracking, results retrieval, downloads, and error handling.

#### Image LSB Frontend Development

Created the initial image steganography interface with input fields for an image file, secret message, and passphrase. Implemented frontend validation to prevent incomplete submissions and provide appropriate status feedback.

#### Audio LSB Frontend Development

Developed the audio steganography interface to support WAV file selection, secret message entry, and passphrase validation. Maintained consistent interface behavior with the existing image workflow.

#### Frontend Integration and Test Maintenance

Updated the automated test following application integration changes. Adjustments accounted for updated file locations and expected frontend behavior, including the use of mocked API responses where appropriate.

#### Zero-Width Text Frontend Development

Created the initial zero-width text embedding interface with fields for cover text, secret message, an “Embed Message” button, and status area. Extended the interface to include decryption functionality, allowing users to enter encoded text and a passphrase, initiate extraction, and view the decoded message in a read-only output field.


### 3. Testing and Validation

#### Image Steganography Frontend

Purpose: Verify that the image frontend correctly validates the required inputs.

Test Cases:
- Reject submission when the image file is missing.
-	Reject submission when the secret message is missing.
-	Reject submission when the passphrase is missing.
-	Accept valid image, message, and passphrase inputs through frontend validation.

Result: All four automated Pytests passed. Manual browser testing confirmed the interface layout, required field behavior, and validation status feedback.

Evidence: *insert screenshots here*

#### Audio Steganography Frontend
Purpose: Verify that the audio interface correctly handles required inputs and provides validation feedback.

Test Cases:
-	Reject submission when the WAV file is missing.
-	Reject submission when the secret message is missing.
-	Reject submission when the passphrase is missing.
-	Accept valid WAV file, message, and passphrase inputs through frontend validation.
Result: All four automated Pytests passed. Manual browser testing confirmed the WAV file selection, required field validation, and successful status feedback.

Evidence: *insert screenshots here*

#### Image and Audio Integration Testing
Purpose: Verify that the existing frontend tests remain functional following integration changes.

Method: Update the automated tests to reflect the current application structure, file paths, and expected behavior. Mocked API responses were used where necessary to test frontend behavior independently.

Result: All eight automated tests passed, consisting of four image tests and four audio tests.

Evidence: *insert screenshots here*

#####  Zero-Width Text Decryption Frontend
Purpose: Verify that the zero-width decryption interface validates required inputs and displays the decoded message output field properly.

Test Cases:
-	Reject submission when the encoded text is missing.
-	Reject submissions when the decryption passphrase is missing.
-	Verify that the decoded message output field exists and is read-only.

Result: All three automated Pytests passed. Manual browser testing confirmed implementation of the zero-width interface, required field validation, and successful status feedback.

Evidence: *insert screenshots here*


### 4. Lessons Learned

### 5. Individual Contribution Summary

##
### Progress Against the Project Plan

