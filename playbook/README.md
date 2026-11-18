# Playbook — how we make a Short

Reusable know-how collected while making posts, so each new Short starts here instead of
re-researching. The channel look, colours, typography and YouTube metadata rules live in
[../NICHE.md](../NICHE.md). This folder covers the *how*.

| File | Read it when |
|------|--------------|
| [story-formula.md](story-formula.md) | Writing the script: story arc, hooks, twist + loop, Hindi VO word budget |
| [grok-imagine-higgsfield.md](grok-imagine-higgsfield.md) | Planning and prompting the clips — picture and Hindi voice together (Higgsfield · Grok Imagine) |
| [post-template.md](post-template.md) | Starting a new `posts/<slug>/README.md` — copy it and fill it in |
| [thumbnail.md](thumbnail.md) | Making the thumbnail / Instagram cover in ChatGPT: Hinglish text rules, safe zones, prompt template |

## New post, start to finish
1. **Pick the idea.** Exclude everything in [../SUGGESTED_IDEAS.md](../SUGGESTED_IDEAS.md), then add the new one under *In progress*.
2. **Research the mechanism** with the method below. 2–3 searches are enough.
3. **Write the story** with [story-formula.md](story-formula.md): a beat table with one short
   Hindi VO line per clip, each inside the per-clip word budget.
4. **Create the post folder** from [post-template.md](post-template.md) as `posts/<slug>/README.md`,
   with its *object block* and *voice block*.
5. **Make clip 1 first** in Higgsfield (text-to-video, picture + voice), approve it and use it as the
   baseline for every other clip ([grok-imagine-higgsfield.md](grok-imagine-higgsfield.md)).
6. **Make the other clips:** same object block and voice block in every prompt → 2–3 takes →
   keep the take where both the picture and the voice are right. No ChatGPT stills, no separate
   voiceover.
7. **Edit in CapCut:** clips in order, trim each clip to its spoken line, extract the audio before
   reversing a clip, add the Hindi hook text (upper third) and any extra SFX, end on clip 1's first
   frame for the loop.
8. **Thumbnail:** make it in ChatGPT with [thumbnail.md](thumbnail.md) and save it as
   `posts/<slug>/images/thumbnail.png`.
9. **Upload:** fill `posts/<slug>/youtube.md` using NICHE.md → *YouTube metadata & titles*, then
   move the idea to *Published* in SUGGESTED_IDEAS.md and add a row to [../PUBLISHED.md](../PUBLISHED.md)
   (link, title used, thumbnail). Fill in its stats at 24 h, 7 d and 28 d.

## Researching a mechanism (cheap and reliable)
- **Go straight to patents.** "How does <object> work" searches mostly return Google Patents
  pages anyway, and teardowns or forums rarely show up. A patent's *Background* section
  describes the common design and its variants, so 2–3 patents are enough.
- **Note where designs differ.** Brands put the same part in different places (for example, an
  auto umbrella's opening spring can sit inside the stick, between two sliders, or under the
  top). Show one real, common layout. Simplify, but never invent parts.
- **Fact-check the twist hardest.** It becomes the title and the line people quote.
- **Write it down once.** Put a one-line *Mechanism check* and the source links at the bottom of
  the post README. Anything that applies beyond one object goes into this playbook instead.
- **Standard web search is enough.** Use extended search only when standard results are thin.
