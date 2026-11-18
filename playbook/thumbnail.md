# Thumbnail — ChatGPT image prompt

How we make every post's thumbnail, which is also the Instagram/Facebook cover. It's made in ChatGPT's
image generation; the clips stay in Higgsfield. The channel look and safe zones come from
[../NICHE.md](../NICHE.md). First used on sweater pilling (2026-11-17); log what you learn at the bottom.

## Rules
- **Text in Hinglish, Roman capitals, not Devanagari** (from 2026-11-17). It matches the Hinglish titles and
  reaches viewers who don't read Devanagari, and image models spell Roman letters far more reliably.
- **Two lines, 6 words at most.** Mix Hindi and English the way people talk (`SWEATER KI GOLI` /
  `DIRT NAHI HAI!`).
- **The thumbnail and the title split the job.** The thumbnail carries the hook (the contradiction or the
  question); the title carries the twist. Never repeat the title's hook; the object's name ("Sweater Ki Goli")
  may appear in both, because it's the search word. Don't give the answer away on the thumbnail.
- **Show a moment, not a product shot.** Pick the frame from the story with tension in it (a pull that won't
  give, a part mid-action), so the picture itself asks the question. A still object sitting there gives no
  reason to click.
- **One subject, big and sharp,** about 35–45% of the width, in the video's own look (same object block
  colours). One matte coral arrow may point at the detail that tells the story. No other graphics.
- **The subject must contrast with what's behind it.** Put it against the warm gradient (a low angle helps),
  not against more of the same object. Don't put a blurred copy of the whole object behind it: it looms like a
  ghost and pushes the warm colours out of the frame.
- **Describe the subject's real look and say what it is not.** Give its exact colour and say "not moss, not a
  pompom", or whatever look-alike the model reaches for.
- **Readable on a light gradient.** Use a very heavy rounded sans (Montserrat ExtraBold, Poppins Black), white
  with a thin dark outline in the object's colour and a soft drop shadow. Make the gradient slightly deeper
  behind the text. Line 2 is a little larger.
- **Safe zones at 1080×1920:**
  - Text 280–640 px from the top (≈ 15–33%).
  - Nothing important in the top 12% or the bottom 23%, or along the right edge (Instagram's 3:4 grid crop
    and the Shorts/Reels buttons).
  - Keep everything inside the central 75% of the width, so a 2:3 image can be cropped to 9:16. Say "each
    line at most 75% of the image width" in the prompt, or the model runs the text nearly edge to edge.
- **Use a new ChatGPT chat for a new attempt,** so it doesn't copy the previous image. Make small fixes in the
  same chat, one at a time, ending with "change nothing else".
- **ChatGPT may only offer 2:3 portrait.** Place it on a 1080×1920 canvas in Canva or CapCut, fill the height
  and let the sides crop.
- **For a closer match to the video,** attach a still from the edit and put the reference line at the top of
  the prompt (template below).
- **Save it** as `posts/<slug>/images/thumbnail.png` and put the filled prompt in the post README → *Thumbnail*.

## Prompt template
Replace every `[…]`. Leave out the first line if you don't attach a reference still.

```text
Use the attached image as the reference for the [OBJECT]'s colours, materials and look, and keep that look exactly.

Create a vertical YouTube Shorts thumbnail in tall portrait format, ideally 9:16 (1080×1920). If 9:16 isn't available, use 2:3 portrait and keep every important element inside the central 75% of the width, so the sides can be cropped to 9:16.

Style: premium stylized-realistic 3D CGI, like a hero frame from a high-end 3D motion-graphics explainer. Believable materials, soft cinematic studio lighting, clearly a polished 3D render: not a photo, not a cartoon, not generic AI art. No neon, no glowing rings, no lens flares, no sparkles, no bloom.

The moment: [THE ONE MOMENT OF TENSION FROM THE STORY, in one sentence, and the camera viewpoint].

Hero: [THE ONE SUBJECT — what it is, its exact colour and materials, about 35–45% of the image width, centred horizontally, its centre about 55% of the way down; what it is NOT ("not moss, not a pompom"); plus the one detail that tells the story].

Background: behind the subject, only a smooth warm studio gradient in [PALETTE FROM THE POST], richer at the top, so the subject stands out strongly against it. No room, no props, no people, no hands.

Light: a warm light from behind the subject gives it and [THE DETAIL] a thin bright rim, with soft front fill. Rich, clean contrast. Shallow depth of field.

Graphic: one clean, smooth, matte soft-coral arrow curves down from just below the text and points at [THE DETAIL]. Flat matte colour, no glow, no outline.

Text: two lines of bold text, centred, in the upper part of the image, starting about 15% from the top edge and ending about a third of the way down. Spell it exactly, in capital Roman letters:
Line 1: "[LINE 1]"
Line 2: "[LINE 2]"
Use a very heavy, clean, rounded sans-serif font (like Montserrat ExtraBold or Poppins Black). White letters with a thick [DARK OBJECT COLOUR] outline and a soft dark drop shadow, so they read clearly on the light background. Line 2 is larger than line 1. Each line is at most 75% of the image width, with clear empty space on both sides. No other text, letters, numbers, logos or watermarks anywhere.

Layout: keep the top 12% and the bottom 23% of the image free of text and of the subject, and keep the right edge free of important details. It must read instantly at small phone-thumbnail size: one clear subject, big text, strong contrast.
```

## Checks and fixes
- **Spelling:** check every letter. If it's wrong, ask once: "Fix the text to read exactly … and change nothing
  else." If it's still wrong, ask for the same image with no text and add the text in Canva or CapCut, in the
  same style and position.
- **Small-size test:** shrink it to about 3 cm wide on the phone. The text and the subject must still read at a
  glance.
- **Looks like a photo:** add "Clearly a stylized 3D render, not a photograph."
- **Glow or sparkles:** add "No glow, no bloom, no sparkle effects."

## Notes
| Date | Post | What worked | What failed |
|------|------|-------------|-------------|
| 2026-11-17 | sweater pilling v1 | The white text with a dark-green outline read well; the spelling was right | Green pill on green knit with a blurred green sweater behind: no contrast. The pill came out like lime moss with long yellow hairs. A static shot. Line 2 was about 85% wide, too wide for the 9:16 crop |
| 2026-11-17 | sweater pilling v2 | *(to fill in)* Pill pulled against the peach gradient, taut fibres, "GIRTI KYUN NAHI?" | |
