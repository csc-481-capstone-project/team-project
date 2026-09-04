# Frontend API Needs

## Purpose

This document identifies the backend information and actions required for the Steganography Sandbox frontend. Endpoint names and final request formats should be confirmed by the team before implementation.

## Frontend Actions

The frontend needs to support these user actions:

1. Start an embed experiment.
2. Start an extract experiment.
3. Check the status of a submitted experiment.
4. View completed experiment results and detection findings.
5. Download generated output files.
6. Download a generated PDF report.
7. Cancel an in-progress experiment when supported.

## Proposed API Needs

| Frontend feature | Proposed API action | Information needed |
|---|---|---|
| Start embed experiment | `POST /api/experiments/embed` | Carrier type, uploaded file or text, secret message, and passphrase. |
| Start extract experiment | `POST /api/experiments/extract` | Carrier type, uploaded encoded file or text, and passphrase. |
| View job status | `GET /api/experiments/{experiment_id}/status` | Current state, progress percentage, current processing step, and safe error details. |
| View results | `GET /api/experiments/{experiment_id}` | Operation details, output summary, detection results, visualizations, and download availability. |
| Download output | `GET /api/experiments/{experiment_id}/download` | A securely generated download response for the output carrier file. |
| Download PDF report | `GET /api/experiments/{experiment_id}/report` | A securely generated PDF report download response. |
| Cancel job | `POST /api/experiments/{experiment_id}/cancel` | Confirmation that cancellation was requested or completed. |

## Expected Experiment Status Values

| Status | Frontend behavior |
|---|---|
| `queued` | Show that the experiment was accepted and is waiting to start. |
| `processing` | Show a loading indicator, progress information, and current step when available. |
| `complete` | Display results, visualizations, and authorized download buttons. |
| `failed` | Display a safe, plain-language error message and a way to start over. |
| `cancelled` | Explain that the experiment was stopped and provide a way to begin another one. |

## Minimum Status Response Data

The job-status response should provide enough information for the frontend to update without guessing:

| Field | Purpose |
|---|---|
| `experiment_id` | Identifies the current experiment. |
| `status` | Indicates queued, processing, complete, failed, or cancelled. |
| `progress_percent` | Supports a progress bar when measurable. |
| `current_step` | Gives the user a plain-language processing update. |
| `message` | Provides a safe success, warning, or failure message. |
| `created_at` | Records when the experiment began. |
| `completed_at` | Records when the experiment finished, when applicable. |

## Minimum Result Data

A completed experiment should make the following information available to the frontend:

- Carrier type and operation type.
- Success or failure state.
- Output filename or authorized download link.
- Capacity or size details when relevant.
- Detection summary and plain-language interpretation.
- Visualization data or a visualization URL/base64 image.
- PDF report availability.
- Limitations or warnings associated with the result.

## Error-Handling Expectations

- Validation errors should identify the field or file problem without revealing sensitive server details.
- Unsupported file types, oversized files, malformed files, and missing required fields should return helpful messages.
- Incorrect passphrases must not reveal hidden plaintext.
- Failed or unauthorized downloads must show a safe error message.
- The frontend should not expose stack traces, internal file paths, keys, or server configuration.

## Open Team Decisions

The team should confirm these items before frontend integration begins:

- Flask or Django framework.
- Final endpoint names and request/response formats.
- Supported image, audio, and text file formats.
- File-size limits and carrier-capacity limits.
- Whether progress is delivered by polling, server-sent events, or another method.
- Whether cancellation is required for the first release.
- Authentication and authorization requirements for experiments and downloads.