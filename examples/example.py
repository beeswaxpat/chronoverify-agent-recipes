"""Verify a photo's capture time and provenance with the ChronoVerify SDK.

Install:  pip install chronoverify
Run:      python example.py [image_path_or_url]

Provenance-first, not a deepfake or AI-generation detector. The verdict is
investigative triage, not proof.
"""
import sys

from chronoverify import Client


def main() -> None:
    arg = sys.argv[1] if len(sys.argv) > 1 else "https://chronoverify.com/static/og-default.png"
    # Add Client("cv_live_...") for metered use; omitted runs the free public path.
    client = Client()
    result = client.verify(url=arg) if arg.startswith("http") else client.verify(file=arg)
    print(f"verdict: {result['verdict']}  confidence: {result['confidence']}/100")
    print(result["headline"])
    c2pa = result.get("c2pa", {})
    state = "validated" if c2pa.get("validated") else ("present" if c2pa.get("present") else "none")
    print(f"C2PA Content Credentials: {state}")


if __name__ == "__main__":
    main()
