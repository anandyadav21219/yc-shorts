# Camera-journey format ("you build it" story)

Studied 2026-11-17 from a reference Short (Mildly Elsewhere, "How a Hole by the Sea Becomes a Dry
Dock", 70 s, 9:16, 24 fps). We take the *method*, never the title, lines, look or watermark.

## What the reference does, frame by frame
| Time | Line (paraphrased) | Camera |
|------|--------------------|--------|
| 0–3 s | Dig a hole by the sea, park a ship in it | Blur-in, then a centred drone shot looking down the empty pit to the sea; water floods in while the camera holds |
| 4–8 s | The hull is crusted with barnacles, you can't scrub it underwater | Camera drops **through the water surface** (half-above/half-below split frame), sees the crusted bulb, rises back out |
| 9–16 s | So you dig a big hole, cut a gate, open it, the ship floats in | The same centred corridor view; the world changes around a camera that barely moves (pit → concrete → gate → flood → ship) |
| 17–19 s | Shut the gate, pump the water out | Fast fly-along beside the ship, high over the deck |
| 20–23 s | As the water drops, the ship rolls over | Waterline split again, camera sinks with the water level |
| 24–28 s | So lay rows of blocks first | **FPV skim at floor height**, blocks fly in and stack in rows with motion blur |
| 29–37 s | It sits on them; jam props on its sides | Low dolly in toward the bow, then between hull and wall |
| 38–47 s | The sea leaks round the gate, so build a gate that floats and sinks into a slot | Fly-through over the wall, close-up of a leak jet, then an **X-ray cutaway** of the gate's tanks filling |
| 48–53 s | The sea pushes it into its slot, the harder it pushes the tighter it seals | **Ground sliced open**: soil and rock layers in the lower third, sea level vs dock floor side by side |
| 55–67 s | Cracks, the floor bulges: groundwater wants to float the dock. Pour a 17-ft floor | Low shot, then the camera **drops below the floor** to show the water pushing up and the thick new slab |
| 68–70 s | You've built a dry dock | Back to the opening's centred hero view, now finished, with one tiny worker for scale |

## The rules we keep
1. **One world, one hero object.** The same place for the whole video, so the viewer always knows
   where they are. The camera goes away and comes back to the same centred "hero" view.
2. **Impossible camera.** Moves no real crew can film: through the water surface, through the ground
   (sliced cross-section), X-ray through walls, skimming millimetres above the floor, rushing from
   the top of something to its base.
3. **The world changes, not just the camera.** Things get built, flood, crack and assemble in front
   of a slow or still camera, like a time-lapse.
4. **Story = a chain of problems.** You build it → *but* a problem → *so* a fix → *but* a new
   problem → … → finished. Second person ("आप"), one short phrase per shot, a cut or a camera change
   every 1–3 s.
5. **Moves hide the cuts.** Motion-blur whips, the camera passing through a surface, or a match on
   the same framing join the clips, so it feels like one continuous flight.
6. **Scale cue at the end:** one tiny person beside the finished thing.

## What makes ours different (don't copy)
- Never use the "How a Hole Becomes…" title or a "Congratulations, you've built…" ending. In
  English that title is now a crowded copycat genre (e.g. a "Bunker" Short at 2 crore views; checked
  2026-11-17).
- **Our hook is an everyday Indian "why is it like this?" question** that the build story answers.
  The ending comes back to the everyday view and answers the question ("अब समझे…?"). That fits Why Bhai.
- Hindi narration (see [story-formula.md](story-formula.md)), our own colour/lighting rules from
  [../NICHE.md](../NICHE.md) wherever they still apply.

## How the reference is probably made (researched 2026-11-17)
**Not confirmed anywhere.** The channel names no tools on YouTube, its site or in search results.
The video page shows no "altered or synthetic content" label, and the description calls it "this 3D
animation". What the frames show:
- **AI video, not a Blender/3D render.** At 25.5 s the keel blocks smear, ghost and pop in half-formed,
  a crane cable hangs from nothing, and the anchors at 69.5 s are melted blobs. A real render has
  clean motion blur and solid objects. The brick building also changes design between shots.
- **Many short clips, not one long one.** Each shot runs 1–4 s, with blur whips or a camera passing
  through a surface hiding each cut. File: 1080×1920, 24 fps, 70 s.
- **Image first, then video.** The ship, dock and cranes stay close to identical across 70 s, which
  text-to-video can't hold. So the likely path is: consistent keyframe stills from an image model
  that keeps a reference, then image-to-video with **start and end frames** (each clip's end frame
  is the next clip's start frame), then cut in an editor with captions and a watermark on top.
- **Which video model:** can't tell from the pixels.

**What it means for us:** in code this format is easier, not harder. We own the world, so the
place stays identical from start to end and the camera can fly anywhere: through the water surface,
under the road, through a sliced-open wall. The smearing and melting of AI video can't happen.

## Making it in Three.js
- **One scene for the whole video** (the place), with the "world changes" done as time-driven
  animation in `renderAt(t)`: things build, flood or crack while the camera moves slowly.
- **The camera is a path, not cuts.** Write it as keyframes in time (position + look target) and
  interpolate with eased segments. Hide the few real cuts with a pass through a surface (water, ground)
  or a match on the same framing.
- **Impossible moves are just camera positions:** under the tarmac with the road drawn as a slab
  seen from below, half above and half below a water plane, inside a cut-away wall.
- **Keep the hero view identical** in the first and last seconds, for the loop.
- Pipeline, accuracy rules and review: [threejs-video.md](threejs-video.md).
