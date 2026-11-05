# -*- coding: utf-8 -*-
from core import *

# ======================================================================= START
JSONLD = '''
  <script type="application/ld+json">{"@context":"https://schema.org","@type":"LocalBusiness","name":"Clavis IT Service","description":"Persönlicher IT-Service für Privathaushalte, Senioren und kleine Unternehmen in Mannheim und Umgebung.","url":"https://clavis-itservice.de/","telephone":"+49 162 6327036","email":"kontakt@clavis-itservice.de","founder":{"@type":"Person","name":"Eymen Kumaru"},"address":{"@type":"PostalAddress","streetAddress":"Mannheimer Straße 57a","postalCode":"68309","addressLocality":"Mannheim","addressCountry":"DE"},"openingHours":"Mo-Su 08:00-20:00","areaServed":["Mannheim","Viernheim","Ilvesheim","Heddesheim","Ladenburg","Edingen-Neckarhausen","Schriesheim","Hirschberg","Weinheim","Hemsbach","Laudenbach","Heppenheim","Bensheim","Heidelberg"]}</script>'''

index_body = f'''
  <section class="page-hero" aria-labelledby="hero-title">
    <div class="container hero-grid">
      <div>
        <p class="eyebrow reveal">IT-Service · Zuverlässig · Vor Ort</p>
        <h1 id="hero-title" class="reveal">IT-Service in Mannheim.<span class="hero-sub"><span class="mark">Bei Ihnen vor Ort oder per Fernwartung.</span></span></h1>
        <p class="hero-lead reveal">Clavis IT Service: persönliche IT-Betreuung für Privathaushalte, Senioren und kleine Unternehmen.</p>
        <div class="btn-row reveal">{btn_call()}{btn_wa(label="Schreiben")}</div>
      </div>
      {hero_aside()}
    </div>
  </section>

  <section class="section" aria-labelledby="wer-title">
    <div class="container">
      {section_head("Ihr Weg zu mir", "Für wen suchen Sie Unterstützung?", hid="wer-title")}
      <div class="grid-2">
        <article class="card card-hover audience reveal">
          <div class="card-media">{img("unternehmen-support", "IT-Unterstützung an einem Büroarbeitsplatz", "(min-width: 720px) 50vw, 100vw")}</div>
          <span class="card-icon">{ic("briefcase")}</span>
          <h3>Unternehmen</h3>
          <p>Für Praxen, Büros, Handwerk und Betriebe bis 10 Mitarbeiter: Arbeitsplätze, Netzwerk, Microsoft 365 und Datensicherung.</p>
          {btn("geschaeftskunden.html", "Weiter als Unternehmen", "btn-primary", arrow=True)}
        </article>
        <article class="card card-hover audience reveal">
          <div class="card-media">{img("privat-laptop", "Älteres Ehepaar schaut im Wohnzimmer gemeinsam auf einen Laptop", "(min-width: 720px) 50vw, 100vw")}</div>
          <span class="card-icon">{ic("home")}</span>
          <h3>Privatkunden</h3>
          <p>Für Privathaushalte und Senioren: Computer, Smartphone, WLAN, Drucker und Smart-TV, direkt bei Ihnen zu Hause.</p>
          {btn("leistungen.html", "Weiter als Privatkunde", "btn-primary", arrow=True)}
        </article>
      </div>
      <div class="coral-strip on-coral reveal">
        <p><strong>Nicht sicher, was passt?</strong>Rufen Sie an: <a href="{TEL}" class="nowrap">{PHONE}</a> oder schreiben Sie per WhatsApp.</p>
        <div class="btn-row">{btn_call("btn-lg", "Anrufen")}{btn_wa(label="WhatsApp")}</div>
      </div>
    </div>
  </section>

  <section class="section section-alt" aria-labelledby="person-title">
    <div class="container person">
      {portrait()}
      <div>
        <p class="eyebrow reveal">Ihr Ansprechpartner</p>
        <h2 id="person-title" class="person-name reveal">Eymen Kumaru</h2>
        <p class="person-role reveal">Inhaber in Käfertal</p>
        <ul class="feature-list">
          <li class="reveal"><span class="card-icon">{ic("user")}</span><h3>Ein Ansprechpartner</h3><p>Sie erreichen immer mich selbst, vom ersten Anruf bis zur Lösung.</p></li>
          <li class="reveal"><span class="card-icon">{ic("pin")}</span><h3>Vor Ort oder online</h3><p>Bei Ihnen in Mannheim und Umgebung oder bequem per Fernwartung.</p></li>
          <li class="reveal"><span class="card-icon">{ic("message")}</span><h3>Einfach erklärt</h3><p>Ich sage Ihnen vorher, was ich tue, und erkläre es ohne Fachchinesisch.</p></li>
        </ul>
        <div class="btn-row reveal" style="margin-top:2rem">{link("ueber-mich.html", "Mehr über mich")}</div>
      </div>
    </div>
  </section>

  <section class="section section-navy" aria-labelledby="ablauf-title">
    <div class="container">
      {section_head("Ablauf", "So läuft es ab", hid="ablauf-title")}
      {steps3([
        ("Anruf oder Nachricht", "Sie schildern mir kurz Ihr Anliegen. Das Gespräch am Telefon ist kostenlos und unverbindlich."),
        ("Klarer Vorschlag", "Sie erfahren vorher, was ich empfehle und womit Sie rechnen können: Privathaushalte zahlen nach Zeit, Unternehmen arbeiten mit Wartungsvertrag. Sie entscheiden."),
        ("Umsetzung", "Ich setze um, was Sie freigegeben haben, vor Ort oder per Fernwartung, und erkläre Ihnen das Ergebnis. Danach bleibe ich Ihr Ansprechpartner."),
      ])}
    </div>
  </section>

  {cta_band("Sprechen wir über Ihre IT.", "Erzählen Sie mir am Telefon, was Sie brauchen. Danach wissen Sie, wie es weitergeht.",
            links=link("kontakt.html", "Alle Kontaktwege"), area=True)}
'''

# ================================================================= UNTERNEHMEN
CALC_ITEMS = [
    ("arbeitsplaetze", "Arbeitsplätze", "Ein Mitarbeiter mit Computer oder Notebook · 99 € je Arbeitsplatz und Monat", 99, 1, 1),
    ("vms", "Virtuelle Maschinen", "10 € je VM und Monat", 10, 0, 0),
    ("geraete", "Weitere Geräte: Notebooks, Handys &amp; Tablets", "Zusätzlich zum Arbeitsplatz · 10 € je Gerät und Monat", 10, 0, 0),
    ("drucker", "Drucker &amp; Multifunktionsgeräte", "10 € je Gerät und Monat", 10, 0, 0),
    ("server", "Server", "60 € je Server und Monat", 60, 0, 0),
    ("nas", "Netzwerkspeicher &amp; NAS", "30 € je System und Monat", 30, 0, 0),
    ("netzwerk", "Switches, Access Points, Router &amp; Firewalls", "5 € je Gerät und Monat", 5, 0, 0),
    ("iot", "IoT-Geräte (Kameras, Zutrittsleser, Sensoren)", "1 € je Gerät und Monat", 1, 0, 0),
    ("telefon", "Telefonanlage (Cloud oder vor Ort)", "50 € je Anlage und Monat", 50, 0, 0),
    ("stunden", "Zusätzliche feste Stunden im Monat", "3 Stunden sind je Vertrag enthalten. Jede weitere fest gebuchte Stunde: 49 € netto.", 49, 0, 0),
]


def calc_rows():
    out = []
    for key, label, desc, price, mn, default in CALC_ITEMS:
        plain = label.replace("&amp;", "&")
        out.append(f'''<li class="calc-row" data-calc-row data-price="{price}">
            <div><label for="c-{key}">{label}</label><span class="r-desc" id="c-{key}-d">{desc}</span></div>
            <div class="stepper">
              <button type="button" data-step="-1" aria-label="{esc(plain)}: einen weniger">{ic("minus")}</button>
              <input id="c-{key}" name="{key}" type="number" inputmode="numeric" min="{mn}" max="99" value="{default}" aria-describedby="c-{key}-d" data-calc-input>
              <button type="button" data-step="1" aria-label="{esc(plain)}: einen mehr">{ic("plus")}</button>
            </div>
            <output class="calc-line" for="c-{key}" data-calc-line>{f"{price * default:.2f}".replace(".", ",")} €</output>
          </li>''')
    return "\n".join(out)


unternehmen_body = f'''
  <section class="page-hero" aria-labelledby="hero-title">
    <div class="container hero-grid">
      <div>
        <p class="eyebrow reveal">Für Unternehmen</p>
        <h1 id="hero-title" class="reveal">IT-Betreuung für kleine Unternehmen in Mannheim</h1>
        <p class="hero-lead reveal">Für Praxis, Kanzlei, Handwerk, Laden und Büro: Ich übernehme Ihre IT-Betreuung im Wartungsvertrag, wenn Sie keinen eigenen IT-Mitarbeiter haben. Gern auch außerhalb Ihrer Öffnungszeiten.</p>
        <div class="btn-row reveal">{btn_call(label="Kostenlose Bestandsaufnahme vereinbaren")}{btn("#rechner", "Wartungsvertrag online berechnen", icon="calculator")}</div>
        <p class="hero-lead reveal" style="font-size:1rem">Telefon: <a href="{TEL}">{PHONE}</a></p>
      </div>
      {qr_card("Scannen und anrufen")}
    </div>
  </section>

  <section class="section" aria-labelledby="rolle-title">
    <div class="container split split-center">
      <div>
        {section_head("Externe IT-Abteilung", "Für Unternehmen ohne eigene IT-Abteilung", left=True, hid="rolle-title")}
        <div class="prose reveal">
          <p>Große Firmen haben eine eigene IT-Abteilung. In kleinen Unternehmen übernehme ich diese Rolle als externe IT-Abteilung, schon ab einem Arbeitsplatz.</p>
          <p>Als Einzelunternehmer bin ich immer Ihr direkter Ansprechpartner, am Telefon und vor Ort.</p>
          <p>Ich bin zum Beispiel für Arzt- und Zahnarztpraxen da, für Kanzleien und Steuerbüros, für Handwerksbetriebe, Läden und Gastronomie, für Pflegedienste und Vereine und für Selbstständige im Homeoffice.</p>
        </div>
      </div>
      {media("unternehmen-buero", "Mitarbeiterin arbeitet an einem Büroarbeitsplatz mit Computer und Unterlagen")}
    </div>
  </section>

  <section class="section section-alt" id="leistungen" aria-labelledby="leist-title">
    <div class="container">
      {section_head("Leistungen", "Was ich für Unternehmen übernehme", "Alles im Rahmen Ihres Wartungsvertrags.", hid="leist-title")}
      {cards([
        ("user-plus", "Arbeitsplätze einrichten", "Ich richte neue Rechner ein und statte neue Mitarbeitende vollständig aus. Verlässt jemand das Team, schließe ich die Zugänge sauber."),
        ("wifi", "Netzwerk &amp; WLAN", "Ich richte Ihr Netzwerk ein, mit eigenem Gästenetz für Kunden, WLAN in jedem Raum und aufgeräumter Verkabelung."),
        ("mail", "Microsoft 365 &amp; E-Mail", "Postfächer, Kalender und gemeinsame Ablage, auch beim Umzug vom alten Anbieter. Ihr Team bekommt eine Einweisung."),
        ("database", "Datensicherung &amp; NAS", "Ich richte eine automatische Sicherung ein und spiele die Wiederherstellung einmal mit Ihnen durch. So wissen Sie sicher, dass sie funktioniert."),
        ("printer", "Drucker &amp; Multifunktionsgeräte", "Im Netzwerk eingebunden, Scans landen direkt im Postfach oder im richtigen Ordner. Auch vom Handy aus."),
        ("shield", "IT-Sicherheit", "Virenschutz, Updates, Passwörter und Zugriffsrechte. Auf Wunsch zeige ich Ihrem Team, wie es gefälschte E-Mails sicher erkennt."),
        ("clock", "Zeiterfassung", "Digitale Zeiterfassung, die zu Ihrem Betrieb passt: am Terminal, am Rechner oder per App. Mit Einweisung fürs Team und abgestimmt mit Ihrem Lohnbüro."),
        ("receipt", "E-Rechnung", "Ich richte XRechnung oder ZUGFeRD in Ihrer Software ein und stimme den Ablauf mit Ihrem Steuerbüro ab."),
        ("truck", "Umzug &amp; Neueröffnung", "Ich ziehe Ihre Technik mit um. Internet und Netzwerk laufen schon vor dem ersten Arbeitstag."),
        ("clipboard", "Regelmäßige Wartung", "Meistens einmal im Quartal: Updates, Virenschutz, Datensicherung, Festplatten und Reinigung. Danach bekommen Sie einen kurzen Bericht."),
        ("headset", "Laufende Betreuung", "Ein fester Ansprechpartner, schnelle Hilfe per Fernwartung und Termine vor Ort, im Rahmen Ihres Wartungsvertrags."),
        ("globe", "Webseiten", "Mobil bedienbar, schnell, mit Impressum und Datenschutz nach deutschem Recht. Auf Wunsch mit Domain und Hosting, für Vertragskunden zum Festpreis."),
      ], compact=True)}
      <p class="hint-line reveal">{link("leistungen.html", "Auch für Privatkunden und Senioren")}</p>
    </div>
  </section>

  <section class="section section-navy" aria-labelledby="weg-title">
    <div class="container">
      {section_head("Ablauf", "Bestandsaufnahme, Vorschlag, Umsetzung", hid="weg-title")}
      {steps3([
        ("Bestandsaufnahme", "Ich komme in Ihren Betrieb und sehe mir an, was da ist und was Sie vorhaben. Das dauert meistens ein bis zwei Stunden und ist für Sie kostenlos."),
        ("Vorschlag mit Preisrahmen", "Sie bekommen schriftlich, was ich empfehle, welcher monatliche Betrag sich für Ihren Betrieb ergibt und was zurückgestellt werden kann. Auch der Vorschlag ist kostenlos und unverbindlich. Sie entscheiden."),
        ("Umsetzung und danach", "Umbauten lege ich möglichst außerhalb Ihrer Öffnungszeiten. Danach betreue ich Ihren Betrieb im Wartungsvertrag."),
      ])}
    </div>
  </section>

  <section class="section section-alt" id="wartungsvertrag" aria-labelledby="vertrag-title">
    <div class="container">
      {section_head("Wartungsvertrag", "Wartungsvertrag für Ihren Betrieb", "Für Unternehmen arbeite ich ausschließlich im Wartungsvertrag. So ist Ihre IT laufend betreut und Sie wissen jeden Monat, womit Sie rechnen.", hid="vertrag-title")}
      <div class="split">
        <div class="price-card reveal">
          <span class="price-tag">Für Unternehmen</span>
          <p class="price-big"><strong>ab 199 €</strong><span>netto im Monat</span></p>
          <p class="price-text">Der Preis liegt bei 99 € je Arbeitsplatz und Monat, der Mindestbetrag bei 199 €. Ein Arbeitsplatz ist ein Mitarbeiter mit seinem Computer oder Notebook. Server, Netzwerk und weitere Geräte kommen je nach Bedarf dazu; den Betrag stellen Sie unten für Ihren Betrieb zusammen.</p>
          <p class="price-text">Zzgl. 19 % USt. Drei Stunden sind inklusive. Was über die drei Stunden hinausgeht, berechne ich mit 49 € netto pro Stunde. Der Vertrag läuft mindestens drei Monate, danach ist er monatlich kündbar.</p>
          <div class="btn-row">{btn("#rechner", "Vertrag berechnen", "btn-primary", icon="calculator")}</div>
        </div>
        <div class="reveal">
          <h3 style="margin-bottom:1rem">Das ist enthalten</h3>
          {checklist([
            "<strong>Wartungstermin einmal im Quartal:</strong> Updates, Virenschutz, Datensicherung, Festplatten und Reinigung, danach ein kurzer Bericht.",
            "<strong>Überwachung:</strong> Ich behalte Datensicherung, Festplatten, Virenschutz und Zertifikate im Blick. Fällt etwas auf, merke ich es meistens vor Ihnen.",
            "<strong>Updates:</strong> Windows, Programme, Router und Firewall halte ich aktuell.",
            "<strong>Geprüfte Datensicherung:</strong> Ich teste, ob sich Ihre Daten wirklich zurückholen lassen.",
            "<strong>Drei Stunden inklusive,</strong> zum Beispiel für ein neues Postfach oder einen neuen Mitarbeiter.",
            "<strong>Vorrang bei Störungen:</strong> Vertragskunden werden bevorzugt bearbeitet.",
          ])}
        </div>
      </div>

      <div class="sub-head reveal">
        <div><h3>Was das für Ihren Betrieb bedeutet</h3><p>Monatsbetrag netto zzgl. 19 % USt., ohne Server, Netzwerk und weitere Geräte.</p></div>
      </div>
      <div class="split">
        <ul class="rows reveal" aria-label="Beispielbeträge nach Arbeitsplätzen">
          <li><span class="r-title">1 Arbeitsplatz<span class="r-desc">Mindestbetrag, zum Beispiel für Selbstständige im Büro oder Homeoffice</span></span><span class="r-val">199 €</span></li>
          <li><span class="r-title">3 Arbeitsplätze</span><span class="r-val">297 €</span></li>
          <li class="is-highlight"><span class="r-title">5 Arbeitsplätze</span><span class="r-val">495 €</span></li>
          <li><span class="r-title">10 Arbeitsplätze</span><span class="r-val">990 €</span></li>
        </ul>
        <div class="reveal">
          {checklist([
            "Vorsteuerabzugsfähig, die Umsatzsteuer ist ausgewiesen.",
            "Per Überweisung innerhalb von 14 Tagen.",
            "Abends und am Wochenende ohne Aufschlag.",
            "In Mannheim ohne Anfahrtspauschale, außerhalb einmal pro Termin nach Entfernung. Fernwartung ohne Anfahrt.",
          ])}
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="rechner" aria-labelledby="rechner-title">
    <div class="container">
      {section_head("Rechner", "Vertrag für Ihren Betrieb berechnen", "Stellen Sie zusammen, was zu Ihrem Betrieb gehört. Die Summe ist eine unverbindliche Kalkulation, den endgültigen Betrag lege ich nach einer kurzen Bestandsaufnahme fest.", hid="rechner-title")}
      <form class="calc" data-calc onsubmit="return false" aria-label="Wartungsvertrag berechnen">
        <ul class="calc-list reveal">
          {calc_rows()}
        </ul>
        <aside class="calc-sum reveal" aria-label="Ergebnis">
          <p class="label">Monatsbeitrag</p>
          <output class="calc-total" data-calc-total aria-live="polite">199,00 €</output>
          <p class="calc-min" data-calc-min>Mindestbetrag 199 € greift</p>
          <p class="sum-fine">netto zzgl. 19 % USt. · mindestens 199 € im Monat · Mindestlaufzeit 3 Monate, danach monatlich kündbar · keine Staffelpreise</p>
          <div class="btn-row">
            <a class="btn btn-primary btn-lg" href="mailto:{MAIL}" data-calc-mail>{ic("mail")}Angebot anfragen</a>
            <button class="btn btn-outline" type="button" data-calc-reset>{ic("refresh")}Zurücksetzen</button>
          </div>
        </aside>
      </form>
      <p class="calc-disclaimer reveal">Unverbindliche Kalkulation, kein Angebot. Der endgültige Betrag steht nach einer kurzen Bestandsaufnahme fest. Geräte im Vertrag überwache ich laufend, Vertragskunden werden bei Störungen bevorzugt bearbeitet.</p>
      <div class="callout on-coral reveal">
        <p><strong>Größere Vorhaben für Vertragskunden</strong>Für ein neues Netzwerk, einen Umzug oder die Einführung von Microsoft 365 bekommen Vertragskunden auf Wunsch ein schriftliches Festpreisangebot. Webseiten gibt es für Vertragskunden immer zum Festpreis.</p>
      </div>
    </div>
  </section>

  <section class="section section-alt" aria-labelledby="avv-title">
    <div class="container">
      {section_head("Verlässlichkeit", "Auftragsverarbeitung und Dokumentation", hid="avv-title")}
      <div class="grid-3">
        <article class="card reveal"><span class="card-icon">{ic("lock")}</span><h3>Auftragsverarbeitungsvertrag</h3><p>Wo ich mit personenbezogenen Daten in Berührung komme, schließen wir auf Wunsch einen Vertrag zur Auftragsverarbeitung nach Art. 28 DSGVO. Geben Sie mir dazu bitte vor Auftragsbeginn Bescheid.</p></article>
        <article class="card reveal"><span class="card-icon">{ic("file")}</span><h3>Dokumentation, die Ihnen gehört</h3><p>Zu jedem größeren Auftrag schreibe ich auf, was wo steht, welche Zugänge es gibt und wohin gesichert wird. So wissen Sie auch ohne mich, was eingerichtet ist.</p></article>
        {fern_warn(team=True)}
      </div>
    </div>
  </section>

  {faq("Häufige Fragen", "Was Unternehmen vorher wissen wollen", None, [
    ("Ab welcher Betriebsgröße lohnt sich das?", "Ab einem Arbeitsplatz. Ein Ein-Personen-Betrieb mit einem Rechner, einem Drucker und einem Postfach ist ein typischer Auftrag. Nach oben liegt die sinnvolle Grenze bei Unternehmen bis 10 Mitarbeitern. Bei größeren Betrieben sage ich Ihnen offen, ob ich der richtige Ansprechpartner bin."),
    ("Was kostet die Bestandsaufnahme?", "Nichts. Die Bestandsaufnahme in Ihrem Betrieb und der schriftliche Vorschlag mit Preisrahmen sind für Unternehmen kostenlos und unverbindlich. Kosten entstehen erst mit dem Wartungsvertrag."),
    ("Rechnen Sie netto oder brutto ab?", "Für Unternehmen gelten Nettopreise zzgl. 19 % USt.: der monatliche Betrag des Wartungsvertrags und Stunden über die drei inklusiven hinaus mit 49 € netto. Auf der Rechnung ist die Umsatzsteuer gesondert ausgewiesen und damit für Sie vorsteuerabzugsfähig."),
    ("Was gehört zur regelmäßigen Wartung?", ["Ein fester Termin im Takt Ihrer Wahl, meistens quartalsweise. Geprüft werden Updates für Windows und die Programme, Virenschutz, Datensicherung samt Rückspieltest, Zustand der Festplatten, Router und Access Points sowie Drucker und Verbrauchsmaterial. Dazu die Reinigung der Geräte, damit sie lange halten.", "Danach bekommen Sie einen kurzen Bericht, was ich erledigt habe und was als Nächstes ansteht."]),
    ("Brauche ich dafür einen Wartungsvertrag?", "Ja. Für Unternehmen arbeite ich ausschließlich im Wartungsvertrag. Sie stellen online zusammen, was zu Ihrem Betrieb gehört, drei Stunden sind inklusive, weitere Stunden kosten 49 € netto, Mindestlaufzeit drei Monate, danach monatlich kündbar."),
    ("Wie schnell sind Sie da?", ["In der Regel ist ein Termin am selben oder am nächsten Tag möglich. In dringenden Fällen sagen Sie es mir am Telefon, dann priorisiere ich Ihr Anliegen.", "Sie erfahren am Telefon verbindlich, wann ich da bin. Vieles erledige ich auch sofort per Fernwartung."]),
    ("Wann erreiche ich Sie?", "Telefonisch täglich von 8 bis 20 Uhr. Wenn ich gerade bei einem Kunden bin, sprechen Sie auf die Mailbox oder schreiben per WhatsApp. Ich melde mich in der Regel innerhalb einer Stunde zurück. Einen Termin machen wir dann aus, gern auch kurzfristig."),
    ("Können Sie außerhalb der Öffnungszeiten kommen?", "Ja, gern. Früh morgens, abends oder am Wochenende, ohne Aufschlag."),
    ("Schließen Sie einen Auftragsverarbeitungsvertrag ab?", "Ja. Wo ich mit personenbezogenen Daten in Berührung komme, etwa in einer Praxis oder Kanzlei, schließen wir auf Wunsch einen Auftragsverarbeitungsvertrag nach Art. 28 DSGVO. Bringen Sie gern Ihr eigenes Muster mit."),
    ("Übernehmen Sie auch Technik, die jemand anders eingerichtet hat?", "Ja. Der erste Schritt ist dann eine kostenlose Bestandsaufnahme: Was steht wo, welche Zugänge gibt es, wohin wird gesichert. Danach wissen Sie selbst, woran Sie sind, auch unabhängig von mir."),
    ("Können Sie uns bei der E-Rechnung helfen?", ["Ja. Eine E-Rechnung ist ein strukturierter Datensatz, den Ihre Software lesen und schreiben können muss. Verbreitet sind XRechnung und ZUGFeRD.", "Ich sehe mir an, was Ihr Rechnungsprogramm heute kann, richte das Empfangen und Erstellen ein und stimme den Ablauf mit Ihrem Steuerbüro ab. Wenn Ihr Programm es nicht kann, sage ich Ihnen, welches passt, bevor Sie etwas kaufen."]),
    ("Kaufen Sie die Geräte für uns ein?", ["Die Beschaffung übernehme ich gern: Geräte aussuchen, Angebote vergleichen, bestellen, Lieferung prüfen und anschließend alles einrichten. Bestellt wird dabei auf Ihren Namen. So laufen Rechnung, Garantie und Gewährleistung direkt zwischen Ihnen und dem Händler, ohne Umweg über mich.", "Die Zeit dafür läuft über die Stunden im Wartungsvertrag, bei größeren Bestellungen auf Wunsch zu einer festen Pauschale. Ich verkaufe keine Hardware und verdiene an keiner Empfehlung mit. Ich schlage vor, was zu Ihrer Arbeit passt."]),
  ])}

  {cta_band("Sprechen wir über Ihr Unternehmen.", "Ein Anruf oder eine kurze E-Mail genügt. Danach wissen Sie, ob ich der Richtige für Sie bin und womit Sie rechnen können.",
            extra_btn=btn_mail(subject="Anfrage%20Unternehmen"))}
'''

# ================================================================ PRIVATKUNDEN
def group(gid, icon, title, intro, items, extra="", photo=None):
    head = f'''<div class="sub-head reveal" id="{gid}">
        <div><h3>{title}</h3><p>{intro}</p></div>{extra}
      </div>'''
    if photo:
        name, alt, pos = (photo + (None,))[:3]
        return head + f'''
      <div class="group-split">
        {media(name, alt, cls="media media-tall", sizes="(min-width: 1040px) 40vw, 100vw", pos=pos)}
        {cards(items, grid="grid-2", compact=True, h="h4")}
      </div>'''
    return head + (cards(items, compact=True, h="h4") if items else "")


privat_body = f'''
  <section class="page-hero" aria-labelledby="hero-title">
    <div class="container hero-grid">
      <div>
        <p class="eyebrow reveal">Für Privatkunden &amp; Senioren</p>
        <h1 id="hero-title" class="reveal">Computerhilfe und IT-Service für Privatkunden in Mannheim</h1>
        <p class="hero-lead reveal">PC-Hilfe, WLAN, Drucker oder ein neues Smartphone: Persönlicher IT-Service für Privathaushalte und Senioren. Ich komme zu Ihnen nach Hause in Mannheim und Umgebung oder unterstütze Sie per Fernwartung.</p>
        <div class="btn-row reveal">{btn_call()}{btn("preise.html", "Preise ansehen", arrow=True)}</div>
      </div>
      {qr_card("Scannen und anrufen")}
    </div>
  </section>

  <section class="section" aria-labelledby="leist-title">
    <div class="container">
      {section_head("Leistungen", "Meine Leistungen", hid="leist-title")}
      <nav aria-label="Leistungsbereiche">
        <ul class="chips chips-center reveal" style="margin-bottom:1rem">
          <li><a class="chip" href="#einrichtung">{ic("laptop")}Einrichtung</a></li>
          <li><a class="chip" href="#reparatur">{ic("wrench")}Reparatur &amp; Pflege</a></li>
          <li><a class="chip" href="#wlan">{ic("wifi")}WLAN &amp; Internet</a></li>
          <li><a class="chip" href="#sicherheit">{ic("shield")}Sicherheit &amp; Daten</a></li>
          <li><a class="chip" href="#fernwartung">{ic("headset")}Fernwartung</a></li>
          <li><a class="chip" href="#senioren">{ic("heart")}Senioren</a></li>
          <li><a class="chip" href="#webseiten">{ic("globe")}Webseiten</a></li>
        </ul>
      </nav>

      {group("einrichtung", "laptop", "Einrichtung &amp; Installation", "Sie haben ein neues Gerät gekauft? Ich richte es ein, übertrage Ihre Daten und weise Sie in die Bedienung ein.", [
        ("laptop", "Computer &amp; Laptop einrichten", "Ich richte Windows und Ihre Programme ein. Dateien, Fotos und Lesezeichen nehmen Sie vom alten Gerät mit."),
        ("tablet", "Tablet einrichten", "Ich richte Ihr iPad oder Android-Tablet vollständig ein und stelle die Schrift so groß ein, dass Sie alles gut lesen können."),
        ("smartphone", "Smartphone einrichten", "Kontakte, Fotos und WhatsApp übertrage ich vom alten Gerät. Die Bedienung stelle ich so ein, wie es Ihnen leichtfällt."),
        ("mail", "E-Mail einrichten", "Ihre E-Mails kommen auf Computer, Handy und Tablet an, auch nach einem Anbieterwechsel."),
        ("printer", "Drucker installieren", "Ich bringe Ihren Drucker ins WLAN und richte das Scannen ein. Danach drucken Sie auch vom Handy aus."),
        ("tv", "MagentaTV, Vodafone TV &amp; Fernsehbox", "Ich schließe den Receiver an, sortiere die Sender und richte Aufnahme und Mediathek ein."),
        ("plug", "Zubehör anschließen", "Monitor, Drucker, Webcam oder Festplatte: Ich schließe alles an und teste es mit Ihnen."),
      ])}

      {group("reparatur", "wrench", "Computer reparieren lassen", "Bevor Sie neu kaufen: Oft lässt sich ein Gerät mit einem einzigen neuen Teil retten.", [
        ("wrench", "PC- &amp; Laptop-Reparatur", "Ich finde heraus, was Ihrem Gerät fehlt, und sage Ihnen ehrlich, ob sich die Reparatur lohnt."),
        ("smartphone", "Tablet- &amp; Smartphone-Reparatur", "Ich sehe mir Ihr Gerät an und sichere zuerst Ihre Daten, damit nichts verloren geht."),
        ("cpu", "Aufrüsten statt neu kaufen", "Mit einer SSD und etwas mehr Arbeitsspeicher wird Ihr Rechner wieder spürbar schneller."),
        ("sparkles", "Reinigung &amp; Wartung", "Eine gründliche Reinigung von Lüfter und Gehäuse sorgt dafür, dass Ihr Gerät wieder leise und leistungsfähig arbeitet."),
      ], photo=("privat-reparatur", "Geöffneter Laptop mit sichtbaren Bauteilen auf einer Werkbank"))}

      {group("pflege", "gauge", "Optimierung &amp; Pflege", "Wenn Ihr Computer langsam ist oder ein Programm nicht mehr startet, suche ich die Ursache und behebe sie.", [
        ("wifi", "WLAN &amp; Internet", "Ich konfiguriere Ihren Router und sorge dafür, dass das WLAN in allen Räumen zuverlässig verfügbar ist.", "", "wlan"),
        ("bug", "Softwareprobleme beheben", "Startet ein Programm nicht oder arbeitet es fehlerhaft, ermittle ich die Ursache und stelle den Betrieb wieder her."),
        ("gauge", "Computer wieder schneller machen", "Ich bereinige das System, installiere ausstehende Updates und entferne, was die Leistung beeinträchtigt."),
        ("refresh", "Windows-Updates &amp; Systempflege", "Ich installiere ausstehende Updates und bringe Windows wieder auf einen sauberen Stand."),
      ])}

      {group("sicherheit", "shield", "Daten &amp; Sicherheit", "Ich sorge dafür, dass Ihre Fotos und Dokumente nicht verloren gehen und niemand Fremdes an Ihre Daten kommt.", [
        ("shield", "Virenentfernung", "Ich entferne Schadsoftware und unerwünschte Werbeprogramme und richte einen zuverlässigen Schutz ein."),
        ("database", "Datensicherung einrichten", "Ihre Daten werden automatisch gesichert. Ob auf eine Festplatte oder in die Cloud, entscheiden Sie."),
        ("transfer", "Daten auf ein neues Gerät übertragen", "Fotos, Dokumente, Kontakte und E-Mails ziehen vollständig mit um."),
        ("key", "Passwörter ordnen", "Ich richte Ihnen einen Passwort-Manager ein und zeige Ihnen, wie Sie ihn benutzen."),
      ])}

      {group("fernwartung", "headset", "Fernwartung &amp; Betreuung", "Viele Anliegen lassen sich aus der Ferne in wenigen Minuten erledigen, ganz ohne Vor-Ort-Termin. Die Verbindung startet nur mit Ihrer Freigabe.", [
        ("headset", "Schnelle Hilfe ohne Termin", "Für Einstellungen, Updates und kurze Fragen. Sie geben die Verbindung frei und beenden sie, wann Sie möchten."),
        ("calendar", "Regelmäßige Pflege", "Ich installiere Updates, bereinige das System und prüfe die Datensicherung, in dem Rhythmus, den Sie wünschen."),
        ("user", "Laufende Betreuung", "Für alle, die einen festen Ansprechpartner möchten. Den Umfang legen wir gemeinsam fest."),
      ], extra=btn("fernwartung.html", "Fernwartung starten", "btn-primary", "btn-sm", icon="download"))}

      {group("senioren", "heart", "Digitale Unterstützung für Senioren", "Sie möchten Computer, Tablet und Smartphone sicher und selbstbewusst nutzen? Ich nehme mir die nötige Zeit.", [
        ("users", "Geduldiges Erklären &amp; Üben", "Wir gehen die Funktionen gemeinsam Schritt für Schritt durch, etwa WhatsApp-Nachrichten, Videotelefonate mit der Familie oder die Suche im Internet, und üben so lange, bis Sie sich sicher fühlen."),
        ("book", "Persönliche Schritt-für-Schritt-Notizen", "Auf Wunsch halte ich die wichtigsten Schritte gut lesbar schriftlich fest, damit Sie sie jederzeit nachschlagen können."),
        ("alert", "Schutz vor Enkeltrick, Phishing &amp; Betrug", "Ich zeige Ihnen, woran Sie gefälschte Anrufe, verdächtige SMS und betrügerische E-Mails sofort erkennen, damit Ihr Geld und Ihre Daten sicher bleiben."),
        ("bag", "Unabhängige Kaufberatung", "Sie überlegen, ein neues Gerät anzuschaffen? Ich berate Sie neutral und unabhängig, welches Smartphone, Tablet oder welcher Laptop am besten zu Ihren Bedürfnissen passt."),
      ], photo=("privat-senioren", "Großvater und Enkel schauen gemeinsam auf ein Tablet", "62% 50%"))}

      {group("webseiten", "globe", "Webseiten erstellen", "Schlichte, schnelle Webseiten für Hobby, Verein und Gewerbe, mit Impressum und Datenschutz nach deutschem Recht.", [
        ("globe", "Für Hobby, Verein und Gewerbe", "Eine schlichte, schnelle Webseite für den privaten oder ehrenamtlichen Rahmen oder für Ihr eigenes Gewerbe."),
        ("file", "Impressum und Datenschutz inklusive", "Beide Seiten sind von Anfang an nach deutschem Recht dabei."),
      ])}

      <div class="callout on-coral reveal">
        <p><strong>Sie suchen IT-Betreuung für Ihr Unternehmen oder Ihre Praxis?</strong>Für Gewerbe, Kanzlei, Praxis und Handwerk biete ich Arbeitsplatz-Einrichtung, Firmennetzwerke, Microsoft 365, Datensicherung und E-Rechnung, alles im Wartungsvertrag.</p>
        {btn("geschaeftskunden.html", "Leistungen für Unternehmen ansehen", "btn-outline", "btn-sm", arrow=True)}
      </div>
    </div>
  </section>

  {cta_band("Ihr Anliegen ist nicht dabei?", "Sprechen Sie mich gern an. Ich sage Ihnen offen, ob ich helfen kann, und andernfalls, wer Ihnen weiterhilft.",
            links=link("preise.html", "Preise ansehen") + link("kontakt.html", "Alle Kontaktwege"))}
'''

PAGES1 = [
    ("index.html", "Clavis IT Service | IT-Service für Privathaushalte & Unternehmen in Mannheim",
     "IT-Service in Mannheim und 25 km Umkreis: für Privathaushalte und Senioren vor Ort, für kleine Unternehmen im Wartungsvertrag. Auch per Fernwartung.",
     index_body, None, JSONLD),
    ("geschaeftskunden.html", "IT-Betreuung für kleine Unternehmen in Mannheim | Clavis IT Service",
     "IT-Betreuung für kleine Unternehmen in Mannheim und Umgebung: Arbeitsplätze, Netzwerk, Microsoft 365, Wartung und Datensicherung im Wartungsvertrag.",
     unternehmen_body, None, ""),
    ("leistungen.html", "Computerhilfe für Privatkunden in Mannheim | Clavis IT Service",
     "Computerhilfe in Mannheim: PC, Laptop, Tablet, Smartphone, WLAN, Drucker und Fernseher einrichten und reparieren, zu Hause oder per Fernwartung.",
     privat_body, None, ""),
]
