# CapstoneProject Context

## Project

- **Title:** CSC 481 Capstone Project Comprehensive Web-Based Steganography Sandbox
- **Domain:** Full-stack development and system integration
- **Our Purpose:** Our goal as a team is to Build an educational web application that lets authorized users
  encrypt, embed, extract, inspect, and document steganography experiments.
- **Stack:** Flask or Django, Bootstrap, Python, Matplotlib, ReportLab or
  WeasyPrint, Pytest, and GitHub.

## Required capabilities

1. Image LSB, audio LSB, and zero-width-text embedding/extraction.
2. AES encryption before embedding and decrypt-after-extraction workflow.
3. Secure upload/download validation and filename sanitization.
4. A simple statistical detection module with understandable results.
5. Base64-embedded Matplotlib visualizations in the UI.
6. A PDF technical report automatically generated for every experiment.
7. Responsive Bootstrap interface, automated tests, and clear documentation.
8. Non-blocking job handling; Celery/Redis is optional when the synchronous
   implementation cannot meet the responsiveness target.

## Team ownership

- **Team Leader:** Jamaal Spratley - full-stack integration, REST API design, Git workflow,
  deployment, and release coordination.
- **Member A (Backend):** Bryan Goodman - steganography algorithms, encryption, service layer,
  and REST APIs.
- **Member B (Frontend/QA):** Kendra Pelzer - Bootstrap UI/UX, visualizations, Pytest suite,
  documentation, and accessibility checks.

## Working agreements

- Work in small feature branches; do not commit directly to `main`.
- Every merge requires a pull request, a second-team-member review, passing
  tests, and an updated issue/task reference.
- Treat uploaded content as untrusted: validate type, size, and dimensions or
  duration; never execute or expose raw user-supplied filenames.
- Keep AES keys and secrets out of source control; use environment variables.
- Preserve experiment metadata needed to reproduce the generated report.
- Keep the product educational and lawful: show a usage notice and do not
  include features intended to evade authorized monitoring.

## Definition of done

A feature is done when its acceptance criteria are implemented, tests pass,
the user-facing behavior is documented, error states are handled, and it is
merged through the team pull-request workflow.
