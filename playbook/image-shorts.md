# Image Shorts — stylized 3D stills from ChatGPT

From 2026-11-20 every Short is an **image Short**: one stylized 3D image per spoken phrase, made in
ChatGPT from a paste-ready prompt, then put together on this Mac with a slow move on each image, the
ElevenLabs Hindi voice and burnt-in captions. The Three.js code pipeline is retired
([threejs-video.md](threejs-video.md) is kept only as history; its template post was deleted on
2026-11-20). First image Short: [../posts/fan-regulator/](../posts/fan-regulator/).

## Post folder
```
posts/<slug>/
  README.md          fact sheet, final script, image list (from post-template.md)
  prompts/NN-*.md    one paste-ready ChatGPT prompt per image
  images/NN-*.png    the approved images
  audio/vo.mp3       the ElevenLabs take (from Anand)
  <slug>.mp4         the finished Short
  thumbnail-prompt.md, youtube.md, instagram.md
```
When a post is published, everything except the MP4, the thumbnail, `thumbnail-prompt.md`,
`youtube.md` and `instagram.md` can be cleared out (Anand's call, 2026-11-20).

## From idea to images
1. **Fact sheet first** (mechanism method in [README.md](README.md)). Accuracy still comes first: every
   part in an image must be a real part of the common design.
2. **Final script** with [story-formula.md](story-formula.md): one short Hindi line per beat, split at
   `…` into phrases.
3. **One image per phrase.** Every phrase gets its own literal picture of what is being said. That is
   usually 12–16 images for 30–35 s, about 2–3 s each. The last frame reuses image 01 for the loop.
4. **Pick the heroes.** Each object that comes back (the fan, the old regulator, the new one) gets a
   hero image made first. Every later prompt that shows it names that hero as its reference.
5. **Write one prompt file per image** in `prompts/` (format below). Each prompt is complete on its own,
   so it can be pasted without the others.

## Prompt file format
```markdown
# NN · <beat> — <short name>
**Voice:** <the exact Hindi phrase>
**On screen:** ~N s · **Motion in the edit:** <slow push-in / pan / pull back>
**Reference:** none (hero) | attach images/NN-*.png and say: same <object> as this image.
**Save as:** `images/NN-<name>.png`

## Prompt (paste into ChatGPT)
<subject paragraph> + the shared style block below

## Check before saving
- <what must be true for this image>
```

## Shared style block (end every prompt with it)
> Style: a premium, art-directed stylized 3D CGI render, the kind a top motion-graphics studio makes for
> an educational explainer. Believable geometry, clean modelling and convincing materials, but clearly a
> polished 3D render: not a photograph, not a cartoon, not generic AI art.
> Background: a smooth studio gradient in [soft peach / coral pink / mint / cream]. No room, no wall, no
> ceiling, no props or decoration. The subject floats cleanly against the gradient.
> Lighting: soft professional studio light, a soft rim light, controlled reflections, subtle contact
> shadows, gentle shallow depth of field.
> Colours: harmonious and soft. No neon, no glowing rings, no glowing anything, no dark-blue/purple neon
> palette, no oversaturation.
> Composition: vertical 9:16 for a phone. The main subject large and centred, inside the central
> two-thirds of the width. Keep the top quarter and the bottom fifth calm, empty background.
> No text, letters, numbers, labels, logos or watermarks anywhere in the image.

## Making the images in ChatGPT
- **One chat per post, images in order.** Heroes first. Attach the named reference image to each
  prompt so the object keeps its shape and materials.
- **Images carry no text.** The hook title and captions are added in the edit, so ChatGPT never has to
  spell Hindi.
- **ChatGPT gives 2:3 portrait (1024×1536).** The edit scales it to fill 1080×1920 and trims the sides, so
  nothing important may sit in the outer sixth of the width.
- **Check every image** against its file's *Check before saving* list, plus: same object as the hero, no
  glow, no text, no invented parts. Fix in the same chat, one change at a time ("Keep everything the same
  but make the out-arrow thinner").
- **Colour code:** energy/electricity = matte golden-yellow arrows; force/pressure = matte coral arrows;
  air/flow = mint; heat = soft translucent warm haze with small coral wavy arrows; steam = soft white.
- **Name only the arrows this image shows** (checked 2026-11-20, rickshaw-horn). Pasting the whole colour
  legend into a prompt makes ChatGPT draw every arrow it lists. Say what the image has and add "No arrows" or
  "No sound rings" for the rest.
- **Run several chats at once** (checked 2026-11-20). After the heroes exist, open 4–5 ChatGPT tabs, each a
  new chat with its prompt and its hero attached. Five images came back in about a minute instead of five.
  Consistency held because each prompt attaches the hero file itself.
- **Street opening shots** (rickshaw-horn, Anand's call): a colourful stylized 3D Indian street with no people
  for the hook and the twist, and gradients for the close-ups. It worked well with the hero attached.

## Putting the video together
- **Motion:** one slow, smooth move per image (push-in, pan or pull back, about 5–8 % over the shot).
  No shakes, spins or flashy transitions; straight cuts at the voice pauses.
- **Timing:** cut at the pauses of the ElevenLabs take. Until the voice arrives, cut to the estimated
  seconds in the README.
- **Text:** the hook title in the upper third for the first ~3 s, then one caption at a time (NICHE.md →
  *Narration captions*, *One text at a time*). Captions come from the script's exact Devanagari.
- **Output:** 1080×1920, 30 fps, H.264 MP4 named `<slug>.mp4`.

### The build script (checked 2026-11-20)
Copy `posts/fan-regulator/build/` into the new post. `build.py` holds the shot list (image, phrase start and
end in the take, motion, caption). It moves each image with sub-pixel PIL transforms, burns in the captions,
pipes the frames to ffmpeg (libx264 + AAC) and ends on image 01 for the loop. `python3 build/build.py --stills`
writes one still per shot to `build/stills/` for review first.
- **Captions need CoreText.** Homebrew ffmpeg (9.0.2) has no text shaping in `drawtext`, so Devanagari
  conjuncts break there. `caption.swift` (compile once: `swiftc -O caption.swift -o caption`) renders each
  phrase in Kohinoor Devanagari Bold to a PNG, shrinking it to fit 950 px.
- **Measure the take:** `ffmpeg -i audio/vo.mp3 -af silencedetect=noise=-38dB:d=0.12 -f null -` lists the
  pauses. On fan-regulator they split the take into exactly the 14 phrases.
- **Hook title:** when the voice starts at 0 s a caption is always on screen, so the hook title is left out
  (one text at a time) and the thumbnail carries it.

### ChatGPT in Chrome (what worked on 2026-11-20)
- Typing: put the prompt into the composer with `document.execCommand('insertText')` on the ProseMirror box,
  then click the button whose aria-label is `Send`.
- ChatGPT sometimes returns two versions ("Which image do you like more?"). Pick the more accurate one.
- Saving: Chrome only allows repeated downloads from a real click. A page button that fetches the image blob
  and downloads it, clicked through the browser tool, works. The page's CSP blocks posting to localhost.
- For a reference that isn't the image just above, attach it with the "Attach photos" file input. For the
  image just above, saying "from the image just above" is enough.
