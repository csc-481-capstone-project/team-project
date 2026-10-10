# TEAM 2 MIDTERM REPORT
## Project: Comprehensive Web-Based Steganography Sandbox

### Team Lead:
#### Team Member: Jamaal Spratley

### 1. Milestones Achieved
The app development and implimentation of the project has progressed from initial planning and design to functional interfaces for image, audio, and zero-width text steganography.

The following milestones have been achieved:
-	The initial creation of the GitHub repository with weekly plan developed.
- the development of the app.py using frontend and backend scripts for the upload of images into the browser for images
- the development of the app.py using frontend and backend scripts for the upload of images into the browser for audio
- the development of the app.py using frontend and backend scripts for the implementation of zero-width text into the browser 
- the implementation of decryption of zero-width text so secret messages are able to be taken out of the text.



### 2. Completed Subtasks
### the creation of the venv, requirements and the git-ignore files for later use.
created the venv for the sandbox and the ignore files so git hub would not ignore non important files.
### The first image uploaded test for the sandbox 
combined the scripts made for the frontend and backend image uploading to allow the sandbox to upload and download images for later decryption.
### The first audio file upload test for the sandbox 
combined the scripts made for the frontend and backend audio uploading to allow the sandbox to upload and download audio for later decryption.
### The first zero-width text tests for the sandbox
combined the scripts made for the frontend and backend zero-width text implementation to allow the sandbox to read and hide text for later decryption.
### The first zero-width text decryption test for the sandbox 
combined the scripts made for the frontend and backend zero-width text decryption to allow the sandbox to read and decrypt hidden text.


### 3. Testing and Validation

#### Image Steganography Frontend

Purpose: Verify that the image upload for the sandbox was working and running so images could be downloaded for the sandbox and uploaded to the sandbox.

Result: all images can be uploaded with a secret hidden message and downloaded with a secret message.

Evidence: *insert screenshots here*

#### Audio Steganography Frontend
Purpose: Verify that the audio upload for the sandbox was working and running so audio files could be downloaded for the sandbox and uploaded to the sandbox.

Result: all audio files. can be uploaded with a secret hidden message and downloaded with a secret message.

Evidence: *insert screenshots here*

### The first zero-width text tests for the sandbox
Purpose: Verify that the zero-width text page for the sandbox was working and running so text-files could be put into the website for encryption.

Result: all zero-width text files. can be encrypted 

Evidence: *insert screenshots here*

#####  Zero-Width Text Decryption Frontend
Purpose: Verify that the zero-width text page for the sandbox was working and running so zero-width text-files could be put into the website for decryption.

Result: all zero-width text files. can be decrypted.

Evidence: *insert screenshots here*




### 4. Lessons Learned
-png has multiple forms like RGB and RGBA.  
- learned that html files can only have one <!doctype> per file so with the use of two HTMLs I had to make a link so they would have their own space and not conflict.
- learned that HTML files need to be properly structured for the information to show at the right point, for instance if you have a button you want at the bottom of the web site, the code must be positioned last under everything else.
- zero-width text needs a certain text size for the payload so the longer the hidden text, the longer your non-hidden text has to be to avoid corruption.

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

