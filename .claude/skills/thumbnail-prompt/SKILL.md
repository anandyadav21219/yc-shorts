---
name: thumbnail-prompt
description: Writes the paste-ready ChatGPT image prompt for a Why Bhai Short's vertical 9:16 thumbnail with a Hindi (Devanagari) headline, built from the post's own README and video, and saves it as posts/<slug>/thumbnail-prompt.md. Use it whenever Anand asks for a thumbnail, a thumbnail prompt, a cover or an Instagram cover for any video or post in this repo, even when he only says "give me the thumbnail for the new video" or names the video loosely ("the wind one", "1st post").
---

# Thumbnail prompt

Returns one prompt that Anand pastes into ChatGPT to generate the thumbnail. The prompt gives ChatGPT the
video's story, what is on screen and the channel's design style. ChatGPT chooses the moment, the layout and
the Hindi headline itself.

**Why this format:** Anand tested it on 19 Nov 2026. The context prompt gave the rain and sweater
thumbnails he liked. Two other versions failed. One described the old code-rendered thumbnail in detail ("do
not assume from the thumbnail itself"). The other copied the rain result's badges, spacing and layout into the
prompt and came out worse. ChatGPT designs a better thumbnail when it understands the video than when it's
told where to put things.

## 1. Find the post
- Match Anand's words to a folder in `posts/`. "New video" means the most recently changed folder with a
  finished video (an `.mp4` or `video/` folder). Numbers like "1st post" follow `PUBLISHED.md` (#1 is the
  pressure cooker, #2 is sweater pilling).
- Ask only if two folders fit equally well.

## 2. Read what the video really shows
From `posts/<slug>/README.md`:
- **Topic:** the hook question in the first heading, `# Post — "…"`. Copy the Devanagari exactly.
- **Story:** the cause → effect chain, from the fact sheet, script or *Mechanism check*.
- **Twist:** the last beat of the script.
- **Visuals:** the shot or story table (the *Picture* or *What we see* column).

If the folder has `check.jpg` (the contact sheet of every shot), look at it. It shows the real palette and mood
(calm and premium, or bright and playful), which the design-style lines must match.

## 3. Fill the template
```text
Create a vertical 9:16 YouTube Shorts thumbnail (1080×1920) for my Hindi science channel "Why Bhai", which explains how everyday things work in 3D.

VIDEO TOPIC: "[hook question in Devanagari]" ([the same question in English])
What the video shows: [the cause → effect chain in 3–5 plain sentences]. The twist at the end: [the twist in one sentence].
Visuals in the video: [the real things on screen, in story order: the object, its parts, the close-ups, the arrows, any moment that proves something wrong].

WHAT TO MAKE: one eye-catching thumbnail that makes people curious enough to watch. It shouldn't give away the final answer. Pick the strongest idea from the video for the main visual. Write a short, catchy headline in Hindi (Devanagari script), 2 lines and 6 words at most.

DESIGN STYLE:
- Clean, premium stylized 3D, like a high-end motion-graphics studio[, bright and a little playful]. Not a real photo, not a cartoon.
- Smooth soft studio gradient background in [warm, ]tasteful colours ([the video's own palette]), with no [kitchen or ]real environment.[ No [colour] background, so the [object] stands out.]
- [The object's materials and the look of the main elements, in one or two lines.] Soft studio lighting with gentle shadows.
- Accents in matte soft coral[ (what coral means)][ and soft blue/mint (what it means)] only. No neon, no glow effects, no dark blue/purple AI-style look.
- One main subject, big and clear, that reads instantly at small phone size.
- Hindi text: bold, rounded, white with a dark outline and a soft shadow, placed in the upper third. Keep the Devanagari spelling correct.
- Keep the bottom quarter fairly empty, since the YouTube Shorts buttons cover it.
- No English text, logos, watermarks, [people, ]hands or extra clutter.
```

How to fill it:
- **Describe the video, not a picture.** Don't add positions, badges, sizes, hex codes, camera angles or a
  fixed headline. That's the part ChatGPT does better on its own.
- **Write in plain English sentences.** Keep Hindi only for the topic line, so ChatGPT copies it correctly.
- **List only what's really in the video.** The thumbnail should match what the viewer then sees, and every
  part shown has to be accurate.
- **Include the twist, but keep the "shouldn't give away" line.** The thumbnail carries the hook and the YouTube
  title carries the twist, so ChatGPT needs to know the twist in order to avoid it.
- **Only the bracketed design lines change per post:** the mood, palette, materials and accent meanings. The
  rest stays word for word, so every thumbnail looks like the same channel.
- **Contrast:** if the object has a strong colour, keep that colour out of the background (the green sweater
  on a green background failed).
- **A character in the video:** if the video shows a person (the photochromic rider, for example), describe
  them as the stylized character they are on screen, and drop "people" from the last line so the two don't
  contradict each other. Otherwise keep "people" in it.

Examples of finished prompts: `posts/how-rain-works/thumbnail-prompt.md` (calm and premium; Anand liked the
result), `posts/sweater-pilling/thumbnail-prompt.md` (a strong object colour),
`posts/how-wind-works/thumbnail-prompt.md` (bright and playful).

## 4. Save it
Write `posts/<slug>/thumbnail-prompt.md`:

````markdown
# Thumbnail prompt — "[hook question]"

Made [date]: a context prompt for ChatGPT with a Hindi (Devanagari) headline. Method:
[../../playbook/thumbnail.md](../../playbook/thumbnail.md). Paste it into a new ChatGPT chat and save the
result as `images/thumbnail.png`.

```text
[the filled prompt]
```
````

If the post README has a *Thumbnail* section, or says there is no thumbnail, add a line that links to
`thumbnail-prompt.md`. If the file already exists, show Anand the new version before replacing it.

## 5. Reply
Give the filled prompt in one `text` code block, ready to copy. Then add two short lines: paste it into a new
ChatGPT chat, and zoom in on the Hindi headline before uploading (ChatGPT often breaks vowel signs like ँ, ं
and ी). For fixes and checks after generating, point to `playbook/thumbnail.md` → *Checks* and *If it fails*.
