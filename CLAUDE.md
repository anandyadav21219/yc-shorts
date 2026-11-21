# yc-shorts — Why Bhai

Faceless Hindi YouTube Shorts: how everyday things work, in 3D. **From 2026-11-20 every Short is an
image Short:** each post is planned in markdown, each spoken phrase gets one stylized 3D image made in
ChatGPT from a paste-ready prompt file, and the images are put together on this Mac with a slow move per
image, burnt-in Hindi captions and the narration. The Hindi narration is an ElevenLabs voice (Anand
makes the take from the script and sends a voice-only MP3). The Three.js code pipeline is retired and
its template post was deleted (2026-11-20). The thumbnail is also made in ChatGPT from a context
prompt with a Devanagari headline. Write it with the `thumbnail-prompt` skill
(`.claude/skills/thumbnail-prompt/`, rules in `playbook/thumbnail.md`). Accuracy comes first: every
image is built from a fact-checked mechanism.

## Read first, instead of re-researching
- `NICHE.md` — channel look, colours, typography, YouTube metadata and title rules
- `playbook/` — reusable how-to. `image-shorts.md` covers the image workflow: one prompt file per
  image, the shared style block, hero images for consistency, checks, and putting the video together.
  Also: story formula and Hindi VO word budget, thumbnail rules, the mechanism-research method, and
  the post README template
- `tools/build/` — the video build script (`build.py`) and the Devanagari caption renderer; copy into a new post
- `SUGGESTED_IDEAS.md` — do-not-repeat list: exclude these when suggesting ideas, and log new ones there
- `PUBLISHED.md` — what's live: links, titles used, and stats at 24 h / 7 d / 28 d, plus lessons learned
- `INSTAGRAM_FACEBOOK.md` — Instagram + Facebook Page setup and the Reel routine for every post
- `posts/<slug>/` — one folder per Short: `README.md` (fact sheet, script, image list), `prompts/`
  (one ChatGPT prompt per image), `images/`, the MP4, `thumbnail-prompt.md` and `upload.md` (YouTube +
  Instagram/Facebook fields in one file). Once a post is live, only `<slug>.mp4`, `thumbnail.png` and
  `upload.md` are kept (Anand's call, 2026-11-21). Working files of past posts are in git history

## Keep it reusable
- Anything learned that applies beyond one object (prompting, consistency, framing, voice pacing, what
  worked or failed) goes into the matching `playbook/` file.
- Object-specific facts and sources stay in that post's README (*Mechanism check*).
- Tool facts carry a "checked" date. Re-check only when something looks off.
