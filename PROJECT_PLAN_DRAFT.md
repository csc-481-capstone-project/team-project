# Comprehensive Web-Based Steganography Sandbox

**Status:** Team Project Plan for CSC 481 Capstone Project Comprehensive Web-Based Steganography Sandbox
**Planned delivery window:** August 31 - November 25, 2026  
**Final presentation and demonstration:** 29 November 2026

## 1. Project charter

### Goal

Deliver a secure, web-based educational sandbox where an authorized user can
run reproducible steganography experiments using image LSB, audio LSB, and
zero-width text. For each experiment, the application encrypts the payload
with AES before embedding, presents a basic detection assessment and visual
evidence, and produces a downloadable PDF technical report.

### Success criteria

| Area | Measurable outcome |
|---|---|
| Core carriers | A user can embed and extract a test payload successfully in image LSB, audio LSB, and zero-width text workflows. |
| Encryption | The embedded payload is AES-encrypted; extraction without the correct key/passphrase fails safely and does not reveal plaintext. |
| Secure handling | Unsupported, oversized, malformed, and path-manipulation uploads are rejected with safe errors; downloaded files use server-generated names. |
| Detection | Each supported carrier yields at least one documented statistical signal, a plain-language interpretation, and a visualization where meaningful. |
| UI responsiveness | Valid experiment submission gives immediate progress feedback; long jobs do not freeze the browser. |
| Reporting | Every completed experiment generates a readable PDF with inputs, configuration, outputs, detection results, visualizations, and limitations. |
| Quality | Automated unit/integration tests pass for core logic and APIs; the README documents setup, usage, limitations, and legal/ethical use. |

### Scope boundary

The project is an educational laboratory, not a production secure-messaging
service or forensic certification tool. The statistical detector presents
heuristics and limitations, not proof that content is or is not steganographic.

## 2. Architecture and work products

| Component | Owner | Primary outputs |
|---|---|---|
| Application foundation | Jamaal Spratley | Repository structure, configuration, REST API contract, CI, deployment runbook |
| Core steganography | Bryan Goodman| Image/audio/text embed-extract modules, carrier validation, test vectors |
| Cryptography and services | Bryan Goodman| AES utility, key/passphrase handling policy, experiment orchestration APIs |
| Web experience | Kendra Pelzer | Bootstrap pages, accessible forms, progress/status display, download flows |
| Detection and visuals | Kendra Pelzer with Bryan Goodman review | Statistical heuristics, Matplotlib charts, plain-language results |
| Reporting | Kendra Pelzer with Jamaal Spratley review | PDF template, experiment report generator, report validation |
| Quality and documentation | Kendra Pelzer | Pytest suite, test plan, README, user guide, final demo script |
| Integration and release | Jamaal Spratley | Pull-request enforcement, end-to-end tests, staging/deployment, release tag |

## 3. Milestones, dependencies, and acceptance gates

| Milestone | Target | Depends on | Exit criteria |
|---|---|---|---|
| M1 - Foundation and design | Oct 6 | None | Repository, issue board, API contract, threat model, wireframes, and sample carriers approved. |
| M2 - Carrier and encryption core | Oct 20 | M1 | All three carrier workflows pass known-good round-trip tests; AES integration is reviewed. |
| M3 - Integrated user workflow | Nov 4 | M2 | UI can submit, monitor, extract, and download an experiment through stable APIs. |
| M4 - Detection and reporting | Nov 11 | M3 | Heuristics, visualizations, and per-experiment PDF reports work end to end. |
| M5 - Quality and release candidate | Nov 18 | M4 | Security/error tests, regression suite, documentation, and deployment rehearsal are complete. |
| M6 - Final demonstration | Nov 25 / TBD | M5 | Tagged release, rehearsed demo, presentation artifacts, and retrospective are complete. |

## 4. Weekly task breakdown and ownership

| Week / dates | Jamaal Spratley | Bryan Goodman - Backend | Kendra Pelzer - Frontend/QA | Shared milestone |
|---|---|---|---|---|
| 1: Aug 31-Oct 6 | Create repo, branches/PR rules, issue board, API draft | Research libraries; define carrier interfaces and test vectors | Wireframes, Bootstrap design tokens, test-plan outline | M1 design review and scope lock |
| 2: Oct 7-13 | Scaffold Flask/Django app, config, CI, upload policy | Implement AES utility and image-LSB round trip | Build layout, upload form, validation/error UI | Image workflow usable locally |
| 3: Oct 14-20 | Integrate APIs, review security controls | Implement audio LSB and zero-width text modules; unit tests | Create experiment/history UI and API test fixtures | M2 carrier-core gate |
| 4: Oct 21-27 | Define job/status API and staging environment | Add extraction endpoints and robust file validation | Add progress/status components and accessibility pass | End-to-end embed/extract beta |
| 5: Oct 28-Nov 4 | Integrate all workflows; resolve API/UI defects | Add experiment metadata persistence and error handling | Connect UI to APIs; add download flows and smoke tests | M3 integrated beta |
| 6: Nov 5-11 | Review report schema and performance risks | Implement/verify detection service inputs and API results | Build charts, detection explanations, PDF report template/generation | M4 report-and-detection gate |
| 7: Nov 12-18 | Deployment rehearsal, release checklist, PR audit | Security/edge-case fixes and performance profiling | Regression suite, docs, accessibility, user guide | M5 release candidate |
| 8: Nov 19-25 | Release tag, demo coordination, presentation integration | Technical demo segment; final core fixes only | QA sign-off, final report samples, demo flow | M6 final demo and retrospective |

## 5. Operating schedule

| Cadence | Participants |
|---|---|
| Every Saturday | Team members will meet every Saturday to discuss next week's plans, combine work, and submit a weekly update/assignments.

### Team norms and availability assumptions

- Each member reserves two focused implementation blocks weekly plus the three
  team touchpoints above.
- Work is visible on the issue board before implementation begins.
- A blocker is escalated in the team channel within one business day.
- No new feature begins during Week 8 without unanimous agreement; only
  demonstration-critical fixes are admitted.

## 6. Git and quality workflow

1. Create a GitHub issue with acceptance criteria and assign one accountable owner.
2. Create a branch named `feature/<issue>-<short-description>` or
   `fix/<issue>-<short-description>`.
3. Open a pull request early; link the issue and include test evidence.
4. Require one teammate review, passing CI, no secrets, and resolved comments
   before merge.
5. Squash-merge to `main`, close the issue, and update the relevant
   documentation or release notes.

Minimum automated coverage includes algorithm round trips, invalid/malformed
input, wrong-key extraction, API validation, report generation, and at least
one end-to-end workflow per carrier. Manual checks cover visual usability,
responsive layout, downloaded-file naming, and PDF legibility.

## 7. Key risks and responses

| Risk | Likelihood / impact | Response | Owner |
|---|---|---|---|
| Audio formats and LSB capacity are inconsistent | Medium / High | Support a small, documented format set first; validate capacity before processing; use fixture files. | Bryan Goodman |
| Upload or download security flaw | Medium / High | Allowlist formats, size limits, server-side filenames, isolated storage, and negative tests. | Jamaal Spratley + Bryan Goodman |
| UI blocks during file processing | Medium / Medium | Return an experiment ID/status promptly; use background worker if measured processing exceeds the responsiveness target. | Jamaal Spratley |
| PDF/report data does not match experiment | Low / High | Generate reports from immutable experiment metadata and test a representative report per carrier. | Kendra Pelzer |
| Late integration failures | Medium / High | Demo cross-team integration every Wednesday; keep API contract versioned and tested. | Jamaal Spratley |
| Scope pressure | High / Medium | Preserve the three carrier round trips and report workflow; defer advanced detection and optional Celery/Redis only by recorded team decision. | Entire team |

## 8. Final demonstration checklist

- Demonstrate one successful encrypted embed/extract workflow for each carrier.
- Demonstrate a safe rejection of an invalid upload and a wrong-key failure.
- Show detection results and at least one visualization.
- Download and inspect a generated technical PDF report.
- Show tests passing, GitHub PR history, and the deployment or local-run guide.
- State limitations, ethical-use notice, and future improvements.

## 9. Decisions required at the first team meeting

1. Confirm Flask or Django, the supported image/audio formats, and AES
   passphrase/key-management approach.
2. Set file-size and carrier-capacity limits.
3. Choose ReportLab or WeasyPrint and decide whether Celery/Redis is needed.
4. Replace role labels with names; confirm availability and the final
   presentation date.
5. Approve this draft before it is saved as the final Word document and merged
   to the shared repository.
