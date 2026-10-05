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
<span>&copy; 2026 TEK Digital Solutions. WorkTrail Recorder for iPhone.</span>
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
<span class="pill">FOR IPHONE</span>
<h1>Record your working day.<br>Read it back in writing.</h1>
<p class="lead">WorkTrail Recorder keeps a spoken record of your day, marks the moments that matter, and turns speech into text on your iPhone. No account. No cloud.</p>
<span class="cta" aria-disabled="true">Coming soon to the App Store</span>
<span class="cta-note">WorkTrail Recorder is in final testing.</span>
''' + wave() + '''
</div></div>

<section id="features"><div class="wrap">
<h2>Built for long days</h2>
<p class="sub">Start it in the morning and let it run. Everything you need later is one tap away.</p>
<div class="grid">
''' + ''.join([
    card('RECORD', 'All-day recording', 'Sessions split into clips on a schedule you choose and keep recording with the screen off or the phone in your pocket.'),
    card('MARK', 'Mark the moment', 'One tap marks what was just said. Save a clip, or save the last few minutes after something worth keeping.'),
    card('TRANSCRIBE', 'Transcripts on the device', 'Speech becomes text on your iPhone. Quiet speech is brought up to a clear level first, and you get a cleaned copy next to the raw one.'),
    card('READ', 'Search, correct, share', 'Read along with the audio, search across transcripts, fix a passage, and share the text with or without the recording.'),
    card('JOURNAL', 'A work journal', 'Write notes against the day and set reminders tied to the places you work.'),
    card('AUTOMATE', 'Recording by place', 'Start or stop recording when you arrive at, stay at, or leave a place you save. Arm and disarm each place with a switch.'),
    card('BACK UP', 'Your folder, your copy', 'Back up sessions to a folder you pick in Files, verify the copy, and restore from it.'),
    card('SUMMARIZE', 'On-device summaries', 'On iPhones with Apple Intelligence, summarize the records you choose after reviewing exactly what will be used.'),
    card('LOOK', 'Themes and density', 'Graphite keys, a Hazy Black theme, and a display density setting that fits more on screen.'),
]) + '''
</div>
</div></section>

<section class="privacy-band"><div class="wrap">
<h2>Private by design</h2>
<p class="sub">A recorder hears everything, so it should keep it to itself.</p>
<div class="grid">
''' + ''.join([
    card('NO ACCOUNT', 'Nothing to sign in to', 'There is no WorkTrail account and no WorkTrail server. The app works without either.'),
    card('ON DEVICE', 'Audio stays on your iPhone', 'Recordings and transcripts are stored on the device. Transcription runs on the device; your audio is not uploaded.'),
    card('NO TRACKING', 'No analytics, no ads', 'The app does not collect usage data, does not track you, and shows no advertising.'),
]) + '''
</div>
<p class="sub" style="margin-top:24px">The full details are in the <a href="privacy/">privacy policy</a>.</p>
</div></section>

<section><div class="wrap">
<h2>Record responsibly</h2>
<p class="sub">Recording people can require their consent. You are responsible for telling people they are being recorded and for following the recording laws where you are. WorkTrail Recorder does not record phone calls.</p>
</div></section>
'''

FAQ = [
    ('Do I need an account?', 'No. There is nothing to sign in to. The app works as soon as you allow the microphone.'),
    ('Does recording keep going when the screen is off?', 'Yes. Recording continues in the background, and a notification and Live Activity show that it is running. A phone call or another app taking over audio pauses it; WorkTrail resumes when the interruption ends or when you return to the app.'),
    ('How do I get a transcript?', 'Open a recording and choose Transcript, then Transcribe. The first time, the app may ask to download a speech model. Transcription happens on your iPhone and can take a while for long recordings.'),
    ('The transcript missed words. What can I do?', 'Choose a larger model under More, Settings, Transcription, Model / quality (Balanced or Accurate catch more than Fast), then run a new pass on the recording. Keeping the phone closer to the speaker helps the most.'),
    ('Where are my recordings stored?', 'On your iPhone, inside the app. To keep a copy elsewhere, use Backup and choose a folder in Files, such as iCloud Drive.'),
    ('How does recording by place work?', 'In Automation, save a place, choose when recording should start or stop, and arm it. The app asks for Always location access at that point so it can notice arrivals while closed. iPhone watches up to 20 armed places at once.'),
    ('How do I delete everything?', 'More, Settings, Backup + Reset, Clean-install reset erases everything the app stored on the iPhone. Deleting the app does the same.'),
    ('Can it record phone calls?', 'No. iPhone does not allow apps to record calls, and WorkTrail Recorder does not try to.'),
]

SUPPORT = '''
<div class="doc"><div class="wrap">
<h1>Support</h1>
<p class="meta">Help with WorkTrail Recorder for iPhone.</p>
<div class="note"><p>Email <a href="mailto:%(email)s">%(email)s</a>. Include your iPhone model, iOS version and the app version shown under More, About. Please do not send recordings unless we ask for one.</p></div>
<h2>Common questions</h2>
%(faq)s
<h2>Reporting a problem</h2>
<p>Under More, Diagnostics you can share a text report of the app's state. Attaching it to your email helps us find the cause faster.</p>
</div></div>
''' % dict(email=EMAIL, faq=''.join('<details><summary>%s</summary><p>%s</p></details>' % item for item in FAQ))

PRIVACY = '''
<div class="doc"><div class="wrap">
<h1>Privacy Policy</h1>
<p class="meta">WorkTrail Recorder for iPhone &middot; Last updated %(updated)s</p>

<p>WorkTrail Recorder is published by TEK Digital Solutions ("we"). This policy explains what the app does with your information. The short version: the app has no account and no server of ours, and we do not collect your recordings, transcripts, location or usage data.</p>

<h2>Information we collect</h2>
<p>None. The app does not send us your recordings, transcripts, journal entries, saved places, location, contacts, identifiers or analytics. It contains no advertising and no tracking.</p>

<h2>Information stored on your iPhone</h2>
<ul>
<li><strong>Recordings and transcripts.</strong> Audio you record, the transcripts made from it, marks, clips and summaries are stored in the app's private storage on your iPhone.</li>
<li><strong>Journal entries and saved places.</strong> Notes you write and the places you save for reminders and recording rules.</li>
<li><strong>Location.</strong> If you allow it, the app uses your location on the device to tag recordings, centre the map, and notice when you arrive at or leave a place you armed. "Always" access is requested only when you arm a place. Location is not sent to us.</li>
<li><strong>Settings.</strong> Your preferences, theme and display density.</li>
</ul>
<p>This information leaves your iPhone only when you choose to share it, export it, or back it up to a folder you select in Files (for example iCloud Drive or another provider you use). Those providers handle the copy under their own terms.</p>

<h2>Connections the app makes</h2>
<p>The app works offline for recording and transcription. It connects to the internet only for these features:</p>
<ul>
<li><strong>Map tiles.</strong> The Automation map loads map images for the area you look at from OpenStreetMap (tile.openstreetmap.org) and, for satellite views, the U.S. Geological Survey (basemap.nationalmap.gov). Those services receive your IP address and which map tiles were requested.</li>
<li><strong>Address search.</strong> Searching for an address uses Apple Maps, which receives the text you type.</li>
<li><strong>Speech models.</strong> If you choose a larger transcription model, it is downloaded from huggingface.co, which receives your IP address. Your audio is never part of that request.</li>
<li><strong>Summaries.</strong> Optional summaries run on Apple's on-device model on supported iPhones.</li>
</ul>
<p>These services are operated by others under their own privacy policies. We receive nothing from them about you.</p>

<h2>Recording other people</h2>
<p>You decide what is recorded. Recording people can require their consent. You are responsible for telling people they are being recorded and for following the laws where you are.</p>

<h2>Children</h2>
<p>The app is not directed to children under 13 and we do not knowingly collect information from anyone.</p>

<h2>Deleting your information</h2>
<p>Deleting a recording in the app removes it from the iPhone. More, Settings, Backup + Reset, Clean-install reset erases everything the app stored. Deleting the app does the same. Copies you exported or backed up elsewhere are yours to remove.</p>

<h2>Changes to this policy</h2>
<p>If the app begins handling information differently, this page will be updated and the date above will change.</p>

<h2>Contact</h2>
<p>Questions about privacy: <a href="mailto:%(email)s">%(email)s</a>.</p>
</div></div>
''' % dict(email=EMAIL, updated=UPDATED)

TERMS = '''
<div class="doc"><div class="wrap">
<h1>Terms of Use</h1>
<p class="meta">WorkTrail Recorder for iPhone &middot; Last updated %(updated)s</p>

<p>These terms apply to your use of WorkTrail Recorder (the "app"), published by TEK Digital Solutions ("we"). By using the app you agree to them. If you obtained the app from the Apple App Store, Apple's Licensed Application End User License Agreement also applies; where the two differ on a point Apple's agreement requires, Apple's agreement governs.</p>

<h2>Licence</h2>
<p>We grant you a personal, non-transferable licence to use the app on Apple devices you own or control, as permitted by the App Store's usage rules. You may not resell the app, or use it to break the law.</p>

<h2>Your recordings and your responsibility</h2>
<ul>
<li>Recordings, transcripts and notes you make are yours.</li>
<li>Recording people can require their consent. You are solely responsible for telling people they are being recorded, for obtaining any consent the law requires, and for following the recording, privacy and workplace laws that apply to you.</li>
<li>You are responsible for how you store, share and back up what you record.</li>
</ul>

<h2>Transcripts and summaries</h2>
<p>Transcripts and summaries are produced automatically and can contain errors, omissions or words that were not said. Check them against the audio before relying on them. They are not a substitute for professional, legal, medical or safety records.</p>

<h2>Keeping your recordings safe</h2>
<p>Recordings are stored only on your iPhone unless you back them up. A recording can be lost if the device fails, runs out of storage, is reset, or the app is deleted, and a recording can be interrupted by calls, other apps or the system. Keep backups of anything you cannot afford to lose.</p>

<h2>Third-party services</h2>
<p>Map images, address search and optional model downloads are provided by others, as described in the <a href="../privacy/">privacy policy</a>. Their availability is outside our control. Open-source components used by the app are credited in the app.</p>

<h2>No warranty</h2>
<p>The app is provided "as is" and "as available", without warranties of any kind, to the fullest extent the law allows. We do not warrant that the app will be uninterrupted, error-free, or that any recording or transcript will be complete or accurate.</p>

<h2>Limitation of liability</h2>
<p>To the fullest extent the law allows, we are not liable for indirect, incidental, special or consequential damages, for lost data or recordings, or for claims arising from what you record or how you use it. Our total liability for any claim relating to the app is limited to the amount you paid for it.</p>

<h2>Changes</h2>
<p>We may update the app and these terms. The date above shows the latest version. Continuing to use the app after a change means you accept the updated terms.</p>

<h2>Contact</h2>
<p><a href="mailto:%(email)s">%(email)s</a></p>
</div></div>
''' % dict(email=EMAIL, updated=UPDATED)

page('index.html', 'WorkTrail Recorder — record, mark and transcribe on iPhone',
     'WorkTrail Recorder keeps a spoken record of your working day and transcribes it on your iPhone. No account, no cloud.', HOME, 'home')
page('support/index.html', 'Support — WorkTrail Recorder', 'Help and contact for WorkTrail Recorder for iPhone.', SUPPORT, 'support')
page('privacy/index.html', 'Privacy Policy — WorkTrail Recorder', 'What WorkTrail Recorder does with your information: nothing is collected.', PRIVACY, 'privacy')
page('terms/index.html', 'Terms of Use — WorkTrail Recorder', 'Terms of use for WorkTrail Recorder for iPhone.', TERMS, 'terms')
(ROOT / 'icon.svg').write_text(MARK.replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" '), encoding='utf-8', newline='\n')
(ROOT / '.nojekyll').write_text('', encoding='utf-8')
print('built')
