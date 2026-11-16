# Channel Niche

## What we make
Faceless YouTube Shorts: **how everyday things work, animated in 3D.**
Short, satisfying 3D cutaway explainers of ordinary objects people use daily but never think about.

- Inspiration: Mildly Elsewhere (@MildlyElsewhere) — keep our own name, look and style; don't copy theirs.
- Angle: Indian everyday objects first (relatable, less covered), then universal ones.
- Language: Hindi / English (TBD — possibly both, same visuals, two voiceovers).

## Format (every short)
- Length: 30–45 sec, 9:16
- 0–2 sec: hook question on screen ("Why does the cooker whistle?")
- Middle: 3D cutaway, one simple idea per shot
- End: satisfying loop or twist fact
- Voice: AI voiceover
- Production: Google Flow, 10-sec clips (3–4 clips per short), stitched in CapCut

## Channel design (common to every short)
The shared look for the whole channel. Each post keeps this and adds its own object-specific design.

**Style — "Cinematic Engineering 3D":** photoreal exterior of the real object, then a clean,
simplified technical cutaway. Golden rule: same geometry and lighting direction in both, so
it feels like looking *inside the same object*, not a different animation.

**Fixed visual code (same in every post):**
| Role | Hex |
|------|-----|
| Steam — soft white volumetric vapour | `#F4F8FC` |
| Pressure / force — arrows, glow | `#FF792E` |
| Cutaway background — dark charcoal | `#192630` |

Object materials and scene lighting colours are chosen per post (see each post's file).

**Lighting & rendering:** PBR, brushed/real materials, ray-traced reflections where possible;
warm key light from upper-left (~3200–4000 K), soft neutral fill, subtle cool rim on the
exterior. Cutaway = darker background, brighter internal surfaces, restrained orange emissive
arrows. Steam stays translucent white, never an opaque cloud. Avoid heavy bloom, plastic
materials, over-dramatic particles.

**Hindi typography:** Noto Sans Devanagari Bold or Mukta ExtraBold; white lettering with a
charcoal shadow; orange emphasis on key words. Keep text in the upper third, with margin at
the top and right edges for the YouTube Shorts UI.

**Workflow:** generate one master reference image of the object first, then anchor all the
clips to it so the object doesn't change shape or finish between shots.

**Reference channels:** The Slow Mo Guys (motion, timing, vapour), Branch Education (clear
cross-sections), Animagraffs (mechanical movement, camera transitions), Blender product
visualization (realistic materials, studio reflections).

## Open decisions
- [ ] Look: clean studio 3D vs. real kitchen → 3D cutaway (suggested: kitchen → cutaway)
- [ ] Voice: Flow audio per clip vs. one separate voiceover (suggested: separate VO)
- [ ] Language: Hindi / English / both
- [ ] Reference images for Flow (cooker cutaway render, whistle close-up)
- [ ] Channel name

## Files
- [FIRST_POST.md](FIRST_POST.md) — first post plan (script + this post's design)
- [POST_IDEAS.md](POST_IDEAS.md) — backlog of post ideas
