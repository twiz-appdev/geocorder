"""Builds the WorkTrail Recorder site: python build.py writes the four pages next to this file."""
import pathlib

ROOT = pathlib.Path(__file__).parent
EMAIL = 'tekdigitalsolutionsllc@gmail.com'
UPDATED = 'October 5, 2026'

MARK = ('<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="8" fill="#131a23" stroke="#263241"/>'
        '<g fill="#3d8ff0"><rect x="6" y="13" width="2.6" height="6" rx="1.3"/><rect x="10.4" y="9" width="2.6" height="14" rx="1.3"/>'
        '<rect x="14.8" y="5.5" width="2.6" height="21" rx="1.3"/><rect x="19.2" y="10" width="2.6" height="12" rx="1.3"/>'
        '<rect x="23.6" y="13.5" width="2.6" height="5" rx="1.3"/></g></svg>')


def wave():
    import math
    bars = []
    count = 96
    for i in range(count):
        level = 0.18 + 0.82 * abs(math.sin(i * 0.37) * math.cos(i * 0.11 + 0.6))
        height = round(8 + level * 60, 1)
        bars.append('<rect x="%.1f" y="%.1f" width="4" height="%.1f" rx="2" opacity="%.2f"/>'
                    % (i * 10 + 3, (72 - height) / 2, height, 0.35 + 0.65 * level))
    return '<svg class="wave" viewBox="0 0 960 72" preserveAspectRatio="none" aria-hidden="true">' + ''.join(bars) + '</svg>'


def page(path, title, description, body, current):
    depth = '' if path == 'index.html' else '../'
    def link(name, href, key):
        mark = ' aria-current="page"' if key == current else ''
        return '<a href="%s%s"%s>%s</a>' % (depth, href, mark, name)
    nav = ''.join([link('Home', '', 'home'), link('Support', 'support/', 'support'),
                   link('Privacy', 'privacy/', 'privacy'), link('Terms', 'terms/', 'terms')])
    html = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(description)s">
<meta name="theme-color" content="#0a0f15">
<link rel="stylesheet" href="%(depth)sstyles.css">
<link rel="icon" href="%(depth)sicon.svg" type="image/svg+xml">
</head>
<body>
<header class="site-header"><div class="wrap">
<a class="brand" href="%(home)s">%(mark)s<span>WORKTRAIL RECORDER</span></a>
<nav class="nav" aria-label="Site">%(nav)s</nav>
</div></header>
<main>
%(body)s
</main>
<footer class="site-footer"><div class="wrap">
<span>&copy; 2026 TEK Digital Solutions. WorkTrail Recorder for iPhone.<br><small>Apple, iPhone, Apple Intelligence, Apple Maps, Siri, iCloud and App Store are trademarks of Apple Inc., registered in the U.S. and other countries. iOS is a trademark or registered trademark of Cisco in the U.S. and other countries and is used under license.</small></span>
<nav aria-label="Footer">%(nav)s<a href="mailto:%(email)s">Contact</a></nav>
</div></footer>
</body>
</html>
''' % dict(title=title, description=description, depth=depth, home=depth or './', mark=MARK, nav=nav, body=body, email=EMAIL)
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding='utf-8', newline='\n')


def card(tag, title, text):
    return '<div class="card"><span class="tag">%s</span><h3>%s</h3><p>%s</p></div>' % (tag, title, text)


HOME = '''
<div class="hero"><div class="wrap">
<span class="pill">for iPhone</span>
<h1>Record your working day.<br>Read it back in writing.</h1>
<p class="lead">WorkTrail Recorder keeps a spoken record of your day, marks the moments that matter, and turns speech into text on your iPhone. No account. No WorkTrail server.</p>
<span class="cta" aria-disabled="true">Coming soon to the App Store</span>
<span class="cta-note">WorkTrail Recorder is in final testing.</span>
''' + wave() + '''
</div></div>

<section id="features"><div class="wrap">
<h2>Built for long days</h2>
<p class="sub">Start it when your work begins and stop it when you are done. A call or another app can pause a recording; WorkTrail tries to pick it back up and tells you if it cannot.</p>
<div class="grid">
''' + ''.join([
    card('RECORD', 'All-day recording', 'Sessions split into clips on a schedule you choose and keep recording with the screen off. A notification and Live Activity show whenever WorkTrail is recording.'),
    card('MARK', 'Mark the moment', 'One tap marks what was just said. Save a clip, or save the last few minutes after something worth keeping.'),
    card('TRANSCRIBE', 'Transcripts on the device', 'Speech becomes text on your iPhone with a built-in speech model; larger models are optional downloads. Quiet speech is brought up to a clear level first, and you get a cleaned copy next to the raw one.'),
    card('READ', 'Search, correct, share', 'Read along with the audio, search across transcripts, fix a passage, and share the text with or without the recording.'),
    card('JOURNAL', 'A work journal', 'Write notes against the day and set reminders tied to the places you work.'),
    card('AUTOMATE', 'Recording by place', 'When you arrive at, stay at, or leave a place you save, WorkTrail starts recording if it is open, or sends a notification you tap to start. Arm and disarm each place with a switch.'),
    card('BACK UP', 'Your folder, your copy', 'Back up sessions to a folder you pick in Files, check the copy against the original, and copy missing recordings back from it.'),
    card('SUMMARIZE', 'On-device summaries', 'On iPhone models with Apple Intelligence (iOS 26 or later), summarize the records you choose after reviewing exactly what will be used.'),
    card('LOOK', 'Themes and density', 'Dark key-style themes including Hazy Black, and a display density setting that fits more on screen.'),
]) + '''
</div>
</div></section>

<section class="privacy-band"><div class="wrap">
<h2>Private by design</h2>
<p class="sub">A recorder hears everything, so it should keep it to itself.</p>
<div class="grid">
''' + ''.join([
    card('NO ACCOUNT', 'Nothing to sign in to', 'There is no WorkTrail account and no WorkTrail server. The app works without either.'),
    card('ON DEVICE', 'Audio is never uploaded by the app', 'Recordings and transcripts are stored on the device. Transcription runs on the device. Copies leave it only through backups you set up, including a cloud folder you choose, or when you share them.'),
    card('NO TRACKING', 'No analytics, no ads', 'The app does not collect usage data, does not track you, and shows no advertising.'),
]) + '''
</div>
<p class="sub" style="margin-top:24px">The full details are in the <a href="privacy/">privacy policy</a>.</p>
</div></section>

'''

FAQ = [
    ('Do I need an account?', 'No. There is nothing to sign in to. The app works as soon as you allow the microphone.'),
    ('Does recording keep going when the screen is off?', 'Yes. Recording continues in the background, and a notification and Live Activity show that it is running. A phone call or another app taking over audio pauses it. WorkTrail tries to resume when the interruption ends; if it cannot, it shows a notification and resumes when you tap it or return to the app.'),
    ('How do I get a transcript?', 'Open a recording, tap Speech, then Transcribe. A speech model is built in. Transcription happens on your iPhone and can take a while for long recordings.'),
    ('The transcript missed words. What can I do?', 'Choose a larger model under More, Settings, Transcription, Model / quality (Balanced or Accurate catch more than Fast), then run a new pass on the recording. Keeping the phone closer to the speaker helps the most.'),
    ('Where are my recordings stored?', 'On your iPhone, inside the app. They are included in your iPhone backup (iCloud Backup or a computer backup) if you use one. To keep a separate copy, use Backup and choose a folder in Files, such as iCloud Drive.'),
    ('How does recording by place work?', 'In Automation, save a place, choose whether arriving, staying or leaving should start a recording, and arm it. The app asks for Always location access so it can notice this while closed. If WorkTrail is open the recording starts; otherwise you get a notification with a Start Recording button, because iPhone does not let apps switch the microphone on in the background. iPhone watches up to 20 armed places at once.'),
    ('How do I delete everything?', 'More, Settings, Backup + Reset, Open backup + reset center, Prepare clean-install reset (you type a confirmation phrase) erases the recordings, transcripts, journal, places and settings the app stored on the iPhone. Deleting the app does the same. Copies in your backup folder, in an iPhone or iCloud backup, or that you shared are not removed.'),
    ('Can it record phone calls?', 'No. iPhone does not allow apps to record calls, and WorkTrail Recorder does not try to.'),
]

SUPPORT = '''
<div class="doc"><div class="wrap">
<h1>Support</h1>
<p class="meta">Help with WorkTrail Recorder for iPhone.</p>
<div class="note"><p>Email <a href="mailto:%(email)s">%(email)s</a>. Include your iPhone model, iOS version and the app version shown under More, About. Please do not send recordings or transcripts; they can contain other people's voices and words. The Diagnostics reports are enough in almost every case.</p></div>
<h2>Common questions</h2>
%(faq)s
<h2>Reporting a problem</h2>
<p>Under More, Diagnostics you can share a text report of the app's state. Attaching it to your email helps us find the cause faster. The <a href="../privacy/">privacy policy</a> lists what each report contains.</p>
</div></div>
''' % dict(email=EMAIL, faq=''.join('<details><summary>%s</summary><p>%s</p></details>' % item for item in FAQ))

PRIVACY = '''
<div class="doc"><div class="wrap">
<h1>Privacy Policy</h1>
<p class="meta">WorkTrail Recorder for iPhone &middot; Last updated %(updated)s</p>

<p>WorkTrail Recorder is published by TEK Digital Solutions ("we"). This policy explains what the app does with your information. The short version: the app has no account and no server of ours, and we do not collect your recordings, transcripts, location or usage data.</p>

<h2>Information we collect</h2>
<p>None through the app. The app does not send us your recordings, transcripts, journal entries, saved places, location, contacts, identifiers or analytics. It contains no advertising and no tracking.</p>
<p>If you email us, we receive your email address and whatever you send, including any report you attach from More, Diagnostics. The readiness report can include the names of your saved places and of your microphone or headset. A recording test report also includes that session's date, times and length, a timeline of its events (including arrivals at and departures from named places), and your iPhone model, iOS version, battery level and free storage. Neither report contains audio, transcript text, journal text or coordinates. Our email is provided by Google (Gmail), which stores messages for us in the United States. We use what you send only to answer you and fix the problem you report, and we delete support email within 24 months after the conversation ends. We do not sell or share personal information, and we do not use it for advertising.</p>

<h2>Information stored on your iPhone</h2>
<ul>
<li><strong>Recordings and transcripts.</strong> Audio you record, the transcripts made from it, marks, clips and summaries are stored in the app's private storage on your iPhone.</li>
<li><strong>Journal entries and saved places.</strong> Notes you write and the places you save for reminders and recording rules.</li>
<li><strong>Location.</strong> If you allow it, the app uses your location on the device to tag recordings and marked moments, centre the map, and notice when you arrive at or leave a place you armed. "Always" access is requested only when you turn on a place-based feature or ask for it in Setup. Location is not sent to us. When the map shows your position, your approximate area reaches the map tile services, and coordinates you look up reach Apple, as described under Connections the app makes. Location tags (latitude and longitude) are saved with recordings and marked moments, so backed-up and exported session files include them, and so does a transcript you share "with session details".</li>
<li><strong>Lock Screen.</strong> Reminders and the recording indicator can show titles, place names and note previews on the Lock Screen.</li>
<li><strong>Activity history.</strong> A log of app events, such as recordings started and ended, backups, and arrivals at or departures from places you armed, with their times. The Automation map also remembers your last known position so it opens there.</li>
<li><strong>Settings.</strong> Your preferences, theme and display density.</li>
</ul>
<p>This information leaves your iPhone only when you share it, export it, back it up to a folder you select in Files (for example iCloud Drive or another provider you use), or when your iPhone's own backup (iCloud Backup or a computer backup, if you use one) includes the app's data. Those providers handle the copy under their own terms.</p>

<h2>Connections the app makes</h2>
<p>The app works offline for recording and transcription. It connects to the internet for these features:</p>
<ul>
<li><strong>Map tiles.</strong> The Automation map loads map images for the area you look at from OpenStreetMap (tile.openstreetmap.org) and, for satellite views, the U.S. Geological Survey (basemap.nationalmap.gov). Those services receive your IP address, basic browser information and which map tiles were requested. Because the map opens on your current position, the tiles requested show those services your approximate area (within a few hundred metres). They keep request logs under their own policies.</li>
<li><strong>Address search and address lookup.</strong> Searching for a place, the suggestions shown while you type, and looking up the address of a pin or of your current position use Apple Maps. Apple receives the text you type, the map area or position being searched near, and the coordinates being looked up. "Open in Maps" hands a recording's coordinates to Apple Maps when you tap it.</li>
<li><strong>Speech models.</strong> If you choose a larger transcription model, it is downloaded from huggingface.co, which receives your IP address. Your audio is never part of that request.</li>
<li><strong>Summaries.</strong> Optional summaries run on Apple's on-device model on supported iPhones.</li>
</ul>
<p>These services are operated by others under their own privacy policies. We receive nothing from them about you.</p>

<h2>This website</h2>
<p>This website is hosted on GitHub Pages. GitHub receives your IP address and browser information when you visit, under GitHub's privacy statement. The site sets no cookies and uses no analytics or advertising.</p>

<h2>Recording</h2>
<p>You decide what is recorded. Use WorkTrail in line with the recording laws where you are.</p>

<h2>Children</h2>
<p>The app is not directed to children under 13, and the app collects no information from anyone. We do not knowingly collect personal information from children under 13. If a child under 13 has emailed us, a parent or guardian can ask us to delete it, and if we learn of it we delete it.</p>

<h2>Deleting your information</h2>
<p>Deleting a recording in the app removes its audio, transcripts, marks and clips from the iPhone. Summaries made from it, journal notes linked to it and the activity history stay until you delete them or use the clean-install reset. The clean-install reset under More, Settings, Backup + Reset erases the recordings, transcripts, journal, places and settings the app stored. Deleting the app does the same. Copies in your backup folder, in an iPhone or iCloud backup, or that you shared or exported are not removed by the app and are yours to remove.</p>

<h2>Your choices and rights</h2>
<p>We hold no app data about you, so the only information we can access, correct or delete is email you sent us. To see, correct or delete it, or to object to how we use it, write to <a href="mailto:%(email)s">%(email)s</a>; we answer within 30 days. If you are in the EU or UK: we handle your email to answer your request and support the app you bought (our legitimate interest, and our contract with you); it is stored in the United States by our email provider; and you may complain to your data protection authority. The app and this site do not track you across other companies' apps or websites, so they work the same whether or not your browser sends a Do Not Track signal.</p>

<h2>Changes to this policy</h2>
<p>If the app begins handling information differently, this page will be updated and the date above will change. If a change means more information leaves your iPhone than this policy describes, the app's update notes will say so before the change takes effect.</p>

<h2>Contact</h2>
<p>Questions about privacy: <a href="mailto:%(email)s">%(email)s</a>.</p>
</div></div>
''' % dict(email=EMAIL, updated=UPDATED)

TERMS = '''
<div class="doc"><div class="wrap">
<h1>Terms of Use</h1>
<p class="meta">WorkTrail Recorder for iPhone &middot; Last updated %(updated)s</p>

<p>WorkTrail Recorder (the "app") is published by TEK Digital Solutions ("we", "us"). The licence for the app is Apple's Licensed Application End User License Agreement (the standard App Store licence). These terms add to it; they are between you and us, not Apple. Where these terms and Apple's licence differ, Apple's licence governs. By downloading or using the app you agree to both.</p>

<h2>Licence</h2>
<p>Your licence to use the app is the one in Apple's standard licence: personal, non-transferable use on Apple devices you own or control, as permitted by the App Store's usage rules. You may not resell the app, or use it to break the law.</p>

<h2>Your recordings and your responsibility</h2>
<ul>
<li>Recordings, transcripts and notes you make are yours.</li>
<li>You are responsible for using the app lawfully, including the recording, privacy and workplace laws that apply to you.</li>
<li>You are responsible for how you store, share and back up what you record.</li>
</ul>

<h2>Transcripts and summaries</h2>
<p>Transcripts and summaries are produced automatically and can contain errors, omissions or words that were not said. Check them against the audio before relying on them. They are not a substitute for professional, legal, medical or safety records.</p>

<h2>Keeping your recordings safe</h2>
<p>Recordings are stored on your iPhone; the only other copies are the ones in your own backups. A recording can be lost if the device fails, runs out of storage, is reset, or the app is deleted, and a recording can be interrupted by calls, other apps or the system. Keep backups of anything you cannot afford to lose.</p>

<h2>Third-party services</h2>
<p>Map images, address search and optional model downloads are provided by others, as described in the <a href="../privacy/">privacy policy</a>. Their availability is outside our control. Open-source components used by the app are listed, with their licences, under More, About in the app.</p>

<h2>No warranty</h2>
<p>The app is provided "as is" and "as available", without warranties of any kind, to the fullest extent the law allows. We do not warrant that the app will be uninterrupted, error-free, or that any recording or transcript will be complete or accurate.</p>

<h2>Support</h2>
<p>We, not Apple, are responsible for the app and for supporting it. Contact us at the address below.</p>

<h2>Limitation of liability</h2>
<p>To the fullest extent the law allows, we are not liable for indirect, incidental, special or consequential damages, or for lost data or recordings, and we are not responsible for claims arising from what you record or how you use the app. Our total liability for all claims relating to the app will not exceed the greater of the amount you paid for the app and US$50. These limits do not apply to liability for death or personal injury caused by our negligence, for fraud, for our intentional or grossly negligent misconduct, or to any other liability that cannot be limited under the law that applies to you. Nothing in these terms removes rights you have under consumer law that cannot be excluded.</p>

<h2>Apple</h2>
<p>Apple is not responsible for the app or its content and has no obligation to provide maintenance or support for it. If the app fails to conform to any applicable warranty, you may notify Apple, and Apple will refund the purchase price; to the maximum extent the law allows, Apple has no other warranty obligation for the app. We, not Apple, are responsible for addressing any claims relating to the app, including product liability claims, claims that the app fails to meet legal or regulatory requirements, consumer-protection or privacy claims, and claims that the app infringes someone else's intellectual property. You confirm that you are not located in a country subject to a US Government embargo or designated by the US Government as a "terrorist supporting" country, and that you are not on any US Government list of prohibited or restricted parties. Apple and its subsidiaries are third-party beneficiaries of these terms and may enforce them against you.</p>

<h2>Changes</h2>
<p>We may update the app and these terms. Updated terms apply from the date shown above and only to use of the app after that date; they do not apply to a dispute that arose before they were posted. If you do not agree to updated terms, stop using the app. If any part of these terms is found unenforceable, the rest remains in effect.</p>

<h2>Contact</h2>
<p><a href="mailto:%(email)s">%(email)s</a></p>
</div></div>
''' % dict(email=EMAIL, updated=UPDATED)

page('index.html', 'WorkTrail Recorder — record, mark and transcribe on iPhone',
     'WorkTrail Recorder keeps a spoken record of your working day and transcribes it on your iPhone. No account, no WorkTrail server.', HOME, 'home')
page('support/index.html', 'Support — WorkTrail Recorder', 'Help and contact for WorkTrail Recorder for iPhone.', SUPPORT, 'support')
page('privacy/index.html', 'Privacy Policy — WorkTrail Recorder', 'What WorkTrail Recorder does with your information: the app sends nothing to us, and recordings stay on your iPhone.', PRIVACY, 'privacy')
page('terms/index.html', 'Terms of Use — WorkTrail Recorder', 'Terms of use for WorkTrail Recorder for iPhone.', TERMS, 'terms')
(ROOT / 'icon.svg').write_text(MARK.replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" '), encoding='utf-8', newline='\n')
(ROOT / '.nojekyll').write_text('', encoding='utf-8')
print('built')
