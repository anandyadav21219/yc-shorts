> **Retired 2026-11-20.** Shorts are now image Shorts: see [image-shorts.md](image-shorts.md). The template post
> `posts/how-rain-works/` code was deleted the same day, so the commands below no longer run. Kept as history.

# Video in code — Three.js

Every Short is made in code on this Mac: Three.js 3D scenes rendered frame by frame, Hindi narration
from an **ElevenLabs** voice (a voice-only MP3 Anand makes from the script), sound effects and music synthesised in Node, and an AVFoundation
encoder that writes the MP4. No AI video tools, no CapCut (changed 2026-11-18). The thumbnail is
made in ChatGPT from a context prompt ([thumbnail.md](thumbnail.md), changed 2026-11-19). Because we build the world ourselves, every part,
motion and force can be made exactly right. Accuracy is the reason for working this way.

**Template post:** [../posts/how-rain-works/](../posts/how-rain-works/). Copy it to start a new Short.

## Toolchain (checked 2026-11-18, M1 Mac)
| Piece | What we use |
|---|---|
| 3D | `three` 0.170 (in each post's `node_modules`), ES modules via an import map in `scene.html` |
| Frames | installed Google Chrome, headless, driven by `puppeteer-core`. WebGL runs on the GPU (ANGLE Metal). 600 frames (20 s) take about 35 s |
| Voice | One ElevenLabs take of the whole script, voice only, saved as `audio/vo-elevenlabs.mp3`; `npm run vo` converts it with `afconvert` to 48 kHz mono `audio/vo1.wav`. (`say -v Lekha -r 205`, the only hi_IN voice installed, was used until 2026-11-18 and sounded poor) |
| Sound | `audio.mjs`: plain Node, no packages. Noise, filters and sine synths for SFX, plus a soft pad/pluck music bed |
| Encode | `encode.swift` (AVFoundation): JPEG frames + WAV → H.264/AAC MP4, 1080×1920, 30 fps. There's **no ffmpeg, Blender or sox** on this Mac |
| Timing | `measure.mjs`: speech length and pauses (≥ 120 ms by default; `node measure.mjs audio 180` for longer) of each `audio/vo*.wav` |
| Review | `sheet.swift`: pulls frames out of the MP4 into one contact sheet. `node render.mjs <dir> t1,t2` renders single moments |
| Fonts | Kohinoor Devanagari Bold (captions, hook title), Arial Rounded MT Bold (thumbnail text). Both are installed |
| Full build | `npm run build` (voice → audio → frames → encode → thumbnail): about 1.5 min for 20 s |

## Start a new post
```bash
rsync -a --exclude frames --exclude stills --exclude '*.mp4' --exclude 'audio/*.wav' --exclude 'audio/*.mp3' --exclude images posts/how-rain-works/ posts/<slug>/
```
Then rename the MP4 name in `package.json` (`encode` and `check` scripts) and replace the content of
`timeline.js`, `vo.sh`, `scene.js` and the README. Keep `render.mjs`, `encode.swift`, `sheet.swift`
and the structure of `audio.mjs`. `node_modules` comes along, so no download is needed.

| File | Role |
|---|---|
| `timeline.js` | **The single source of truth.** Voice cues and phrase timings, shot list, event times (merges, pops), thumbnail settings. The scene and the audio both import it, so picture and sound can't drift apart |
| `vo.sh` | The Hindi lines, one per beat |
| `scene.html` | Canvas plus the text overlay (hook title, captions, thumbnail text) |
| `scene.js` | The scenes, the per-shot cameras and `window.renderAt(t)` |
| `audio.mjs` | Voice placement, SFX layers levelled to target loudness, music ducked under the voice |
| `render.mjs` | Frames, stills, or `thumbnail` → `images/thumbnail.png` |

## Order of work
1. **Research the mechanism** ([README.md](README.md) → *Researching a mechanism*) and write a short
   **fact sheet** in the post README: the cause → effect chain, the real parts, the real directions of
   force and flow, real proportions, and which simplifications you'll make. The scene is built from
   this list, so research comes first.
2. **Write the script** with [story-formula.md](story-formula.md): one line per beat, ≤ 12 words,
   Hinglish rule (Hindi sentences, English only for everyday words).
3. **Get the voice first:** give Anand the Devanagari script (one line per beat, `…` at each cut).
   Anand makes one ElevenLabs take, voice only, and sends the MP3. Save it as
   `audio/vo-elevenlabs.mp3`, then `npm run vo`.
4. **Measure the take and its pauses:** `npm run measure` prints the speech length and every pause
   ≥ 120 ms. Match the pauses to the script's phrases (a syllable count settles doubtful ones; short
   ~0.15 s dips inside a phrase are not cuts). Write the phrase timings into `timeline.js → VO`.
5. **Cut the shots to the voice:** one shot per phrase in `timeline.js → SHOTS`, each cut ~0.1 s before
   its phrase starts.
6. **Build the scene, checking stills as you go:** `node render.mjs stills <mid-time of every shot>`,
   then tile them and look at the whole run at once. Fix framing before rendering the whole video.
7. **Sound:** put every SFX on its event time from `timeline.js`, then `npm run audio`.
8. **Full build and review:** `npm run build`, then `npm run check` (contact sheet of every shot
   from the finished MP4). Go through the *Review checklist* below.
9. **Thumbnail:** write `thumbnail-prompt.md` from the template in [thumbnail.md](thumbnail.md) and
   make it in ChatGPT. Fallback: set `THUMB` in `timeline.js`, then `npm run thumbnail`.

## Accuracy rules
- **Show only what the fact sheet says.** Every part, motion and arrow in the scene traces back to a
  line in the post's *Mechanism check*. Simplify shapes, but never invent parts or steps.
- **Directions are facts.** Forces and flows point the real way (air pushes up, weight pulls down,
  vapour rises). Coral = force, weight or pressure; mint = air or flow.
- **Sizes that are compared must compare truly.** If two arrows are compared, their lengths follow
  the real quantities. In the rain post the weight arrow grows with the drop's mass (r³), while the
  air arrows stay fixed.
- **Use real physics when it's cheap:** volume is conserved when drops merge (r = ∛(Σr³)), falling
  speeds up as ½gt², waves move continuously. It looks right because it is right.
- **Exaggerate scale only on purpose, and say so.** Cloud droplets can't be shown at true size, so
  enlarge them, but keep the order right (cloud droplet < raindrop) and note it in the README.
- **Name what you leave out.** The README's *Mechanism check* lists the simplifications (rain: "leaves
  out ice-crystal rain"). The twist gets a source link, because it becomes the title.
- **Timing is part of accuracy.** Shots cut on the measured pauses, and each sound lands on the exact
  frame of its event, because both read `timeline.js`.
- **Captions are the script's exact Devanagari,** split at the same pauses as the voice.

## Scene craft (what worked on the rain post)
- **`renderAt(t)` is a pure function of time.** No state carried between frames, so a still at any
  time matches the frame in the video, and any moment can be checked without a full render.
- **One world, one macro scene.** A floating cut-away diorama (half sea, half land, sliced open to
  show soil and water depth) keeps the object identical in every wide shot. A second scene holds the
  close-ups at droplet scale. Cut between them on a phrase.
- **One shot per phrase, one smooth camera move per shot,** eased (55% ease + 45% linear) so it never
  stops dead. Pull-backs use ease-out. Viewpoints nobody gets with their own eyes: inside the cloud,
  at droplet scale, right on the sea surface.
- **Frame for 9:16 with numbers, not guesses.** Visible width = 2 · distance · tan(fov/2) · 0.5625.
  An object 6.8 wide needs about 24 units of distance at fov 34°. Keep the subject between ~300 and
  ~1100 px from the top, so it clears the hook title and the captions.
- **Materials:** water drops are `MeshPhysicalMaterial` with transmission 1, ior 1.33 and an
  attenuation colour (without the attenuation they read as soap bubbles). Sea: physical, transparent,
  clearcoat, with a live vertex-wave surface. Clouds: white puffs over a flat base, turned grey when it
  rains. No bloom, no neon, no glowing rings.
- **Background:** a vertical studio gradient drawn on a canvas with ±1 noise dither (no banding), one
  palette per shot from NICHE.md.
- **Particles** (vapour): `Points` with a small shader for soft round sprites, using
  `#include <colorspace_fragment>` so the colours match the rest of the scene.
- **Literal pictures:** "ठंड" → a thermometer dropping from coral to blue. "भारी" → a weight arrow
  growing. "हवा थाम नहीं पाती" → air arrows that stay short while the drop falls past them.

## Voice, captions, sound
- **ElevenLabs pace (measured 2026-11-18, "Morgan"):** ≈ 3.0 words/s while speaking, ≈ 2.3 words/s
  over the whole video. Budget the script with [story-formula.md](story-formula.md).
- **A new voice take after the picture is built:** don't move every time in `scene.js` by hand.
  `timeline.js` keeps two clocks: *scene time* (the clock the picture was built on: SHOTS, EVENTS,
  MERGES, times inside `scene.js`) and *video time* (the voice and captions). `sceneTime()` stretches
  each shot to fit between its new cuts, so speed only changes at a cut; `audio.mjs` moves the SFX
  with `videoTime()`. Waves, rain streaks and background drops run on video time so they keep their
  real speed. Used on how-rain-works when the Lekha voice was replaced.
- `audio.mjs` stops if two lines overlap or the voice runs too close to the end, and warns when a
  line's length no longer matches `timeline.js`.
- **Captions and hook title are rendered in the overlay** (NICHE.md → *Narration captions*, *Hindi
  typography*). For a text-free version, empty `#hook` and `#cap` in `scene.html`.
- **Levels that worked:** voice ≈ −17 dB RMS while speaking; effects and music ≈ −31 to −40 dB in the
  gaps; music ducked a further ~45% under the voice; effects ~30% under it.

## Review checklist (before showing anyone)
- [ ] `npm run check`: every shot shows what its phrase says, and nothing important is cut off at
      the edges.
- [ ] Captions are readable on every background, and none sits on top of the key detail.
- [ ] Every arrow points the true way. Compared sizes are true.
- [ ] The MP4 is 1080×1920, 30 fps, exactly the planned length (`afinfo <file>.mp4`).
- [ ] Listen once end to end: every word is clear, the SFX land on their events, the music never
      covers the voice.
- [ ] The *Mechanism check* in the README matches what the video shows, simplifications included.

## The prompt (paste into Claude Code to make a new Short)
```text
Make a new Why Bhai Short in code about: [TOPIC, e.g. "how a ceiling fan regulator changes speed"].
Length: [NN] seconds, 9:16, Hindi narration.

Follow CLAUDE.md, NICHE.md, playbook/story-formula.md and playbook/threejs-video.md, and copy
posts/how-rain-works as the starting point (posts/[slug]/).

1. Research the mechanism first (2–3 searches, patents for objects) and write the fact sheet and
   simplifications into the README before any scene code. Check the topic against SUGGESTED_IDEAS.md.
2. Script: story formula, 5–7 lines of ≤ 12 Hinglish words, a true fact-checked twist.
3. Give me the Devanagari script to make in ElevenLabs; when the voice-only MP3 is in
   audio/vo-elevenlabs.mp3, measure every pause, then cut one shot per phrase in timeline.js.
4. Build the 3D scenes from the fact sheet only: real parts, real directions, real proportions
   (say where scale is exaggerated). Use the channel palette, coral force arrows, no neon.
5. Check stills of every shot before the full render. Fix framing, edges and caption overlap.
6. Sound effects on the exact event times, voice clearly on top.
7. Full build, contact-sheet review, thumbnail-prompt.md for ChatGPT (thumbnail.md template), README with the mechanism
   check and sources. Log the run in playbook/threejs-video.md → Run notes.
Make the creative calls yourself; ask only if the topic itself is unclear.
```

## Run notes
Add a line after each build so the next post starts smarter.

| Date | Post | What worked | What to fix next time |
|------|------|-------------|-----------------------|
| 2026-11-18 | experiments/morning-stretch (English test, 10 s) | Whole pipeline (Three.js → headless Chrome → `say` → AVFoundation) in about 30 s | Mannequin joint seams on the character; Samantha voice is synthetic |
| 2026-11-18 | posts/how-rain-works (20 s, Hindi) | Voice-first timing, shared `timeline.js`, island diorama + macro scene, transmissive drops with attenuation, tear → bun morph, thumbnail from the same scene | First stills: the island was cropped (camera too close for 9:16), droplets looked like grey marbles, drops looked like soap bubbles until attenuation was added, arrows and the pav ran off-frame. All fixed in two still passes |
| 2026-11-18 | posts/how-rain-works, voice swap (25.6 s) | Replaced Lekha with Anand's ElevenLabs take (Morgan) without touching the scene code's times: two clocks in `timeline.js`, each shot stretched 1.03–1.67× to its new cut, SFX moved with `videoTime()`; re-render + encode ≈ 1 min | The take was 24.5 s against Lekha's 17.5 s, so the video grew from 20 s to 25.6 s. Budget ~2.3 words/s for ElevenLabs before writing the script |
| 2026-11-18 | posts/phone-flip-cover (29.4 s, Hindi) | Built on the voice take from the start (scene time = video time, 16 shots). Ghost (see-through) cutaways, a camera that zooms from phone to a 1.2 mm chip in one scene, Hall plate with instanced electrons | Changing `material.transparent` at run time needs `material.needsUpdate = true` (OPAQUE shader define), else ghosting silently fails. First camera passes were ~35% too close: open book 15 cm wide needs d ≈ 55 at fov 34 |
| 2026-11-18 | experiments/floating-island (6 s loop, 1080², not a Short) | Pure `renderAt(t)` with a 6 s turntable and integer-cycle waterfall and cloud motion: the seam matched in the frame diffs. 4K still by re-rendering at SIZE=3840 | Blender is not on this Mac; Three.js did the job. Waterfall reads best as a stream of drops arcing off the rim, not a hugging sheet (the sheet looked like a crack) |
| 2026-11-18 | posts/photochromic-glasses (36.4 s, Hindi, temp guide voice) | Realistic, colourful world instead of studio gradients: own sky shader into a cube map (`Sky.js` came out washed-out white), real leaf-card trees whose shadow maps give true dappled shade, BokehPass depth of field, procedural canvas textures (asphalt, grass, bark, bandhani). A full-face helmet with the eye port cut out of a deformed sphere reads as real, while a modelled face looked like a cartoon. Road repeats every 145.6 m (wheel turns, kerbs, dashes, texture tiles all divide it) so the last frame matches the first | Shade needs the canopy above the rider's *head*, not just the ground (move trees toward the road), and low fill (hemisphere ≈ 0.4, env ≈ 0.3). A dark transparent lens looks grey unless its env reflection drops with the tint. Car interiors in 9:16 need the camera at the driver's eye with the wheel in frame, or the shot doesn't read as a car. The rider's body (capsules) still looks toy-like in wide shots |
| 2026-11-19 | posts/how-wind-works (28 s, background sound only) | One world scene with colourful props (palms, houses, flag, sailboat), glossy instanced air bubbles, rainbow `TubeGeometry` wind ribbons with moving chevron alphaMap and `setDrawRange` to grow them, day→night in one shot. Built picture-first; voice slot ready via the two clocks | First stills: thermometers and gauges at ±1.6 fell off the 9:16 frame (keep side-by-side props within ±0.9 at ~9 units), a fully transparent stripe alphaMap made ribbons look like floating blocks (give gaps ~40% alpha) |
| 2026-11-19 | posts/cold-roti (34.2 s, Hindi, ElevenLabs Morgan) | Fresh project, not copied from how-rain-works. Objects built first and checked in an object sheet (`node render.mjs objects`) before any shot. Roti as one deformable polar mesh (puff, circular-hinge fold, crack along a wavy line), procedural phulka texture, studio sweep floor with vertex-colour gradients for colourful backgrounds, steam lives that divide the video length so the last frame matches the first (PSNR 47 dB). Full render ≈ 77 s for 1026 frames | Round, ringed brown spots read as bubbles: phulka spots need elongated clusters of soft blobs with no dark rim. A thin stove slab floats in the void: make the body ~8 cm tall and sit it on a speckled counter. Portrait frames are narrow (≈19° horizontal at fov 34), so stove shots need the camera ~7 units back. Starch threads still read as spaghetti |
| 2026-11-19 | posts/bartan-naam (39.7 s, Hindi, ElevenLabs Morgan) | Copied cold-roti's tools, new objects. Object sheet first (`node render.mjs objects`), fixed before shots. A per-world studio environment (PMREM of a sphere with grey walls, the sweep colour below, tall soft boxes and black flags) makes polished steel read silver; the name as real Devanagari dots (canvas text → Zhang–Suen thinning → evenly spaced centre-line dots, letters first, shirorekha last); box cutaway with a clipping plane; an `aim(P, dir, d, sy)` helper that puts the subject at a set screen height so it clears the caption band; coiled cord as a helix round a Catmull-Rom path; loop seam by turning the glass 180° (blank side back to camera) | Steel in a warm, uniform environment reads as orange plastic; too many hard strips read as a barcode; 4–5 strips plus 2–3 flags is right. `smoothstep(a, b, x)` with a > b is undefined in GLSL (glow vanished). BokehPass keeps `nearClip` from construction: update `bokeh.uniforms.nearClip/farClip` when `camera.near` changes, or it blurs fine detail away. InstancedMesh needs `frustumCulled = false` when its instances move or grow. Portrait frames are narrow (visible width ≈ 0.3 · distance at fov 30): a 15 cm box needs ~6 units. An svf click with q 0.15 rings hot; check the pre-clip peak |
