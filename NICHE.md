# Channel Niche

## What we make
Faceless YouTube Shorts: **how everyday things work, animated in 3D.**
Short, satisfying 3D cutaway explainers of ordinary objects people use daily but never think about.

- Inspiration: Mildly Elsewhere (@MildlyElsewhere) — keep our own name, look and style; don't copy theirs.
- Angle: Indian everyday objects first (relatable, less covered), then universal ones.
- Language: Hindi / English (TBD — possibly both, same visuals, two voiceovers).

## Format (every short)
- Length: 20–45 sec, 9:16, 30 fps
- 0–2 sec: hook question on screen ("Why does the cooker whistle?")
- Middle: 3D cutaway, one simple idea per shot
- End: satisfying loop or twist fact
- Voice: Hindi narration by an ElevenLabs voice (one voice-only take of the whole script, MP3 sent by
  Anand), one short line per beat, made first so the shots are cut to its measured pauses
- Captions: the spoken phrase as a plain subtitle, rendered into the video from the script's exact
  Devanagari text, in one style for every post
- Production (from 2026-11-20): an **image Short**. One stylized 3D image per spoken phrase, made in
  ChatGPT from a paste-ready prompt file, then put together on this Mac with a slow move per image,
  burnt-in captions and the voice. No AI video tools. Rules:
  [playbook/image-shorts.md](playbook/image-shorts.md). The thumbnail is also made in ChatGPT from a
  context prompt: [playbook/thumbnail.md](playbook/thumbnail.md). (The Three.js code pipeline used
  18–19 Nov 2026 is retired.)

## Channel design (common to every short)
The shared look for the whole channel. Each post keeps this and adds its own object-specific design.

**Style — clean, premium stylized 3D images:** art-directed 3D educational
illustrations. Believable object modelling with clean geometry and convincing materials (glassy
water, matte soil, soft clouds), but clearly a polished 3D render — **never a real photo, a cartoon,
or generic AI artwork.** Think skilled 3D motion-graphics studio. Every part shown is a real part
(see [playbook/image-shorts.md](playbook/image-shorts.md)).

**Background:** smooth studio gradient in a harmonious, tasteful palette — soft yellow, peach,
coral pink, mint, cream (picked to suit each subject). No real environments, no props, no
decoration. The background separates the object; it never competes.

**Colour code (consistent across posts):** steam = soft semi-transparent white; mechanical
force / pressure = clean matte graphical arrows in a tasteful accent (soft coral/red); air / flow =
mint; electricity / energy = matte golden-yellow arrows; heat = soft translucent warm haze with small
coral wavy arrows. **No
neon glows, no glowing rings, no stereotypical dark-blue/purple/orange-neon AI palette.**

**Lighting & materials:** soft professional studio lighting, controlled reflections, subtle
contact shadows, realistic textures. The object feels solid and three-dimensional without
looking photographic. Avoid oversaturated or clashing colours and toy-like over-glossy surfaces.

**Composition:** mobile-first 9:16; main object centered and large, readable instantly on a
phone; consistent object shape, materials and framing across every scene; leave room for steam
or arrows where needed.

**Camera — viewpoints nobody gets with their own eyes:** after the establishing image, frame
the part close up, from below, or cut open, with shallow depth of field and a soft rim light. In
the edit each image gets one slow, smooth move (push-in, pan or pull back); no shakes, fast whips
or VFX presets.

**Educational clarity:** one clear idea per image — establish the whole object, then its parts,
then clean 3D cutaways to reveal the inside. Cutaways stay understandable and visually
consistent with the exterior.

**Hindi typography:** Kohinoor Devanagari Bold (installed on the Mac); white lettering with a soft
dark edge and shadow. **The hook title is rendered in the overlay** for the first ~3 s, fading in
from a text-free first frame so the loop stays clean. Keep it in the upper third,
clear of the Shorts/Reels UI. At 1080×1920 that means about **280–640 px from the top**, so the
text survives Instagram's 3:4 grid crop. Thumbnail titles follow the same position rule (see
[INSTAGRAM_FACEBOOK.md](INSTAGRAM_FACEBOOK.md)).

**Thumbnails (from 2026-11-19):** made in ChatGPT from a context prompt that gives the video's story,
what is on screen and this design style, and lets ChatGPT pick the moment, layout and headline. The
headline is **Hindi in Devanagari**, 2 lines and 6 words at most. Don't fix the layout in the prompt.
The thumbnail carries the hook and the title carries the twist. Method and template:
[playbook/thumbnail.md](playbook/thumbnail.md). Each post saves its prompt as `thumbnail-prompt.md`.

**Narration captions (every post, from 2026-11-18):** burnt into the video from the script's
phrases, split at the same pauses as the voice, so the spelling and timing are exact. Plain and
calm: the spoken phrase in Kohinoor Devanagari Bold, 74 px, white with a soft dark edge and no box,
about two-thirds the size of the hook title, starting about 1170 px from the top (inside the
≈ 1150–1300 px band), below the main object and above the Shorts/Reels title and buttons. It shows
only while the narrator speaks. No word-by-word highlights, pop or bounce animations, coloured words
or emoji, and no caption in the first half-second or on the final loop frame. Same style in every post.

**One text at a time (from 2026-11-19, Anand's call):** never two lines or two texts on screen together. Each
caption is one phrase on one line (`white-space: nowrap`, font shrinks to fit 950 px), and the hook title is
left out when a caption is already on screen (posts/cold-roti).

**Workflow:** each object that comes back gets a hero image made first, and every later image
of it is made with that hero attached as a reference, so its shape, materials and palette can't
drift between shots. Check every image before the video is put together.

**Avoid:** generic AI aesthetics, neon / glowing rings, real kitchen backgrounds, unnecessary
props, oversaturated clashing colours, unrealistic or invented parts, toy-like surfaces, any text
beyond the hook title and captions, watermarks, and inconsistent object shapes between scenes.

**References:** [posts/fan-regulator/](posts/fan-regulator/), the first image Short and the layout
for every new one. For thumbnails, `posts/how-rain-works/images/thumbnail-chatgpt.png`. Study Branch Education and
Animagraffs for clear cutaways and mechanical storytelling.

## YouTube metadata & titles (every post)
Apply this to **every** short at upload. Each post saves its filled version as
`posts/<slug>/youtube.md` (see the pressure-cooker post for the first example).

**Inspiration:** Mildly Elsewhere (@MildlyElsewhere) — "How everyday things work." Study how
they title Shorts; use the strategy, not their exact words.

**Language:** Hinglish (Hindi in Roman script + English mix), Title Case. Warm, casual, relatable.

**Title rules (the most important field):**
- **No `#shorts`, no emoji, no channel name in the title.** Just the clean curiosity line.
  (YouTube detects Shorts from the 9:16 ratio.) Hashtags/emoji go in the description only.
- **Never a plain question** ("X kyun hota hai?"). Tease a surprising claim or hidden truth —
  the explanation is the payoff, the title sells the mystery.
- Use one of these three frames (present tense, concrete, specific):
  1. `This [thing] [does something shocking]` → "Ye Chhota Sa Weight Khana Aadhe Time Mein Pakata Hai"
  2. `Why [counterintuitive fact]` → "Cooker Seeti Isi Wajah Se Bajata Hai, Jo Aap Nahi Jaante"
  3. `How a [small/ordinary thing] Becomes a [big thing]` → Mildly Elsewhere's biggest-hit frame;
     reach for it whenever the object has a build-up/transformation.
- Best single pattern for a reveal: a counterintuitive twist from the script's own ending
  (e.g. "Aapka Cooker Seeti Nahi Bajata — Wo Saans Chhodta Hai").

**Description:** short (like theirs). Open with the Hinglish hook question, 2–3 lines of the
actual explanation (reuse the VO script, romanised), a satisfying closing line, then:
`🔔 Subscribe karo Why Bhai — nayi Shorts har din.` End with ~10 hashtags.
Always include: `#shorts #whybhai` + object-specific + `#scienceinhindi #hinglish #howitworks #3danimation`.

**Tags:** mix Hinglish + English search phrases — "<object> kaise kaam karta hai",
"<object> kyun <verb>", "kitchen/everyday science hindi", "science in hinglish", "hindi shorts",
"3d animation", "faceless channel india", plus object-specific terms.

**Pinned comment:** one casual Hinglish question that invites replies + asks what object to cover
next; end with `#WhyBhai`.

**Cadence (from 2026-11-17):** one new Short every day, so the subscribe and follow lines say "har din".

**Upload settings (every time):** Audience = *Not made for kids*; Language = Hindi;
Category = Education; **AI disclosure = Yes** (the narrator is a computer-generated voice, so keeping
the label on is the safe choice); add to the *"How Everyday Things Work"* playlist; publish 1–3 PM or 8–10 PM IST
(Public or Schedule).

## Open decisions
- [x] Look: premium stylized-realistic 3D on a warm studio gradient (see Channel design)
- [x] Production: image Shorts, stylized 3D images from ChatGPT (changed 2026-11-20; Three.js code 18–19 Nov)
- [x] Voice: ElevenLabs Hindi voice (Morgan on how-rain-works), made first, shots cut to its pauses (changed 2026-11-18; Lekha before that sounded poor)
- [ ] Language: Hindi / English / both (first post is Hindi)
- [ ] Channel name

## Files
- [SUGGESTED_IDEAS.md](SUGGESTED_IDEAS.md) — idea log and do-not-repeat list
- [playbook/](playbook/) — reusable how-to: image Shorts workflow, story formula, Hindi VO word budget, thumbnail, post template
- [posts/fan-regulator/](posts/fan-regulator/) — first image Short: the layout for every new post
- [INSTAGRAM_FACEBOOK.md](INSTAGRAM_FACEBOOK.md) — Instagram + Facebook Page setup and the Reel routine for every post
