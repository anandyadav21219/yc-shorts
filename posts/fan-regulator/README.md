# Post — "पंखे का रेगुलेटर स्पीड कैसे घटाता-बढ़ाता है?"

**How a ceiling-fan regulator changes the speed, and why the old one ran hot**
~35 s · 9:16 · image Short: 14 stylized-3D images from ChatGPT, ElevenLabs Hindi voice, captions

> Channel style, colours and typography: [../../NICHE.md](../../NICHE.md) → *Channel design*.
> Story rules and word budget: [../../playbook/story-formula.md](../../playbook/story-formula.md).
> Image Short rules (prompts, consistency, checks): [../../playbook/image-shorts.md](../../playbook/image-shorts.md).

## Fact sheet
- **Cause → effect chain:** the regulator sits in series with the fan → it lets less voltage reach the
  motor → the motor pulls with less force → the blades settle at a lower speed.
- **Old regulator (resistor type):** a coil of resistance wire wound on a ceramic former, with taps on an
  arc of contacts and a wiper under the knob. The voltage it holds back is burnt off as heat, which is why
  those black bakelite regulators were warm to the touch. At low speed nearly the same electricity is
  drawn; it just turns into heat in the regulator.
- **New regulator (capacitor step type):** two or three film capacitors on a small board and a rotary step
  switch behind the knob. A capacitor drops voltage on AC without burning it: it stores the energy and
  hands it back every half-cycle. Each step connects a different capacitor (or combination).
  **Smaller capacitance = more voltage held back = slower fan.** The top step bypasses the capacitors.
- **Real parts shown:** bakelite body, resistance coil, ceramic former, brass contacts and wiper; modular
  plastic body, circuit board, box-shaped film capacitors, rotary step switch; 3-blade ceiling fan.
- **Directions:** energy flows from the mains through the regulator to the fan. The yellow arrows are
  **energy (power), not current**. In a series circuit the current going in and coming out is the same,
  so the arrows never claim more current enters than leaves.
- **Left out on purpose:** electronic TRIAC regulators (they also save power, by switching the AC wave on
  late in each half-cycle), the bleeder resistor across the capacitors, the fan's own run capacitor,
  induction-motor slip, power factor, and any numbers (µF, watts).

## Story
**Arc in one line:** the small knob controls the fan → the old one hid a coil → it burnt the leftover
electricity as heat → the new one uses capacitors → they hold electricity and give it back → the knob picks
the capacitor → twist: low speed really saves power only on the new one → loop to the knob.

**Hook text:** not burnt in. The voice starts at 0 s, so a caption is always on screen and *one text at a time*
wins (as on cold-roti). The thumbnail and title carry the hook: पंखे का रेगुलेटर स्पीड कैसे घटाता-बढ़ाता है?

| # | Image | Beat | Voice (Hindi, ElevenLabs) | ~s |
|---|-------|------|---------------------------|----|
| 01 | Wall knob, close-up | Hook | दीवार का ये छोटा-सा नॉब… | 1.8 |
| 02 | Ceiling fan from below, fast | Hook | पंखे को धीमा-तेज़ कैसे करता है? | 2.4 |
| 03 | Old black bakelite regulator | Culprit (old) | पुराने काले रेगुलेटर में… | 1.8 |
| 04 | Old regulator cut open: the coil | Culprit (old) | तार की कॉइल लगी होती थी। | 2.2 |
| 05 | Thick energy arrow in, thin one out | How (old) | पंखे तक कम बिजली पहुँचती थी… | 2.2 |
| 06 | Heat haze rising off the coil | How (old) | बाकी गर्मी बनकर जल जाती थी। | 2.4 |
| 07 | New white modular regulator | Culprit (new) | नए रेगुलेटर में… | 1.4 |
| 08 | New regulator cut open: capacitors | Culprit (new) | कॉइल की जगह कैपेसिटर लगे होते हैं। | 2.6 |
| 09 | Energy flows into a capacitor, no heat | How (new) | कैपेसिटर बिजली को जलाते नहीं… | 2.0 |
| 10 | Energy loops back out | How (new) | बस थामकर वापस लौटा देते हैं। | 2.2 |
| 11 | Knob turns, a different capacitor connects | How (new) | नॉब घुमाते ही छोटा-बड़ा कैपेसिटर जुड़ता है… | 2.8 |
| 12 | Ceiling fan from below, slow | Money shot | और बदल जाती है रफ़्तार। | 2.0 |
| 13 | New regulator on the lowest step, cool | Twist | तो 1 पर नया रेगुलेटर बिजली बचाता है… | 2.6 |
| 14 | Old (hot) and new (cool) side by side | Twist | और पुराना वही बिजली गर्मी में उड़ा देता था। | 3.0 |
| 01 | Wall knob again (reuse, no new image) | Loop | — | 1.5 |

Cut times are measured from the ElevenLabs take (`audio/vo.mp3`, 35.6 s, Morgan) and live in `build/build.py`.

**Full script (82 words ≈ 35 s; every line ≤ 12 words). Paste into ElevenLabs as one take:**

> दीवार का ये छोटा-सा नॉब… पंखे को धीमा-तेज़ कैसे करता है?
>
> पुराने काले रेगुलेटर में… तार की कॉइल लगी होती थी।
>
> पंखे तक कम बिजली पहुँचती थी… बाकी गर्मी बनकर जल जाती थी।
>
> नए रेगुलेटर में… कॉइल की जगह कैपेसिटर लगे होते हैं।
>
> कैपेसिटर बिजली को जलाते नहीं… बस थामकर वापस लौटा देते हैं।
>
> नॉब घुमाते ही छोटा-बड़ा कैपेसिटर जुड़ता है… और बदल जाती है रफ़्तार।
>
> तो 1 पर नया रेगुलेटर बिजली बचाता है… और पुराना वही बिजली गर्मी में उड़ा देता था।

## Images: 14 to make, one prompt file each
Every prompt in [prompts/](prompts/) is complete and ready to paste. Make them **in order, in one ChatGPT
chat**, and attach the hero image each file names, so the fan and the two regulators look the same in every
shot. Save each result in `images/` under the name the file gives.

| Hero (make first) | Used again in |
|---|---|
| 01 new white regulator | 07, 08, 11, 13, 14 |
| 02 ceiling fan | 12 |
| 03 old black regulator | 04, 05, 06, 14 |

[01](prompts/01-wall-knob.md) · [02](prompts/02-fan-fast.md) · [03](prompts/03-old-regulator.md) ·
[04](prompts/04-old-coil-cutaway.md) · [05](prompts/05-old-less-power.md) · [06](prompts/06-old-heat.md) ·
[07](prompts/07-new-regulator.md) · [08](prompts/08-new-capacitors.md) · [09](prompts/09-capacitor-in.md) ·
[10](prompts/10-capacitor-back.md) · [11](prompts/11-knob-turn.md) · [12](prompts/12-fan-slow.md) ·
[13](prompts/13-new-saves.md) · [14](prompts/14-old-vs-new.md)

## Look (on top of the channel style)
- **Objects:** an Indian white modular switch plate with a round regulator knob; an old black bakelite
  dome regulator on a small wooden board; a white 3-blade ceiling fan seen from below.
- **Colour code for this post:** energy = matte golden-yellow arrows; heat = soft translucent warm haze
  with small coral wavy arrows. Nothing glows and nothing is red-hot.
- **Backgrounds:** peach for the new regulator, coral pink for the old one, mint for the fan and the
  capacitor close-ups, cream wherever yellow arrows need contrast.

## Files
| File | What it is |
|---|---|
| `README.md` | This plan: fact sheet, script, image list |
| `prompts/NN-*.md` | One paste-ready ChatGPT prompt per image |
| `images/NN-*.png` | The approved images (saved by Anand) |
| `audio/vo.mp3` | The ElevenLabs take (from Anand, Morgan, 35.6 s) |
| `build/build.py`, `build/caption.swift` | Puts the video together: cuts, slow moves, captions, voice |
| `fan-regulator.mp4` | The finished Short |
| `thumbnail-prompt.md`, `youtube.md`, `instagram.md` | Made after the video, as for every post |

## Thumbnail
- **Prompt:** `thumbnail-prompt.md` · **Image:** `images/thumbnail.png` (ChatGPT, 20 Nov 2026)
- **Text ChatGPT chose:** `पंखे का रेगुलेटर` / `स्पीड कैसे बदलता है?`

## Mechanism check
Resistor regulators drop the fan's voltage across a wire-wound resistor and waste that energy as heat;
capacitor step regulators drop it across a capacitor's reactance, which stores and returns the energy, so
low speed really uses less electricity. Electronic (TRIAC) regulators also save power, by phase control.
The video shows the resistor and capacitor types only.

Sources: [EngineersGarage, how fan regulators work](https://www.engineersgarage.com/insight-how-fan-regulators-work/),
[ElectricalVolt, regulator and power consumption](https://electricalvolt.com/what-is-the-effect-of-the-speed-regulator-of-a-ceiling-fan-on-power-consumption),
[BijliBachao, choosing a fan regulator](https://www.bijlibachao.com/fans/choose-the-right-regulator-for-ceiling-fan-for-electricity-saving.html),
[US 7,489,094, triac phase-angle fan control](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7489094) (checked 2026-11-20).
