# -*- coding: utf-8 -*-
"""Gemeinsame Bausteine für die Clavis-IT-Service-Seiten."""
import html as _html

PHONE = "0162 63270 36"
TEL = "tel:+491626327036"
WA = "https://wa.me/491626327036"
MAIL = "kontakt@clavis-itservice.de"
SITE = "https://clavis-itservice.de"
ICONS_URL = "assets/img/icons.svg"
ASSET_V = "8"  # bei CSS-/JS-Änderungen erhöhen, damit Browser nicht die alte Version aus dem Cache nehmen

# ---------------------------------------------------------------- Icons
ICONS = {
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "chat": '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/><path d="M8 12h.01M12 12h.01M16 12h.01"/>',
    "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    "pin": '<path d="M20 10c0 4.99-5.54 10.19-7.4 11.8a1 1 0 0 1-1.2 0C9.54 20.19 4 14.99 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "arrow": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "plus": '<path d="M5 12h14"/><path d="M12 5v14"/>',
    "minus": '<path d="M5 12h14"/>',
    "menu": '<path d="M4 6h16M4 12h16M4 18h16"/>',
    "x": '<path d="M18 6 6 18M6 6l12 12"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2m-7.07-14.07 1.41 1.41m11.32 11.32 1.41 1.41M2 12h2m16 0h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/>',
    "moon": '<path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/>',
    "briefcase": '<path d="M16 20V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/><rect width="20" height="14" x="2" y="6" rx="2"/>',
    "home": '<path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
    "user": '<circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 0 0-16 0"/>',
    "user-plus": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M19 8v6M22 11h-6"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
    "monitor": '<rect width="20" height="14" x="2" y="3" rx="2"/><path d="M8 21h8M12 17v4"/>',
    "laptop": '<path d="M20 16V7a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v9m16 0H4m16 0 1.28 2.55a1 1 0 0 1-.9 1.45H3.62a1 1 0 0 1-.9-1.45L4 16"/>',
    "smartphone": '<rect width="14" height="20" x="5" y="2" rx="2"/><path d="M12 18h.01"/>',
    "tablet": '<rect width="16" height="20" x="4" y="2" rx="2"/><path d="M12 18h.01"/>',
    "wifi": '<path d="M12 20h.01M2 8.82a15 15 0 0 1 20 0M5 12.86a10 10 0 0 1 14 0M8.5 16.43a5 5 0 0 1 7 0"/>',
    "network": '<rect x="16" y="16" width="6" height="6" rx="1"/><rect x="2" y="16" width="6" height="6" rx="1"/><rect x="9" y="2" width="6" height="6" rx="1"/><path d="M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3"/><path d="M12 12V8"/>',
    "printer": '<path d="M6 9V2h12v7"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect width="12" height="8" x="6" y="14"/>',
    "tv": '<rect width="20" height="15" x="2" y="7" rx="2"/><path d="m17 2-5 5-5-5"/>',
    "plug": '<path d="M12 22v-5M9 8V2M15 8V2M18 8v5a4 4 0 0 1-4 4h-4a4 4 0 0 1-4-4V8Z"/>',
    "wrench": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    "cpu": '<rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2M15 20v2M2 15h2M2 9h2M20 15h2M20 9h2M9 2v2M9 20v2"/>',
    "sparkles": '<path d="M12 3l1.9 5.8L20 11l-6.1 2.2L12 19l-1.9-5.8L4 11l6.1-2.2Z"/><path d="M19 3v4M21 5h-4"/>',
    "gauge": '<path d="m12 14 4-4"/><path d="M3.34 19a10 10 0 1 1 17.32 0"/>',
    "refresh": '<path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"/><path d="M8 16H3v5"/>',
    "bug": '<path d="m8 2 1.88 1.88M14.12 3.88 16 2M9 7.13v-1a3 3 0 1 1 6 0v1"/><path d="M12 20c-3.3 0-6-2.7-6-6v-3a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v3c0 3.3-2.7 6-6 6M12 20v-9M6.53 9C4.6 8.8 3 7.1 3 5M6 13H2M3 21c0-2.1 1.7-3.9 3.8-4M20.97 5c0 2.1-1.6 3.8-3.5 4M22 13h-4M17.2 17c2.1.1 3.8 1.9 3.8 4"/>',
    "database": '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14a9 3 0 0 0 18 0V5"/><path d="M3 12a9 3 0 0 0 18 0"/>',
    "transfer": '<path d="M8 3 4 7l4 4M4 7h16M16 21l4-4-4-4M20 17H4"/>',
    "key": '<path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5"/>',
    "shield": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
    "lock": '<rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "cloud-mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    "heart": '<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>',
    "book": '<path d="M12 7v14M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"/>',
    "bag": '<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18M16 10a4 4 0 0 1-8 0"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20M2 12h20"/>',
    "file": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4M10 9H8M16 13H8M16 17H8"/>',
    "receipt": '<path d="M4 2v20l2-1 2 1 2-1 2 1 2-1 2 1 2-1 2 1V2l-2 1-2-1-2 1-2-1-2 1-2-1-2 1Z"/><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8M12 17.5v-11"/>',
    "truck": '<path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2M15 18H9M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.624l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/>',
    "clipboard": '<rect width="8" height="4" x="8" y="2" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="m9 14 2 2 4-4"/>',
    "calendar": '<rect width="18" height="18" x="3" y="4" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    "alert": '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4M12 17h.01"/>',
    "info": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>',
    "calculator": '<rect width="16" height="20" x="4" y="2" rx="2"/><path d="M8 6h8M16 14v4M16 10h.01M12 10h.01M8 10h.01M12 14h.01M8 14h.01M12 18h.01M8 18h.01"/>',
    "server": '<rect width="20" height="8" x="2" y="2" rx="2"/><rect width="20" height="8" x="2" y="14" rx="2"/><path d="M6 6h.01M6 18h.01"/>',
    "download": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m7 10 5 5 5-5"/><path d="M12 15V3"/>',
    "eye": '<path d="M2.06 12.35a1 1 0 0 1 0-.7 10.75 10.75 0 0 1 19.88 0 1 1 0 0 1 0 .7 10.75 10.75 0 0 1-19.88 0"/><circle cx="12" cy="12" r="3"/>',
    "headset": '<path d="M3 11h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-5Zm0 0a9 9 0 1 1 18 0m0 0v5a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3Z"/><path d="M21 16v2a4 4 0 0 1-4 4h-5"/>',
    "message": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "search": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "camera": '<path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3"/>',
    "cookie-off": '<path d="M12 2a10 10 0 1 0 10 10 4 4 0 0 1-5-5 4 4 0 0 1-5-5"/><path d="M8.5 8.5v.01M16 15.5v.01M12 12v.01M11 17v.01M7 14v.01"/>',
    "thumbs": '<path d="M7 10v12M15 5.88 14 10h5.83a2 2 0 0 1 1.92 2.56l-2.33 8A2 2 0 0 1 17.5 22H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h2.76a2 2 0 0 0 1.79-1.11L12 2a3.13 3.13 0 0 1 3 3.88Z"/>',
}


def write_icons(path):
    parts = ['<svg xmlns="http://www.w3.org/2000/svg">']
    for name, body in ICONS.items():
        parts.append(f'<symbol id="i-{name}" viewBox="0 0 24 24">{body}</symbol>')
    parts.append('</svg>\n')
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("".join(parts))


def ic(name, cls=""):
    assert name in ICONS, name
    c = f"icon {cls}".strip()
    return f'<svg class="{c}" aria-hidden="true"><use href="{ICONS_URL}#i-{name}"/></svg>'


def esc(s):
    return _html.escape(s, quote=True)


# ---------------------------------------------------------------- Bausteine
def btn_call(size="btn-lg", label=None, cls="btn-primary"):
    text = label or PHONE
    aria = f' aria-label="Anrufen: {PHONE}"' if label is None else ""
    return f'<a class="btn {cls} {size}" href="{TEL}"{aria}>{ic("phone")}{text}</a>'


def btn_wa(size="btn-lg", label="Per WhatsApp schreiben", cls="btn-outline"):
    return f'<a class="btn {cls} {size}" href="{WA}" rel="noopener">{ic("chat")}{label}</a>'


def btn_mail(size="btn-lg", label="E-Mail schreiben", cls="btn-outline", subject=None):
    href = f"mailto:{MAIL}" + (f"?subject={subject}" if subject else "")
    return f'<a class="btn {cls} {size}" href="{href}">{ic("mail")}{label}</a>'


def link(href, text, cls="btn-link"):
    return f'<a class="{cls}" href="{href}">{text}{ic("arrow", "icon-arrow")}</a>'


def btn(href, text, cls="btn-outline", size="btn-lg", icon=None, arrow=False):
    i = ic(icon) if icon else ""
    a = ic("arrow", "icon-arrow") if arrow else ""
    return f'<a class="btn {cls} {size}" href="{href}">{i}{text}{a}</a>'


def qr_card(label="Scannen und direkt anrufen", badge="Telefonisch täglich 8–20 Uhr"):
    b = f'<span class="status-badge"><i></i>{badge}</span>' if badge else ""
    return f'''<aside class="qr-card reveal" aria-label="Telefonnummer als QR-Code">
        <div class="qr"><img src="assets/img/qr-anrufen.svg" width="148" height="148" alt="QR-Code: Clavis IT Service anrufen, {PHONE}"></div>
        <p class="qr-label">{label}</p>
        <a class="qr-phone" href="{TEL}">{PHONE}</a>
        {b}
      </aside>'''


def section_head(eyebrow, title, lead=None, left=False, hid=None, tag="h2"):
    cls = "section-head section-head-left" if left else "section-head"
    idattr = f' id="{hid}"' if hid else ""
    e = f'<p class="eyebrow reveal">{eyebrow}</p>' if eyebrow else ""
    l = f'<p class="section-lead reveal">{lead}</p>' if lead else ""
    return f'<div class="{cls}">{e}<{tag}{idattr} class="reveal">{title}</{tag}>{l}</div>'


def cards(items, grid="grid-3", compact=False, hover=True, h="h3"):
    cls = "card" + (" card-compact" if compact else "") + (" card-hover" if hover else "")
    out = [f'<div class="{grid}">']
    for it in items:
        icon, title, text = it[0], it[1], it[2]
        extra = it[3] if len(it) > 3 else ""
        idattr = f' id="{it[4]}"' if len(it) > 4 and it[4] else ""
        out.append(f'''<article class="{cls} reveal"{idattr}>
          <span class="card-icon">{ic(icon)}</span>
          <{h}>{title}</{h}>
          <p>{text}</p>{extra}
        </article>''')
    out.append("</div>")
    return "\n".join(out)


def steps3(items):
    out = ['<ol class="steps steps-3" data-reveal-line>']
    for i, (t, p) in enumerate(items, 1):
        out.append(f'<li class="reveal"><span class="step-num" aria-hidden="true">{i:02d}</span><h3>{t}</h3><p>{p}</p></li>')
    out.append("</ol>")
    return "\n".join(out)


def steps_v(items):
    out = ['<ol class="steps-v">']
    for i, it in enumerate(items, 1):
        t, ps = it[0], it[1:]
        body = "".join(p if p.startswith("<") else f"<p>{p}</p>" for p in ps)
        out.append(f'<li class="reveal"><span class="step-num" aria-hidden="true">{i:02d}</span><div><h3>{t}</h3>{body}</div></li>')
    out.append("</ol>")
    return "\n".join(out)


def checklist(items, cls="checklist"):
    return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def faq(eyebrow, title, lead, items, sid="faq", alt=False):
    q = []
    for question, answer in items:
        paras = answer if isinstance(answer, list) else [answer]
        body = "".join(f"<p>{p}</p>" for p in paras)
        q.append(f'<details class="faq reveal"><summary>{question}{ic("plus")}</summary><div class="faq-body">{body}</div></details>')
    cls = "section section-alt" if alt else "section"
    return f'''<section class="{cls}" id="{sid}" aria-labelledby="{sid}-title">
    <div class="container faq-wrap">
      {section_head(eyebrow, title, lead, left=True, hid=sid + "-title")}
      <div class="faq-list">{"".join(q)}</div>
    </div>
  </section>'''


def note(icon, title, text, warn=False, extra=""):
    cls = "note note-warn reveal" if warn else "note reveal"
    paras = text if isinstance(text, list) else [text]
    body = "".join(f"<p>{p}</p>" for p in paras)
    t = f"<h3>{title}</h3>" if title else ""
    return f'<div class="{cls}">{ic(icon)}<div>{t}{body}{extra}</div></div>'


FERNWARTUNG_WARN = note(
    "alert", "Wichtig zum Thema Fernwartung",
    ["Ich rufe nie unaufgefordert an. Meldet sich jemand so bei Ihnen{team}, beenden Sie das Gespräch bitte sofort.",
     'Haben wir eine Fernwartung vereinbart? <a href="fernwartung.html">Hier starten Sie sie.</a>'],
    warn=True)


def fern_warn(team=False):
    return FERNWARTUNG_WARN.replace("{team}", " oder im Team" if team else "")


AREA_TEXT = ("Vor Ort in Mannheim und Umgebung: Viernheim, Ilvesheim, Heddesheim, Ladenburg, Edingen-Neckarhausen, "
             "Schriesheim, Hirschberg, Weinheim, Hemsbach, Laudenbach, Heppenheim, Bensheim und Heidelberg.")


def cta_band(title, text, links="", area=False, qr_label="Scannen und anrufen", extra_btn=""):
    a = f'<p class="cta-area">{AREA_TEXT}</p>' if area else ""
    return f'''<section class="cta-band" aria-labelledby="cta-title">
    <div class="container">
      <div class="cta-box reveal">
        <div>
          <h2 id="cta-title">{title}</h2>
          <p>{text}</p>
          <div class="btn-row">{btn_call()}{extra_btn}{links}</div>
          {a}
        </div>
        <div class="cta-qr">
          <div class="qr"><img src="assets/img/qr-anrufen.svg" width="130" height="130" alt="QR-Code: anrufen unter {PHONE}" loading="lazy"></div>
          <p class="qr-label">{qr_label}</p>
          <a class="qr-phone" href="{TEL}">{PHONE}</a>
        </div>
      </div>
    </div>
  </section>'''


TOWNS = ["Mannheim", "Viernheim", "Ilvesheim", "Heddesheim", "Ladenburg", "Edingen-Neckarhausen", "Schriesheim",
         "Hirschberg", "Weinheim", "Hemsbach", "Laudenbach", "Heppenheim", "Bensheim", "Heidelberg"]


def town_chips():
    return '<ul class="chips reveal" aria-label="Orte im Einsatzgebiet">' + "".join(
        f'<li class="chip">{ic("pin")}{t}</li>' for t in TOWNS) + "</ul>"


def area_svg():
    # Lage relativ zu Mannheim-Käfertal, 8 px je km (25 km = 200 px)
    pts = [  # name, x, y, label?, anchor
        ("Mannheim", 191, 238, True, "end"), ("Viernheim", 257, 193, True, "start"),
        ("Ilvesheim", 250, 250, False, ""), ("Heddesheim", 271, 222, False, ""),
        ("Ladenburg", 274, 251, True, "start"), ("Edingen-Neckarhausen", 268, 266, False, ""),
        ("Schriesheim", 305, 249, False, ""), ("Hirschberg", 304, 222, False, ""),
        ("Weinheim", 308, 184, True, "start"), ("Hemsbach", 298, 146, True, "start"),
        ("Laudenbach", 298, 126, False, ""), ("Heppenheim", 291, 100, True, "start"),
        ("Bensheim", 281, 66, True, "start"), ("Heidelberg", 322, 315, True, "start"),
    ]
    dots, labels = [], []
    for n, x, y, show, anchor in pts:
        dots.append(f'<circle class="dot" cx="{x}" cy="{y}" r="3.2"/>')
        if show:
            dx = -8 if anchor == "end" else 8
            labels.append(f'<text x="{x + dx}" y="{y + 4}" text-anchor="{anchor}">{n}</text>')
    return f'''<figure class="radius reveal" role="img" aria-label="Einsatzgebiet: von Mannheim-Käfertal aus bis 10 und bis 25 Kilometer Umkreis, von Viernheim und Ladenburg über Heidelberg bis Weinheim, Heppenheim und Bensheim.">
      <svg viewBox="0 0 440 440" aria-hidden="true">
        <circle class="zone-25" cx="220" cy="220" r="200"/>
        <circle class="ring" cx="220" cy="220" r="200"/>
        <circle class="zone-10" cx="220" cy="220" r="80"/>
        <circle class="ring" cx="220" cy="220" r="80"/>
        <text class="km" x="220" y="132" text-anchor="middle">10 km</text>
        <text class="km" x="220" y="14" text-anchor="middle">25 km</text>
        {"".join(dots)}
        {"".join(labels)}
        <circle class="pulse" cx="220" cy="220" r="7"/>
        <circle class="center" cx="220" cy="220" r="7"/>
        <text class="center-label" x="212" y="206" text-anchor="end">Käfertal</text>
      </svg>
    </figure>'''


def photo(label, cls="media", icon="camera", note_text="Foto folgt"):
    # Platzhalter mit fester Fläche: Bild später als <img> mit width/height einsetzen.
    return f'''<div class="{cls} reveal">
      <!-- FOTO: hier <img src="assets/img/..." alt="{esc(label)}" width="..." height="..." loading="lazy"> einsetzen und .ph entfernen -->
      <div class="ph" aria-hidden="true">{ic(icon)}<span>{note_text}<br>{label}</span></div>
    </div>'''


def img(name, alt, sizes="(min-width: 960px) 50vw, 100vw", eager=False, pos=None):
    """Responsives Foto aus assets/img/fotos/<name>-800.webp und -1600.webp (Seitenverhältnis 3:2)."""
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    if pos:
        load += f' style="object-position:{pos}"'
    return (f'<img src="assets/img/fotos/{name}-800.webp" '
            f'srcset="assets/img/fotos/{name}-800.webp 800w, assets/img/fotos/{name}-1600.webp 1600w" '
            f'sizes="{sizes}" width="1600" height="1066" alt="{esc(alt)}" {load} decoding="async">')


def media(name, alt, cls="media", sizes="(min-width: 960px) 50vw, 100vw", pos=None):
    return f'<div class="{cls} reveal">{img(name, alt, sizes, pos=pos)}</div>'


# ---------------------------------------------------------------- Layout
NAV = [("index.html", "Start"), ("geschaeftskunden.html", "Unternehmen"), ("leistungen.html", "Privatkunden"),
       ("preise.html", "Preise"), ("ueber-mich.html", "Über mich"), ("kontakt.html", "Kontakt")]

BRAND = '''<svg class="brand-mark" viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="8"/><circle cx="12" cy="16" r="5" fill="none" stroke="#FFC48C" stroke-width="2.6"/><path d="M17 16h9M22.5 16v4M26 16v3" fill="none" stroke="#FFC48C" stroke-width="2.6" stroke-linecap="round"/></svg>
      <span class="brand-text"><span class="brand-name">Clavis <span>IT Service</span></span><span class="brand-claim">Zuverlässig · Vor Ort</span></span>'''

THEME_BOOT = ("<script>(function(){try{var t=localStorage.getItem('clavis-theme');"
              "if(t==='dark'||t==='light')document.documentElement.setAttribute('data-theme',t);}catch(e){}})();</script>")


def header(active):
    items = "".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a></li>' for h, t in NAV)
    return f'''<header class="site-header" data-header>
  <div class="container header-inner">
    <a class="brand" href="index.html" aria-label="Clavis IT Service – zur Startseite">
      {BRAND}
    </a>
    <nav class="nav" id="site-nav" aria-label="Hauptnavigation" data-nav>
      <ul class="nav-list">{items}</ul>
      <div class="nav-extra">{btn_call("btn-lg", f"Anrufen: {PHONE}")}{btn_wa("btn-lg", "WhatsApp schreiben")}</div>
    </nav>
    <div class="header-actions">
      <button class="icon-btn theme-toggle" type="button" data-theme-toggle aria-label="Dunkle Darstellung aktivieren">
        {ic("moon", "i-moon")}{ic("sun", "i-sun")}
      </button>
      <a class="btn btn-primary btn-sm header-phone" href="{TEL}">{ic("phone")}{PHONE}</a>
      <button class="icon-btn nav-toggle" type="button" aria-controls="site-nav" aria-expanded="false" aria-label="Menü öffnen" data-nav-toggle>
        {ic("menu", "i-open")}{ic("x", "i-close")}
      </button>
    </div>
  </div>
</header>'''


def footer():
    nav = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)
    return f'''<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <a class="brand" href="index.html" aria-label="Clavis IT Service – zur Startseite">
        {BRAND}
      </a>
      <p>Persönlicher IT-Service für Privathaushalte und Unternehmen in Mannheim und Umgebung.</p>
    </div>
    <div>
      <p class="footer-title">Kontakt</p>
      <ul class="footer-contact">
        <li>{ic("phone")}<a href="{TEL}">{PHONE}</a></li>
        <li>{ic("chat")}<a href="{WA}" rel="noopener">WhatsApp schreiben</a></li>
        <li>{ic("mail")}<a href="mailto:{MAIL}">{MAIL}</a></li>
        <li>{ic("pin")}<span>Mannheimer Straße 57a<br>68309 Mannheim</span></li>
        <li>{ic("clock")}<span>Telefonisch täglich 8 bis 20 Uhr,<br>Termine nach Vereinbarung</span></li>
      </ul>
    </div>
    <nav aria-label="Seiten">
      <p class="footer-title">Seiten</p>
      <ul class="footer-links">{nav}</ul>
    </nav>
    <nav aria-label="Service und Rechtliches">
      <p class="footer-title">Service</p>
      <ul class="footer-links">
        <li><a href="fernwartung.html">{ic("headset")}Fernwartung starten</a></li>
        <li><a href="impressum.html">Impressum</a></li>
        <li><a href="datenschutz.html">Datenschutz</a></li>
      </ul>
    </nav>
  </div>
  <div class="container footer-bottom">
    <span>© <span data-year>2026</span> Clavis IT Service · Eymen Kumaru</span>
    <span>{ic("shield")}Diese Website setzt keine Cookies und verwendet keine Analyse-Werkzeuge.</span>
  </div>
</footer>'''


def page(filename, title, desc, body, active=None, extra_head="", noindex=False):
    canon = SITE + "/" + ("" if filename == "index.html" else filename)
    robots = '\n  <meta name="robots" content="noindex, follow">' if noindex else ""
    return f'''<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">{robots}
  <link rel="canonical" href="{canon}">
  <meta name="theme-color" content="#FFFFFF" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#14213D" media="(prefers-color-scheme: dark)">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="de_DE">
  <meta property="og:site_name" content="Clavis IT Service">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:url" content="{canon}">
  <link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
  <link rel="preload" href="assets/fonts/inter-latin-wght.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="assets/fonts/space-grotesk-latin-wght.woff2" as="font" type="font/woff2" crossorigin>
  {THEME_BOOT}
  <link rel="stylesheet" href="assets/css/styles.css?v={ASSET_V}">
  <script src="assets/js/main.js?v={ASSET_V}" defer></script>{extra_head}
</head>
<body>
<a class="skip-link" href="#main">Zum Inhalt springen</a>
{header(active or filename)}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>
'''
