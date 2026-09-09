# Frontend UX and QA Plan

## Purpose

This document defines the user-facing workflow, accessibility expectations, and quality-assurance checks for the Comprehensive Web-Based Steganography Sandbox.

## Proposed User Workflow

1. A user selects an operation: Embed or Extract.
2. The user chooses a carrier type: Image, Audio, or Text.
3. The user uploads or enters the required carrier content.
4. For embedding, the user enters a secret message and passphrase.
5. The application validates the input and starts an experiment.
6. The user sees job status updates while processing occurs.
7. When complete, the user can view results, detection findings, visualizations, and download generated files or a PDF report.

## Planned Pages

| Page | Purpose |
|---|---|
| Home | Explain the educational purpose, ethical-use notice, and supported carrier types. |
| Embed | Form for uploading a carrier and embedding an encrypted message. |
| Extract | Form for uploading encoded content and extracting with a passphrase. |
| Job Status | Shows queued, processing, complete, or failed status. |
| Results | Shows output details, detection findings, and download options. |
| Reports | Lists and downloads generated PDF experiment reports. |
| Error States | Provides clear, safe feedback for invalid files, incorrect passphrases, and failed jobs. |

## Form and Validation Requirements

- Every input has a visible label and helpful instructions.
- File types and maximum upload sizes are shown before upload.
- Invalid, unsupported, malformed, or oversized files show clear error messages.
- Passphrases are masked and never displayed in results or reports.
- Submit buttons are disabled while a request is being processed.
- Errors use text as well as color so they are understandable to all users.

## Job Status and Results

The interface should display these states:

- Queued: The experiment has been accepted and is waiting to start.
- Processing: The application is embedding, extracting, analyzing, or generating a report.
- Complete: Results and authorized downloads are available.
- Failed: A plain-language error is shown without exposing sensitive system details.

## Accessibility Requirements

- Keyboard-only navigation must work for all pages and forms.
- Form fields must have programmatic labels.
- Status and validation messages must be readable by screen readers.
- Text and controls must meet readable color-contrast expectations.
- Layouts must remain usable on desktop and mobile-sized screens.

## Initial QA Checklist

- [ ] Valid image, audio, and text workflows complete successfully.
- [ ] Unsupported file types are rejected safely.
- [ ] Oversized files are rejected with a helpful message.
- [ ] Missing required fields prevent submission.
- [ ] Incorrect passphrases fail without revealing plaintext.
- [ ] Job failures show safe, understandable feedback.
- [ ] Generated files and PDF reports download correctly.
- [ ] Forms and results work with keyboard navigation.
- [ ] Pages remain usable on a mobile-sized screen.

## Backend/API Needs

The frontend will need documented endpoints or contracts for:

- Creating an embed or extract experiment
- Checking experiment/job status
- Retrieving completed results
- Downloading generated carrier files
- Downloading an experiment PDF report