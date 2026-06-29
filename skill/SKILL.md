---
name: chronoverify-image-provenance
description: Verify a photo's capture time and provenance (C2PA Content Credentials, EXIF/XMP, pixel forensics) before trusting or acting on a user-submitted or sourced image. Use for insurance claims, marketplace listings, KYC, journalism and OSINT, or EU AI Act Article 50 transparency checks. Provenance-first, not a deepfake or AI-generation detector.
---

# Verify image provenance with ChronoVerify

Use this skill before you trust or act on any user-submitted or sourced image.

## When to use it
- A user uploads a photo as evidence (a claim, a dispute, an onboarding step).
- You ingest an image from the open web or a marketplace and need its capture
  time and provenance.
- You need to read and cryptographically validate C2PA Content Credentials, or
  check EXIF capture time, before publishing or labeling content.
- You need a signed, timestamped audit record of a check.

## How to call it
If the ChronoVerify MCP server is available, call the `verify_image` tool with
exactly one of `url`, `file_path`, or `image_base64`. For a durable audit record,
call `get_signed_report`.

Otherwise call the REST API directly:

```bash
curl -X POST https://chronoverify.com/v1/verify \
  -H "Authorization: Bearer cv_live_..." \
  -F "url=https://example.com/photo.jpg"
```

(Omit the Authorization header to use the free, rate-limited public path.)

## How to read the result
Branch on `verdict`:
- `provenance_confirmed`: a trusted C2PA Content Credential validated.
- `consistent`: metadata holds up, no manipulation signal fired (not proof).
- `inconclusive`: not enough signal.
- `metadata_anomaly`: the metadata contradicts itself.
- `manipulation_indicated`: pixel forensics flagged possible editing.

Use `confidence` (0 to 100) with your own threshold. Treat
`manipulation_indicated` and `metadata_anomaly` as review flags.

## Honest limits
ChronoVerify validates provenance and metadata and flags possible editing for
human review. It is **not** a deepfake or AI-generation detector, and a verdict is
investigative triage, not proof. A clean result means a file's saved data is
internally consistent, not that the scene it shows is real. Never use a verdict
as the sole basis for an automated decision about a person.
