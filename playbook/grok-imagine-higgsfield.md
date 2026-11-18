# Video clips — Higgsfield · Grok Imagine

How we make every clip, picture **and** Hindi voice, in Higgsfield. No ChatGPT stills, no
separate voiceover tool (workflow changed 2026-11-17). Tool facts are dated because models
change: re-check the Higgsfield UI if something here looks off, and log what you learn in
*Run notes*.

## What the tool offers
Source: Higgsfield's Grok Imagine page (marketing copy), checked 2026-11-17.

| | |
|---|---|
| Clip length | "typically 6–15 seconds" per generation |
| Aspect ratios | 16:9, **9:16**, 1:1 "and more" |
| Resolution / fps | up to 1080p · 24 fps |
| Inputs | text-to-video and image-to-video (upload a reference image). End frame: not stated |
| Audio | generates video **and** audio "in a single pass": voice, SFX, ambience. No documented off switch |
| Camera | natural-language direction — "dolly zooms or pans", focus shifts, lighting changes |
| Speed | ~5–20 s for a standard clip |
| **Prompt length** | **max 4,096 characters**, spaces and line breaks included. A longer prompt is refused with "Prompt is too long (max 4096 characters)" (seen in the UI 2026-11-17) |
| Credits | not listed on the page — note the real cost under *Run notes* |
| Variants | the page names no "Lite" or version number. Other hosts list Grok Imagine Video 1.0 (≤10 s) and 1.5 (longer clips) with conflicting numbers — trust the Higgsfield UI |
| Hindi speech | **not documented** for Grok Imagine's native audio. Test it on the first clip. Other native-audio models on Higgsfield to try if Hindi comes out poor: Seedance 2.0, Kling 3.0, MiniMax Hailuo 3.0 (help-center list, checked 2026-11-17) |

## How we use it
- **Text-to-video, one clip per VO line.** Each clip's prompt carries its picture *and* the Hindi
  line the narrator speaks over it. The clip is the finished shot, with its sound.
- **Same object block in every prompt.** Without a start image the model re-invents the object
  each clip, so shape and colour drift. Paste the post's *object block* (object, materials,
  colours, background, style) **word for word** into every clip, and change only the scene,
  the motion and the camera.
- **Same voice block in every prompt.** Each clip is a separate generation, so the narrator's
  voice can change between clips. Paste the post's *voice block* word for word every time.
- **No text in the clips; captions go on in CapCut** (changed 2026-11-17; before that we
  planned to generate captions in-clip). End every prompt with the *no-text line* below. A clip
  with a voice may come out with its own subtitles, so the line names captions and subtitles
  explicitly. Never keep a take with text in it. CapCut gives exact Devanagari spelling
  and timing, and keeps every clip's first and last frames clean for start images and the loop.
- **Clip 1 is the baseline.** Make it first and get it right. If later clips drift from it, take a
  frame from clip 1 (export a frame in CapCut) and use it as the start image for that clip
  (image-to-video). That frame comes from our own clip, so there's still no separate image step.
- **One motion per clip.** If a beat needs two steps (fibres pull out *and* roll into a ball),
  split it into two clips, and split the VO line with it.
- **Cinematic camera, impossible viewpoints** (from 2026-11-17). After the establishing shot, film
  every macro as if the camera has shrunk to the part's scale: gliding low along it, looking up
  at it like something huge, slipping through gaps, or looking straight down its length. Add
  shallow depth of field and a soft rim light (natural light, never a glow effect). It's still
  one slow, smooth camera move per clip: the surprise comes from *where* the camera is, not from
  fast moves or VFX presets. End the move framed on the thing the next clip starts with.
  When the beat is a force (rubbing, pressing), put the camera *inside* the contact, such as the
  gap between two surfaces, lock it off and let the part move past it, like a truck rolling
  over a camera on the road. *(Idea, first tried on sweater-pilling clip 3. Log whether it
  worked.)* Give every clip a new viewpoint, so each cut feels fresh: for example wide → low
  glide → inside the contact → straight down from above → low side → wide. Something winding or
  spiralling reads best from straight above.
- **Fit the line to the clip.** Generate the shortest length the UI offers (~6 s). The VO line must
  fit inside it with a little air: **~12 Hindi words at most** (see
  [story-formula.md](story-formula.md)). A longer line (usually the twist) gets the next length
  up, not a faster read. Trim the clip's head and tail to the spoken line, never through a word.
- **2–3 takes per clip; spend the extra takes on the money shot.** A take is good only if the
  picture **and** the voice are right. If parts warp, make the object motion smaller and let the
  camera do more.
- **Listen to every take.** Wrong pronunciation, a different-sounding narrator, invented extra
  words, music or a second voice → regenerate. Native audio can't be fixed separately from the
  picture.
- **Cutaways "heal"** back into a solid object when there's big internal motion — keep it small
  and move the camera slowly.
- **Reversing a clip that has a voice:** in CapCut, *Extract audio* first, then reverse only the
  video, so the narrator still plays forwards. Prompt reversed clips for voice only (no SFX), and
  add any SFX in CapCut, because a native SFX won't land on the reversed motion. Don't put
  directional arrows in a clip you plan to reverse — they'd point the wrong way. Time that
  clip's caption to the extracted (forward) voice, not to the picture. Judge a reversed take
  only after reversing it. Because the voice is a separate track by then, slide it so the payoff
  word lands on the frame where the motion completes, and put the SFX on that frame too. If the
  model ignores the prompt and plays the motion forwards cleanly, keep that take and don't
  reverse it.
- **Money shot where something forms** (a ball rolls up, parts assemble): prompt it coming apart,
  then reverse it as above. The model handles undoing better than assembling. *(Idea, first
  tried on sweater-pilling clip 5 — log whether it worked in Run notes.)*
- **Loop:** the last frame should be clip 1's first frame. Make the last clip as image-to-video
  from clip 1's first frame, with clip 1's push-in and the last VO line. Then extract the audio and
  reverse the video. It pulls back and ends on that exact frame. Give the last clip **no new
  angle**: it's the trip home and mirrors clip 1 like a bookend, which is what hides the join.
  For the freeze, use the exported still of clip 1's first frame, not the reversed clip's last
  frame, so the loop frame is exactly the image the video opens on. Test the loop by watching the
  last 2 seconds run into the first 2. If the start image has a mannequin or floating fix, the
  last clip's scene text must use the same one.
- **Clean start and end.** Ask for a still, sharp first half-second, and for the camera to stop and
  hold for the last second. The clip then trims cleanly, cuts into the next clip without a
  mid-move jump, and its first and last frames work as start images for later clips and the loop.
  *(Idea, first tried on sweater-pilling clip 1 — log whether the model obeys it.)*
- **Every prompt ≤ 3,800 characters** (the hard limit is 4,096). That leaves room to add a fix
  sentence on a retake without going over. The fixed parts (opening line, object block,
  constraint line, voice block, VO line and no-text line) take about 1,500–1,600 characters, so
  Scene + Action + Camera + Sound effects get **about 2,200 together**. Every Devanagari letter
  and vowel sign counts as a character. To trim:
  - say each thing once (don't repeat the gradient colours or "perfectly still" in three places);
  - cut adjectives the object block already gives;
  - keep the "why" and comparisons in the README's look notes, not in the prompt.
  - Never trim the object or voice blocks: they must stay word for word.
  Check before pasting: copy the prompt, then run `pbpaste | wc -m` in Terminal. Each post README
  states every prompt's character count.
- **Prompt-enhance off.** If the UI offers to enhance or rewrite the prompt, turn it off, so the
  locked object and voice blocks reach the model word for word.
- **Avoid action/VFX presets** (shake, explode, bullet-time) — they break the clean educational look.
- **Keep comparisons that name another object out of the prompt** ("like a hot-air balloon", "like
  a truck"). The model may draw that object. Put the comparison in the post README's look notes
  for yourself, and describe only the motion and materials in the prompt. *(Caution, not yet
  tested. Sweater-pilling clip 5 is the first prompt written this way.)*
- **Fallbacks:**
  - If a clip won't behave after 3 takes, make it image-to-video from a good frame of an
    earlier clip, with a slow camera move only.
  - If the Hindi comes out wrong, try one take with the VO line written in Roman letters
    (`The narrator says, in Hindi (written here in Roman letters): "..."`) before switching model.
  - If the narrator still sounds different from clip to clip, or the Hindi keeps coming out
    wrong, record the whole script once in Higgsfield's own voice-over tool, mute the clips and
    cut the video to that take. Log it in *Run notes* so we know whether native voice is usable.

## Clip prompt template
Starting point — refine it after real runs. The filled-in prompt must stay **≤ 3,800 characters**
(Higgsfield's hard limit is 4,096). `[OBJECT BLOCK]` comes from the post README;
`[VOICE BLOCK]` is the channel default below. Both blocks and the last line (the no-text line)
stay identical in every clip.

```text
Vertical 9:16 premium 3D CGI educational animation, made by a skilled 3D motion-graphics
studio, not live action and not generic AI art. One continuous shot with no cuts. [OBJECT BLOCK]
Scene: [WHAT WE SEE — framing, which part, cutaway or not].
Action: [ONE ACTION — e.g. "the tiny fibre ends slowly pull out of the yarn and fluff up into
a soft fuzzy layer"].
Camera: the first half-second is perfectly still and sharp. Then [slow push-in / slow dolly
left / gentle orbit / locked off]. The camera then holds the final frame perfectly still
until the end of the clip.
Keep the object's shape, materials and colours consistent; no new objects, no hands unless
stated, no people. Smooth, physically plausible motion.
Audio: [VOICE BLOCK] The narrator says, in Hindi: "[VO LINE, in Devanagari]" The narrator
starts about half a second into the clip, speaks this line exactly once, then stays silent
until the end.
Sound effects: [e.g. crisp plastic click, then a soft fabric whoosh / none]. No music, no
other voices, no extra words.
No text anywhere in the frame: no captions, no subtitles, no letters, numbers, labels, logos
or watermarks.
```

**Voice block (channel default, paste as-is unless the post says otherwise):**

```text
One off-screen narrator: a warm, friendly adult male voice speaking clear, natural,
conversational Hindi with a neutral Indian accent, at a calm medium pace, like explaining
something to a friend. The same narrator voice in every clip.
```

**Captions:** none in the prompt. They're added in CapCut in the channel style
([../NICHE.md](../NICHE.md) → *Narration captions*).

## Run notes
Add a line after each session so the next post starts smarter.

| Date | Post / clip | Setting (model, length, res) | What worked | What failed | Credits |
|------|-------------|------------------------------|-------------|-------------|---------|
| 2026-11-17 | sweater-pilling clip 5 (first draft) | Grok Imagine, text-to-video | — | Refused before generating: "Prompt is too long (max 4096 characters)". The draft was 4,196; cut to 3,555 without touching the fixed blocks | none (refused) |
| 2026-11-17 | second post, tested in both tools | Higgsfield vs Google Flow, same prompts | Both outputs acceptable, though they look different. The same prompt style works in both | — | — |
| 2026-11-17 | ghat-road test clip (camera-journey format) | Google Flow, text-to-video, 8 s, photoreal, Hindi narration in-clip, 5,241-char second-by-second prompt | — | No usable output: the user called it "not acceptable at all". What exactly went wrong wasn't recorded. Retrying in Higgsfield in clean stylized 3D | — |
| 2026-11-17 | stuck-steel-glasses (plan; post dropped the same day) | Google Flow clips + separate ElevenLabs VO (30.85 s) | Voice first, then scenes cut at the measured pauses: 6 scenes of 4–6 s. Clips have no narration | — | — |

## Sources
- [Higgsfield — Grok Imagine](https://higgsfield.ai/grok-imagine) (checked 2026-11-17)
- [Higgsfield help — lipsync, voiceover and aspect ratios](https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-use-lipsync-voiceover-and-aspect-ratios) — native-audio model list (checked 2026-11-17)
- [Higgsfield — AI voice-over](https://higgsfield.ai/ai-voice-over) — the voice-over fallback; Hindi listed (checked 2026-11-17)
- Version/length claims from other hosts, unverified: [fal.ai — Grok Imagine Video 1.5](https://fal.ai/models/xai/grok-imagine-video/v1.5/image-to-video), [Build Fast with AI review](https://www.buildfastwithai.com/blogs/grok-imagine-video-1-5-review-2026)
