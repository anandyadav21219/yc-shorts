# Playbook — how we make a Short

Reusable know-how collected while making posts, so each new Short starts here instead of
re-researching. The channel look, colours, typography and YouTube metadata rules live in
[../NICHE.md](../NICHE.md). This folder covers the *how*. From 2026-11-20 every Short is an image
Short (stylized 3D images from ChatGPT, one per phrase); the first one is
[../posts/fan-regulator/](../posts/fan-regulator/).

| File | Read it when |
|------|--------------|
| [image-shorts.md](image-shorts.md) | Making the Short: one prompt file per image, the shared style block, hero images for consistency, image checks, and putting the video together |
| [threejs-video.md](threejs-video.md) | History only: the Three.js code pipeline used 18–19 Nov 2026 (retired 2026-11-20) |
| [story-formula.md](story-formula.md) | Writing the script: story arc, hooks, twist + loop, Hindi VO word budget for the ElevenLabs voice |
| [post-template.md](post-template.md) | Starting a new `posts/<slug>/README.md`: copy it and fill it in |
| [thumbnail.md](thumbnail.md) | Making the thumbnail / Instagram cover in ChatGPT: the context-prompt template, Devanagari headline, checks, safe zones |
| [camera-journey-format.md](camera-journey-format.md) | Planning a "you build it" story told through one continuous camera journey |

## New post, start to finish
1. **Pick the idea.** Exclude everything in [../SUGGESTED_IDEAS.md](../SUGGESTED_IDEAS.md), then add the new one there.
2. **Research the mechanism** with the method below (2–3 searches are enough) and write the fact
   sheet, with its simplifications, into the post README.
3. **Write the story** with [story-formula.md](story-formula.md): one short Hindi line per beat,
   each inside the word budget.
4. **Start the post folder** `posts/<slug>/` and fill in the README from [post-template.md](post-template.md):
   fact sheet, final script, and the image list (one image per phrase).
5. **Write one prompt file per image** in `prompts/` ([image-shorts.md](image-shorts.md)), heroes first.
6. **Make the images in ChatGPT**, in order in one chat, attaching the hero each prompt names. Check each
   one and save it as `images/NN-<name>.png`.
7. **Voice and edit:** Anand sends the ElevenLabs take (`audio/vo.mp3`); cut the images to its pauses, add
   the hook title and captions, and write `<slug>.mp4` ([image-shorts.md](image-shorts.md) → *Putting the
   video together*).
8. **Thumbnail:** fill the context-prompt template in [thumbnail.md](thumbnail.md), save it as
   `posts/<slug>/thumbnail-prompt.md`, make it in ChatGPT and save it as `posts/<slug>/images/thumbnail.png`.
9. **Upload:** fill `posts/<slug>/youtube.md` using NICHE.md → *YouTube metadata & titles*, then
   move the idea to *Published* in SUGGESTED_IDEAS.md and add a row to [../PUBLISHED.md](../PUBLISHED.md)
   (link, title used, thumbnail). Fill in its stats at 24 h, 7 d and 28 d.

## Researching a mechanism (cheap and reliable)
- **Go straight to patents.** "How does <object> work" searches mostly return Google Patents
  pages anyway, and teardowns or forums rarely show up. A patent's *Background* section
  describes the common design and its variants, so 2–3 patents are enough. For natural processes
  (rain, rust, tides), use a science agency or textbook source (USGS, NOAA, NASA, IMD).
- **Note where designs differ.** Brands put the same part in different places (for example, an
  auto umbrella's opening spring can sit inside the stick, between two sliders, or under the
  top). Show one real, common layout. Simplify, but never invent parts.
- **Write down what you simplify.** The video can't show everything. List what it leaves out, so
  the simplification is a choice and not a mistake.
- **Fact-check the twist hardest.** It becomes the title and the line people quote.
- **Write it down once.** Put a one-line *Mechanism check* and the source links at the bottom of
  the post README. Anything that applies beyond one object goes into this playbook instead.
- **Standard web search is enough.** Use extended search only when standard results are thin.
