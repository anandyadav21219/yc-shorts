# Thumbnail — ChatGPT from a context prompt

Every post's thumbnail, which is also the Instagram/Facebook cover, is made in ChatGPT image generation
from a **context prompt** (from 2026-11-19). The prompt gives ChatGPT the video's story, what is on screen and
the channel's design style. ChatGPT picks the moment, the layout and the Hindi headline itself. The
headline is **Hindi in Devanagari**. Result of this method:
[../posts/how-rain-works/images/thumbnail-chatgpt.png](../posts/how-rain-works/images/thumbnail-chatgpt.png).
Prompts: [rain](../posts/how-rain-works/thumbnail-prompt.md), [sweater](../posts/sweater-pilling/thumbnail-prompt.md),
[pressure cooker](../posts/pressure-cooker-whistle/thumbnail-prompt.md), [wind](../posts/how-wind-works/thumbnail-prompt.md).

## The method: the `thumbnail-prompt` skill
The template and the rules for filling it live in the project skill
[../.claude/skills/thumbnail-prompt/SKILL.md](../.claude/skills/thumbnail-prompt/SKILL.md), so there is one copy.
For a new video, ask Claude Code for "the thumbnail prompt for <video>" or run `/thumbnail-prompt <post>`. It
reads the post's README and contact sheet, fills the template, saves `posts/<slug>/thumbnail-prompt.md` and
returns the prompt.

Then:
1. **Paste it into a new ChatGPT chat**, so it doesn't copy an earlier thumbnail.
2. **Check it** (see *Checks*), fix it in the same chat if needed, and save it as
   `posts/<slug>/images/thumbnail.png`.

The key rule: **describe the video, not the picture.** Don't add positions, badges, hex codes, camera angles,
sizes or a fixed headline. ChatGPT does better without them (sweater v4, which spelled out the rain
thumbnail's layout, came out worse).

## Rules
- **The thumbnail and the title split the job.** The thumbnail carries the hook (the question or the
  contradiction); the title carries the twist. That's why the prompt tells ChatGPT the twist but asks it
  not to give it away.
- **Hindi text in Devanagari** (from 2026-11-19; the rain and sweater thumbnails before this used Hinglish
  in Roman capitals).
- **Every visual comes from the video.** List only things that are really on screen, so the thumbnail
  matches what the viewer then sees.
- **The subject must contrast with what's behind it.** Green on green failed on sweater v1.

## Checks
- **Hindi spelling:** ChatGPT often breaks Devanagari vowel signs and joined letters (ँ, ं, ी, ्).
  Zoom in and read every letter.
- **Small-size test:** shrink it to about 3 cm wide on the phone. The text and the subject must still read
  at a glance.
- **Safe zones at 1080×1920:** the text near the top, nothing important in the bottom fifth (the Shorts title
  and buttons cover it), and a little margin on both sides.
- **Size:** if ChatGPT gives a 2:3 image, place it on a 1080×1920 canvas, fill the height and let the sides
  crop. Check the text still has space on both sides.
- **Look:** stylized 3D, no hands or people, no neon or glow, no extra text.

## If it fails (reply in the same chat, one fix at a time)
- **Hindi misspelt:** "Fix only the Hindi text so it reads exactly: [line 1] / [line 2]. Change nothing else."
  If it's still wrong, ask for "the same image with no text at all" and add the text yourself.
- **Text too close to the edges or the bottom:** "Make the text smaller and keep it in the upper third, with
  space on both sides."
- **Looks like a photo or a cartoon:** "Make it clearly a clean stylized 3D render."
- **Subject blends into the background:** "Change the background to [a contrasting warm colour]."

## Fallback
If ChatGPT can't get the Hindi right, ask for the same image with no text and add the headline on the Mac
(Kohinoor Devanagari Bold, white with a soft dark edge, upper third). The Three.js thumbnail render was
retired with the code pipeline on 2026-11-20.

## Notes
| Date | Post | What worked | What failed |
|------|------|-------------|-------------|
| 2026-11-17 | sweater pilling v1 | The white text with a dark-green outline read well | Green pill on green knit: no contrast. A static shot. Line 2 was about 85% wide, too wide for the 9:16 crop |
| 2026-11-18 | how-rain-works | Rendered from the scene at the crossed-out tear moment; bluer drop on a peach gradient; auto-fitted text | First render: the drop was ~50% wide and the cross touched the right edge, fixed with `zoom: 1.2`; the drop read sage-green on peach until its attenuation was made bluer |
| 2026-11-19 | how-rain-works, sweater pilling v3 | The context prompt in ChatGPT (story + visuals + design style, Devanagari headline, no fixed layout). ChatGPT put the hook question on coral and mint 3D badges over a floating cut-away of the whole water cycle. Anand liked both results | — |
| 2026-11-19 | sweater pilling v4 | — | Copying the rain thumbnail's badges, spacing and process layout into the prompt came out worse than v3. Don't fix the layout; let ChatGPT design it |
| 2026-11-21 | rickshaw-horn v2 | Anand's feedback on v1: ask for **clear margins on every side** (≥ 8% of the width left/right, ≥ 10% of the height at the top), **bold, attractive colours** with a warm/cool contrast against the object, and a **realistic premium-render look** (real materials, true shadows). The background can be the video's own street, blurred to bokeh. Margins are spacing, not layout, so they don't break the "don't fix the layout" rule | v1 (plain soft gradient, stylized look) read too flat and pale to him |
