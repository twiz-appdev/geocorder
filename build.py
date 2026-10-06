"""Builds the GeoCorder site: python build.py writes the four pages next to this file."""
import pathlib

ROOT = pathlib.Path(__file__).parent
EMAIL = 'tekdigitalsolutionsllc@gmail.com'
UPDATED = 'October 6, 2026'
# App Store link for the home page button; empty until GeoCorder is on the store.
STORE_URL = ''

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
<link rel="icon" href="%(depth)sicon.png" type="image/png">
<link rel="apple-touch-icon" href="%(depth)sicon.png">
</head>
<body>
<header class="site-header"><div class="wrap">
<a class="brand" href="%(home)s"><img src="%(depth)sicon.png" alt="" width="30" height="30" style="border-radius:7px"><span>GEOCORDER</span></a>
<nav class="nav" aria-label="Site">%(nav)s</nav>
</div></header>
<main>
%(body)s
</main>
<footer class="site-footer"><div class="wrap">
<span>&copy; 2026 John Gunderson, d/b/a TEK Digital Solutions. GeoCorder for iPhone.<br><small>Apple, iPhone, Apple Intelligence, Apple Maps, Siri, iCloud and App Store are trademarks of Apple Inc., registered in the U.S. and other countries. iOS is a trademark or registered trademark of Cisco in the U.S. and other countries and is used under license.</small></span>
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
<h1>Automate. Record.<br>Transcribe.</h1>
<p class="lead">GeoCorder keeps a spoken record of your day, marks the moments that matter, and turns speech into text on your iPhone. No account needed. No GeoCorder server.</p>
''' + (('<a class="cta" href="%s">Download on the App Store</a>' % STORE_URL) if STORE_URL else '<span class="cta" aria-disabled="true">GeoCorder for iPhone</span>') + '''
''' + wave() + '''
</div></div>

<section id="features"><div class="wrap">
<h2>Built for long days</h2>
<p class="sub">Start it when your work begins and stop it when you are done. A call or another app can pause a recording; GeoCorder tries to pick it back up and tells you if it cannot.</p>
<div class="grid">
''' + ''.join([
    card('RECORD', 'All-day recording', 'Sessions split into clips on a schedule you choose and keep recording with the screen off. A notification and Live Activity show whenever GeoCorder is recording.'),
    card('MARK', 'Mark the moment', 'One tap marks what was just said. Save a clip, or save the last few minutes after something worth keeping.'),
    card('TRANSCRIBE', 'Transcripts on the device', 'Speech becomes text on your iPhone with a built-in speech model; larger models are optional downloads. Quiet speech is brought up to a clear level first, and you get a cleaned copy next to the raw one.'),
    card('READ', 'Search, correct, share', 'Read along with the audio, search across transcripts, fix a passage, and share the text with or without the recording.'),
    card('AUTOMATE', 'Recording by place', 'When you arrive at, stay at, or leave a place you save, GeoCorder starts recording if it is open, or sends a notification you tap to start. Arm and disarm each place with a switch.'),
    card('ROUTINES', 'Routines for your places', 'Reminders when you arrive, leave or stay a while, with Done, Snooze and quick-note buttons, plus a log of your time at each place. Start from a ready-made example or build your own.'),
]) + '''
</div>
</div></section>

<section class="privacy-band"><div class="wrap">
<h2>Private by design</h2>
<p class="sub">A recorder hears everything, so it should keep it to itself.</p>
<div class="grid">
''' + ''.join([
    card('NO ACCOUNT', 'No GeoCorder account', 'There is no GeoCorder account and no GeoCorder server. Signing in to Google is optional and only for backup to your own Google Drive.'),
    card('ON DEVICE', 'Audio is never uploaded for transcription', 'Recordings and transcripts are stored on your iPhone, and transcription runs there. Your audio leaves the iPhone only in backups you set up (a folder in Files or your own Google Drive) or when you share it.'),
    card('NO TRACKING', 'No analytics, no ads', 'The app does not collect usage data, does not track you, and shows no advertising.'),
]) + '''
</div>
<p class="sub" style="margin-top:24px">The full details are in the <a href="privacy/">privacy policy</a>.</p>
</div></section>

'''

FAQ = [
    ('Do I need an account?', 'No. There is no GeoCorder account, and the app works as soon as you allow the microphone. Signing in to Google is optional and only for backup to your own Google Drive.'),
    ('Does recording keep going when the screen is off?', 'Yes. Recording continues in the background, and a notification and Live Activity show that it is running. A phone call or another app taking over audio pauses it. GeoCorder tries to resume when the interruption ends; if it cannot, it shows a notification and resumes when you tap it or return to the app.'),
    ('How do I get a transcript?', 'Open a recording, tap Speech, then Transcribe. A speech model is built in. Transcription happens on your iPhone and can take a while for long recordings.'),
    ('The transcript missed words. What can I do?', 'Choose a larger model under More, Settings, Transcription, Model / quality (Balanced or Accurate catch more than Fast), then run a new pass on the recording. Keeping the phone closer to the speaker helps the most.'),
    ('Where are my recordings stored?', 'On your iPhone, inside the app. They are included in your iPhone backup (iCloud Backup or a computer backup) if you use one. To keep a separate copy, open Backup &amp; Restore and choose a folder in Files, such as iCloud Drive, or sign in with Google to back up to your own Google Drive. Backups go only where you choose.'),
    ('How does recording by place work?', 'In Automation, save a place, choose whether arriving, staying or leaving should start a recording, and arm it. The app asks for Always location access so it can notice this while closed. If GeoCorder is open the recording starts; otherwise you get a notification with a Start Recording button, because iPhone does not let apps switch the microphone on in the background. iPhone watches up to 20 armed places at once.'),
    ('How do I delete everything?', 'More, Settings, Backup + Reset, Open backup + reset center, Prepare clean-install reset (you type a confirmation phrase) erases the recordings, transcripts, journal, places, routines and settings the app stored on the iPhone, and signs GeoCorder out of Google. Deleting the app erases the same things; if you install it again, it starts signed out. Copies in your backup folder or your Google Drive, in an iPhone or iCloud backup, or that you shared are not removed, and neither are Calendar events and reminders your routines added or anything already sent to your own server.'),
    ('Can it record phone calls?', 'No. iPhone does not allow apps to record calls, and GeoCorder does not try to.'),
]

SUPPORT = '''
<div class="doc"><div class="wrap">
<h1>Support</h1>
<p class="meta">Help with GeoCorder for iPhone.</p>
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
<p class="meta">GeoCorder for iPhone &middot; Last updated %(updated)s</p>

<p>GeoCorder is published by John Gunderson, doing business as TEK Digital Solutions ("we"). The short version: there is no GeoCorder account and no server of ours, and the app sends us nothing. Your recordings, transcripts, journal, places and location are kept on your iPhone. They leave it only in the ways listed below, each of which you choose: backups, sharing, Apple Maps lookups, and routines that add to Calendar or Reminders or tell your own server.</p>

<h2>What is stored on your iPhone</h2>
<p>Recordings, transcripts, marks, summaries, journal entries, saved places, routines, a log of your visits, an activity history and your settings are stored in the app on your iPhone. Transcription and summaries run on the iPhone. If you allow location, recordings and marked moments are tagged with where they were made (you can turn this off), and places you arm can start a recording or run the routines you set up for them. Reminders and the recording indicator can show titles and place names on the Lock Screen.</p>
<p>Copies leave your iPhone only when you:</p>
<ul>
<li>share or export something;</li>
<li>back up to a folder you choose in Files or to your own Google Drive, by hand or after you leave a place if a routine you set up asks for it;</li>
<li>switch on a routine that adds a visit to Calendar, adds a reminder to Reminders, or tells your own server;</li>
<li>use your iPhone's own iCloud or computer backup, which includes the app (you can turn this off in Backup &amp; Restore).</li>
</ul>

<h2>Connections the app makes</h2>
<ul>
<li><strong>Apple Maps.</strong> The map, address search and address lookup use Apple Maps, so Apple receives the area being shown, what you type and the coordinates looked up. A Directions button opens the Apple Maps app.</li>
<li><strong>Google Drive (optional).</strong> If you sign in with Google in Backup &amp; Restore, GeoCorder uploads your backups (recordings, transcripts and the rest of each session) to a GeoCorder folder in your own Google Drive, when you back up or after you leave a place if a routine asks for it. Google receives your sign-in and those files. GeoCorder asks only for access to files it creates, so it cannot see the rest of your Drive, and it keeps your Google email address on the iPhone to show which account is signed in. We never receive any of it. Signing out, or the clean-install reset, removes the sign-in from your iPhone.</li>
<li><strong>Calendar and Reminders (optional).</strong> A routine you switch on can add a visit to your default calendar (the place name or address, and your arrival and leaving times) or add its reminder text to your default Reminders list. iPhone asks for access first. From there they sync wherever that calendar or list syncs, such as iCloud, Google or a work account, and anyone you share it with can see them.</li>
<li><strong>Your own server (optional, off by default).</strong> If you set up &ldquo;Tell my own server&rdquo; in a routine, GeoCorder sends the place name, the event (arrive, stay or leave) and the times to the https address you enter, including while the app is in the background. That server is yours or one you choose; nothing reaches us.</li>
<li><strong>Siri and Shortcuts.</strong> If you use GeoCorder with Siri or the Shortcuts app (for example to start recording or add a journal note), Apple handles your request under its own privacy policy; the action itself runs in the app on your iPhone.</li>
<li><strong>Links, Messages and shortcuts from routines.</strong> A routine's notification can offer a button that opens a link you entered, Messages with your text filled in (you tap Send), or a shortcut you named. What happens next is up to that website or app.</li>
<li><strong>Speech models.</strong> Larger transcription models you choose download from huggingface.co, which receives your IP address. Your audio is never sent.</li>
</ul>
<p>These services follow their own privacy policies. No analytics, advertising or tracking is built into the app.</p>

<h2>If you email us</h2>
<p>We receive your email address and what you send, including any report you attach from More, Diagnostics (these can include saved place names, your device model and your microphone's name, but no audio, transcript text or coordinates). Our email is hosted by Google (Gmail). We use it only to help you, keep it for up to 24 months, and delete it sooner if you ask. We do not sell or share personal information. If you are in the EU or UK you may also contact your data protection authority.</p>

<h2>This website</h2>
<p>This site is hosted on GitHub Pages, which receives visitors' IP addresses. It uses no cookies or analytics, so Do Not Track signals change nothing.</p>

<h2>Children</h2>
<p>The app is not directed to children under 13 and collects no information from anyone. If a child under 13 has emailed us, we will delete the message.</p>

<h2>Deleting your information</h2>
<p>Deleting a recording removes it from the iPhone. The clean-install reset (More, Settings, Backup + Reset) erases everything the app stored on the iPhone: recordings, transcripts, marks, summaries, the journal, places, routines, the visit log, the activity history and settings. It also signs GeoCorder out of Google. Deleting the app erases the same things; iPhone may keep the Google sign-in after the app is deleted, but GeoCorder removes it the first time it opens if you install it again. What already left the iPhone stays where it went: copies in your backup folder or Google Drive, in an iPhone or iCloud backup, or that you shared; Calendar events and reminders your routines added; and anything sent to your own server. Those are yours to remove.</p>

<h2>Changes and contact</h2>
<p>If the app starts handling information differently, this page and the date above will change first. Questions: <a href="mailto:%(email)s">%(email)s</a>.</p>
</div></div>
''' % dict(email=EMAIL, updated=UPDATED)

TERMS = '''
<div class="doc"><div class="wrap">
<h1>Terms of Use</h1>
<p class="meta">GeoCorder for iPhone &middot; Last updated %(updated)s</p>

<p>GeoCorder (the "app") is published by John Gunderson, doing business as TEK Digital Solutions ("we", "us"). The licence for the app is Apple's Licensed Application End User License Agreement (the standard App Store licence). These terms add to it; they are between you and us, not Apple. Where these terms and Apple's licence differ, Apple's licence governs. By downloading or using the app you agree to both.</p>

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
<p>Maps, address search, optional model downloads, Google Drive backup, Apple Calendar, Reminders, Siri and Shortcuts are provided by others, as described in the <a href="../privacy/">privacy policy</a>. Their availability is outside our control. Addresses you enter for &ldquo;Tell my own server&rdquo; or &ldquo;Open a link&rdquo; are yours: we do not run or see them, and you are responsible for what you send there. Open-source components used by the app are listed, with their licences, under More, About in the app.</p>

<h2>No warranty</h2>
<p>The app is provided "as is" and "as available", without warranties of any kind, to the fullest extent the law allows. We do not warrant that the app will be uninterrupted, error-free, or that any recording or transcript will be complete or accurate.</p>

<h2>Support</h2>
<p>We, not Apple, are responsible for the app and for supporting it. Contact us at the address below.</p>

<h2>Limitation of liability</h2>
<p>To the fullest extent the law allows, we are not liable for indirect, incidental, special or consequential damages, or for lost data or recordings, and we are not responsible for claims arising from what you record or how you use the app. Our total liability for all claims relating to the app will not exceed the greater of the amount you paid for the app and US$50. These limits do not apply to liability for death or personal injury caused by our negligence, for fraud, for our intentional or grossly negligent misconduct, or to any other liability that cannot be limited under the law that applies to you. Nothing in these terms removes rights you have under consumer law that cannot be excluded.</p>

<h2>Apple</h2>
<p>Apple is not responsible for the app or its content and has no obligation to provide maintenance or support for it. If the app fails to conform to any applicable warranty, you may notify Apple, and Apple will refund the purchase price; to the maximum extent the law allows, Apple has no other warranty obligation for the app. We, not Apple, are responsible for addressing any claims relating to the app, including product liability claims, claims that the app fails to meet legal or regulatory requirements, consumer-protection or privacy claims, and claims that the app infringes someone else's intellectual property. You confirm that you are not located in a country subject to a US Government embargo or designated by the US Government as a "terrorist supporting" country, and that you are not on any US Government list of prohibited or restricted parties. Apple and its subsidiaries are third-party beneficiaries of these terms and may enforce them against you.</p>

<h2>Governing law</h2>
<p>These terms are governed by the laws of the State of Wisconsin, USA. Any dispute we cannot settle informally will be heard in the state or federal courts for Polk County, Wisconsin, except that either of us may bring an individual claim in small-claims court. If you live outside the United States, you keep any protection your local law gives you that cannot be waived.</p>

<h2>Changes</h2>
<p>We may update the app and these terms. Updated terms apply from the date shown above and only to use of the app after that date; they do not apply to a dispute that arose before they were posted. If you do not agree to updated terms, stop using the app. If any part of these terms is found unenforceable, the rest remains in effect.</p>

<h2>Contact</h2>
<p><a href="mailto:%(email)s">%(email)s</a></p>
</div></div>
''' % dict(email=EMAIL, updated=UPDATED)

page('index.html', 'GeoCorder — record, mark and transcribe on iPhone',
     'GeoCorder keeps a spoken record of your working day and transcribes it on your iPhone. No account, no GeoCorder server.', HOME, 'home')
page('support/index.html', 'Support — GeoCorder', 'Help and contact for GeoCorder for iPhone.', SUPPORT, 'support')
page('privacy/index.html', 'Privacy Policy — GeoCorder', 'What GeoCorder does with your information: the app sends nothing to us, and your recordings go only where you choose.', PRIVACY, 'privacy')
page('terms/index.html', 'Terms of Use — GeoCorder', 'Terms of use for GeoCorder for iPhone.', TERMS, 'terms')
(ROOT / 'icon.svg').write_text(MARK.replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" '), encoding='utf-8', newline='\n')
(ROOT / '.nojekyll').write_text('', encoding='utf-8')
print('built')
