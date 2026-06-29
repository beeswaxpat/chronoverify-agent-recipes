// Verify a photo's capture time and provenance with the ChronoVerify SDK.
//
// Install:  npm i chronoverify
// Run:      npx tsx example.ts [image_path_or_url]
//
// Provenance-first, not a deepfake or AI-generation detector. The verdict is
// investigative triage, not proof.
import { ChronoVerify } from "chronoverify";

const arg = process.argv[2] ?? "https://chronoverify.com/static/og-default.png";
// new ChronoVerify("cv_live_...") for metered use; omitted runs the free public path.
const cv = new ChronoVerify();
const result = await cv.verify(arg.startsWith("http") ? { url: arg } : { file: arg });
console.log(`verdict: ${result.verdict}  confidence: ${result.confidence}/100`);
console.log(result.headline);
