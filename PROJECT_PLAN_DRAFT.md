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

| Week | Tasks | Responsible | Expected outcome | Testing requirements | GitHub deliverables |
|---|---|---|---|---|---|

| Week | Tasks | Responsible | Expected outcome | Testing requirements | GitHub deliverables |
|---|---|---|---|---|---|
| 1 | Define scope, responsible-use policy, security goals, and Git workflow requiring feature branches and pull requests | Jamaal Spratley + Kendra Pelzer + Bryan Goodman | Approved project plan and contribution process | Review security risks and branch/PR rules | `README.md`,  `meetingminutes.md` |
| 2 | Design system architecture: frontend, backend, async jobs, Redis/Celery option, file storage, visualization, and reporting flow | Jamaal Spratley + Bryan Goodman + Kendra Pelzer | Shared architecture and data-flow design | Team architecture review | `PROJECT_PLAN_DRAFT.md`, `AGENTS.md` |
| 3 | Set up repository, CI, branch protections, formatting, linting, tests, and pull-request checks | Jamaal Spratley | Enforced, repeatable engineering workflow | Verify CI blocks failed lint/build/test checks | GitHub Actions, branch policy documentation, issue templates |
| 4 | Build responsive frontend shell, navigation, loading states, error states, and accessible component system | Bryan Goodman | UI foundation that clearly supports long-running jobs | Responsive and accessibility testing | Frontend application shell, component tests |
| 5 | Build backend foundation: authentication, authorization, API conventions, job-status model, and audit logging | Kendra Pelzer | Secure API platform supporting user-scoped work | Unit tests for access controls and invalid requests | Backend API, OpenAPI specification, auth tests |
| 6 | Implement secure file upload handling: MIME/type checks, filename sanitization, size limits, image/PDF validation, isolated storage | Kendra Pelzer | Safe upload pipeline for permitted files | Invalid extension, oversized, malformed, and path-traversal tests | Upload service, security tests, upload policy documentation |
| 7 | Implement secure download handling: generated filenames, authorization checks, expiring links or controlled endpoints, safe response headers | Kendra Pelzer | Users can safely retrieve only their own generated files | Unauthorized download, header, and filename-sanitization tests | Download endpoint, integration tests, security notes |
| 8 | Build asynchronous job processing for encode/decode operations using Celery/Redis or an equivalent queue | Kendra Pelzer | Long-running work does not block the web request/UI | Queue retry, failure, timeout, and concurrent-job tests | Worker service, queue configuration, job API documentation |
| 9 | Connect frontend to asynchronous jobs: progress polling/status updates, cancellation handling, loading indicators, and result retrieval | Bryan Goodman + Kendra Pelzer | Smooth UI that remains usable while jobs run | End-to-end success, failure, retry, and cancellation tests | Job-status UI, E2E test suite |
| 10 | Implement LSB image encoding/decoding with capacity validation and secure temporary-file lifecycle | Kendra Pelzer | Reliable baseline steganography workflow | Round-trip, capacity-boundary, corrupted-image, and cleanup tests | fixtures, algorithm documentation |
| 11 | Build dynamic analysis visualizations: histograms, channel views, bit-plane views, and capacity charts generated with Matplotlib and embedded as base64 HTML images | Bryan Goodman + Kendra Pelzer | Interactive, self-contained visual analysis results | Validate chart generation, base64 rendering, and large-image performance | Visualization service, analysis pages, visual tests |
| 12 | Generate downloadable PDF reports using ReportLab or WeasyPrint, including job metadata, visualizations, findings, and responsible-use notice | Kendra Pelzer + Bryan Goodman | Polished report per completed job | PDF content, layout, download authorization, and malformed-input tests | Report generator, report templates, sample report fixtures |
| 13 | Add optional encryption, rate limits, quotas, and abuse-reporting controls | Kendra Pelzer + Jamaal Spratley | Safer public-facing sandbox with operational controls | Encryption vectors, wrong-password, quota, and rate-limit tests | Encryption module, rate-limit middleware, operations guide |
| 14 | Run security, performance, accessibility, and reliability hardening across uploads, jobs, visualizations, downloads, and reports | Jamaal Spratley + Bryan Goodman + Kendra Pelzer | Release candidate meets agreed quality bar | OWASP review, dependency scan, load tests, WCAG audit, queue stress test | Test reports, remediation PRs, release checklist |
| 15 | Beta release through pull requests only; gather feedback, triage issues, fix defects, and finalize user/admin documentation | Jamaal Spratley + Bryan Goodman + Kendra Pelzer | Stable, documented beta | Full regression, user acceptance, and PR review verification | Beta tag, changelog, user guide, deployment guide |
| 16 |demonstrate end-to-end workflow, perform rollback drill, and document retrospective/roadmap | Jamaal Spratley + Bryan Goodman + Kendra Pelzer | Production-ready steganography sandbox | Production smoke test, download/report verification, rollback test | final deployment docs, final presentation (Q&A) |
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
