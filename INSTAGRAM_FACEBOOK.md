# Instagram & Facebook

Post every Why Bhai Short as an **Instagram Reel** and on a **Facebook Page**: the same 9:16 video,
the same file as YouTube. One-time setup first, then the routine for every post.

> Channel look and YouTube playbook: [NICHE.md](NICHE.md). Per-post paste-ready fields live in
> `posts/<slug>/instagram.md` (first example: [posts/pressure-cooker-whistle/instagram.md](posts/pressure-cooker-whistle/instagram.md)).

## Facebook: personal profile or Page? → a Page, created from your personal profile
- **There is no "Page only" option.** Facebook needs a personal profile to create and run a Page.
  The profile is only the login behind it. The Page is a separate public identity with its own
  followers, posts and insights.
- **Don't create a second personal account called "Why Bhai".** A personal profile must be one real
  person under their real name. A brand-named profile can get disabled, and a Page whose only admin
  is that profile goes down with it. Don't use Facebook's "additional profile" option for it either,
  because Meta is phasing that out.
- **Your name stays off the Page.** Visitors see "Why Bhai". The Page's transparency section only
  shows the country of the people who manage it. Once you switch into the Page, you post, comment
  and reply *as Why Bhai*.
- **Not "professional mode".** Professional mode turns your own profile into a creator profile under
  your own name. That suits creators who show their face, not a faceless brand.

---

## One-time setup

### 1. Instagram account
1. **Sign up with the channel's email** (the one behind the YouTube channel), not your personal
   Instagram. The app can hold both accounts; tap your username at the top of your profile to switch.
2. **Username:** the same handle as YouTube. If it's taken, pick one variant and use it on every
   platform.
3. **Switch to a Creator account:** profile → ☰ → *For professionals* → *Account type and tools* →
   *Switch to professional account* → **Creator** → category **Education**.
   Choose Creator, not Business: Business is meant for shops, with a restricted music library and
   shopping tools you don't need.
4. **Profile:**
   - **Photo:** the same channel icon as YouTube, exported from `branding/` as a **1080×1080 PNG**
     (Instagram and Facebook don't accept SVG). It's shown as a circle, so keep the mark centred.
   - **Name:** Instagram search matches this field, so put the topic in it:
     `Why Bhai | Science in Hindi` (alt: `Why Bhai | How Things Work`)
   - **Bio** (150 characters max):
     ```
     Rozmarra ki cheezein andar se kaise kaam karti hain 🔍
     3D mein, Hindi mein · Nayi Reel har din
     ```
   - **Links:** the YouTube channel. Add the Facebook Page once it exists.
5. **Security:** *Accounts Center → Password and security → Two-factor authentication* → on. Save
   the backup codes with the channel's other logins.

### 2. Facebook Page
1. Log in to Facebook **as yourself** → *Menu → Pages → Create new Page*.
2. **Name:** `Why Bhai` (only the name: Facebook's Page rules don't allow extra descriptions in Page
   names). **Category:** `Video creator` + `Education`. **Bio:** same as Instagram.
3. **Profile picture:** the same 1080×1080 icon. **Cover photo:** 1640×924, with the logo and any
   text inside the middle 1640×624 strip. Facebook crops the cover wider on desktop than on phones,
   and that strip shows on both.
4. **Username:** the same handle, which gives you `facebook.com/<handle>`. Add the YouTube and
   Instagram links to the Page's contact info.
5. **Invite friends:** optional. Skip it if you want to keep the Page separate from your personal life.
6. **Backup admin (recommended):** give one trusted person full control under *Page access*, so a
   problem with your profile can't lock you out of the Page. Turn on two-factor authentication on
   your personal profile too.

### 3. Connect Instagram to the Page
- On Facebook, switch into the Page → *Professional dashboard → Linked accounts → Instagram →
  Connect account*, then log in as the Why Bhai Instagram. You can also do it from Instagram:
  *Edit profile → Page → Connect*.
- To check it worked, open *Edit profile* on Instagram: it should show **Why Bhai** next to *Page*.
- This turns on **Share to Facebook** for every Reel. It also lets you use **Meta Business Suite**
  (business.facebook.com) to upload to and schedule on both platforms from the Mac.

---

## Every post: the Reel routine
Apply this to **every** Short. Save each post's filled version as `posts/<slug>/instagram.md`.

### Video
- **Upload the CapCut export**, the same MP4 as YouTube. The first one is already right:
  `posts/pressure-cooker-whistle/video/pressure-cooker-whistle.mp4` is 1080×1920, H.264/AAC, 33 s.
- **Length:** Instagram recommends Reels up to 3 minutes long to non-followers. The 30–45 s format
  is well inside that.
- **Your own video on several platforms is fine.** Meta demotes reposts of other people's content
  and videos with visible watermarks. So never re-download your Short from YouTube, and remove
  CapCut's ending clip and watermark.
- **Text position:** Instagram lays its controls over the video: a header at the top, the caption and
  audio at the bottom, and buttons down the right edge. At 1080×1920, put the Hindi hook text about
  **280–640 px from the top**. That's still the upper third, so it works for Shorts too. Keep
  anything important out of the bottom ~450 px and away from the right edge.

### Cover
- **Use the YouTube thumbnail:** *Edit cover → Add from camera roll*.
- **The profile grid shows only the middle 3:4 of the cover**, cutting about 240 px off the top and
  the bottom. A title in the top 240 px vanishes from your grid, and the first thumbnail has this
  problem. Fix it on the cover screen with *Profile grid*, dragging the crop up. For future
  thumbnails, put the title 280–640 px from the top.

### Caption (the same text goes on Instagram and Facebook)
Write it in Hinglish like the YouTube description, but for someone scrolling who never searched for you:
1. **Line 1 is the hook.** Only the first line shows before "…more", so reuse the YouTube title
   (the hidden-truth line).
2. **2–3 lines of explanation:** the romanised VO, as in the YouTube description. Use the words
   people search for ("pressure cooker", "kaise kaam karta hai"). Instagram search reads captions,
   so this does the job of YouTube's Tags field.
3. **One question** that invites a comment.
4. `Follow karo Why Bhai — nayi Reel har din.`
5. **Max 5 hashtags:** `#whybhai` + 1–2 object tags + `#scienceinhindi #howitworks`. Instagram
   now caps posts at 5. Don't use `#shorts` (it's YouTube-only), and don't put extra hashtags in
   comments.

### Share-screen settings (every time)
- **Share to Facebook: on.** The same Reel then appears on the Why Bhai Page.
- **Advanced settings → Add AI label: on.** Meta requires this label for realistic AI voiceovers
  such as our Higgsfield-generated Hindi voice. It matches the AI disclosure you make on YouTube. Meta can also add
  the label automatically, and it may penalise posts that skip it.
- **Audio:** keep your own track (VO + SFX). It shows up as "Original audio". Don't add trending
  music under the voice.
- **Trial (once it appears):** a Trial Reel goes to non-followers first, which makes it a good way
  to test a second hook. The option unlocks after you reach a minimum follower count.
- **Time:** the same IST windows as YouTube, 1–3 PM or 8–10 PM. Post right away or use the
  schedule option on the share screen.

### After posting
- **Pin a comment**, like on YouTube: ask what object to explain next. Instagram lets you pin up
  to 3 comments.
- **Reply to comments in the first hour.**
- **Share the Reel to your Story** with a Question sticker ("Agli Reel kis cheez par?"). Log good
  answers in [SUGGESTED_IDEAS.md](SUGGESTED_IDEAS.md).
- **Check that the Reel shows on the Facebook Page.** Cross-shared Reels occasionally don't arrive;
  if it's missing, upload it to the Page directly.

### Posting from the Mac
**Meta Business Suite** → *Create reel* → tick both Instagram and the Facebook Page → upload the MP4
and cover → add the caption → *Schedule*. That's one upload for both platforms. Before you
schedule, make sure the AI label is set. If the composer doesn't offer it, post from the phone
instead.

---

## Checking what works (after 2–3 weeks)
- **Insights for each Reel:** look at views from non-followers, average watch time, shares and
  saves. Instagram shows Reels that people watch to the end to more people.
- **Most active times** (*Insights → audience*, which needs about 100 followers): if your audience
  is most active at different times, move your posting window.

## Avoid
- A second Facebook profile for the brand.
- `#shorts`, YouTube or CapCut watermarks, and re-downloaded files.
- More than 5 hashtags.
- Titles or hook text in the top ~280 px of the frame.
