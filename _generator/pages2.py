# -*- coding: utf-8 -*-
from core import *


def rows(items, label, highlight=None):
    out = [f'<ul class="rows reveal" aria-label="{label}">']
    for i, it in enumerate(items):
        title, desc, val = it
        d = f'<span class="r-desc">{desc}</span>' if desc else ""
        hl = ' class="is-highlight"' if highlight == i else ""
        out.append(f'<li{hl}><span class="r-title">{title}{d}</span><span class="r-val">{val}</span></li>')
    out.append("</ul>")
    return "".join(out)


# ======================================================================= PREISE
preise_body = f'''
  <section class="page-hero page-hero-simple" aria-labelledby="hero-title">
    <div class="container">
      <p class="eyebrow reveal">Preise</p>
      <h1 id="hero-title" class="reveal">Preise, die Sie vorher kennen.</h1>
      <p class="hero-lead reveal">Ein fairer Stundensatz für Privathaushalte und ein planbarer Wartungsvertrag für Unternehmen bis 10 Mitarbeiter. Keine versteckten Kosten.</p>
    </div>
  </section>

  <section class="section" aria-label="Preismodelle" style="padding-top:2.5rem">
    <div class="container">
      <div class="tabs-wrap reveal">
        <div class="tabs" role="tablist" aria-label="Preise für" data-tabs>
          <button class="tab" role="tab" id="tab-privat" aria-controls="privat" aria-selected="true" type="button">{"Für Privathaushalte"}</button>
          <button class="tab" role="tab" id="tab-unternehmen" aria-controls="unternehmen" aria-selected="false" tabindex="-1" type="button">Für Unternehmen</button>
        </div>
      </div>

      <div class="tab-panel" role="tabpanel" id="privat" aria-labelledby="tab-privat" tabindex="0">
        <div class="split">
          <div class="price-card">
            <span class="price-tag">Für Privathaushalte</span>
            <p class="price-big"><strong>49 €</strong><span>pro Stunde</span></p>
            <p class="price-text">Klarer Endpreis inklusive 19 % MwSt. Vor Ort zählt die erste Stunde voll, danach geht es im fairen Viertelstundentakt zu 12,25 € weiter. Sind wir nach 70 Minuten fertig, rechne ich 75 Minuten ab – nicht zwei volle Stunden. Per Fernwartung rechne ich ab der ersten Viertelstunde ab.</p>
            <p class="fine">Endpreis inklusive 19 % MwSt. · Für Unternehmen gibt es den Wartungsvertrag, siehe Tab <a href="#unternehmen" data-tab-link="unternehmen">„Für Unternehmen“</a>.</p>
            <div class="btn-row">{btn_call()}</div>
          </div>
          <div>
            {checklist([
              "<strong>Kostenloses Erstgespräch am Telefon:</strong> Wir besprechen vorab in Ruhe, worum es geht.",
              "<strong>In Mannheim 0 € Anfahrt:</strong> Keine Anfahrtspauschale in ganz Mannheim.",
              "<strong>Erklären gehört zum Termin dazu:</strong> Ich erkläre Ihnen alles verständlich und halte die wichtigsten Schritte auf Wunsch schriftlich fest.",
              "<strong>Ehrliche Beratung:</strong> Ich sage Ihnen offen, wenn sich eine Reparatur bei einem alten Gerät nicht mehr lohnt.",
              "<strong>Kein Abo, keine Bindung:</strong> Sie zahlen nur die Zeit, die ich für Sie arbeite.",
            ])}
          </div>
        </div>
      </div>

      <div class="tab-panel" role="tabpanel" id="unternehmen" aria-labelledby="tab-unternehmen" tabindex="0" hidden>
        <div class="split">
          <div class="price-card">
            <span class="price-tag">Wartungsvertrag für Ihren Betrieb</span>
            <p class="price-big"><strong>ab 199 €</strong><span>netto im Monat</span></p>
            <p class="price-text">Für Unternehmen arbeite ich ausschließlich im Wartungsvertrag. Drei Stunden sind inklusive, was darüber hinausgeht, kostet 49 € netto pro Stunde. Mindestlaufzeit drei Monate, danach monatlich kündbar.</p>
            <p class="price-text">Der Preis liegt bei 99 € je Arbeitsplatz und Monat, der Mindestbetrag bei 199 €. Ein Arbeitsplatz ist ein Mitarbeiter mit seinem Computer oder Notebook, zum Beispiel 495 € im Monat bei 5 Arbeitsplätzen. Server, Netzwerk und weitere Geräte kommen je nach Bedarf dazu; den genauen Betrag stellen Sie online zusammen.</p>
            <p class="fine">Zzgl. 19 % USt., auf der Rechnung gesondert ausgewiesen und vorsteuerabzugsfähig. · Für Privathaushalte 49 € pro Stunde inklusive MwSt., siehe Tab <a href="#privat" data-tab-link="privat">„Für Privathaushalte“</a>.</p>
            <div class="btn-row">{btn("geschaeftskunden.html#rechner", "Wartungsvertrag online berechnen", "btn-primary", icon="calculator")}{link("geschaeftskunden.html", "Leistungen für Unternehmen")}</div>
          </div>
          <div>
            {checklist([
              "<strong>Wartungstermin einmal im Quartal:</strong> Updates, Virenschutz, Datensicherung, Festplatten und Reinigung, danach ein kurzer Bericht.",
              "<strong>Drei Stunden inklusive,</strong> zum Beispiel für ein neues Postfach oder einen neuen Mitarbeiter.",
              "<strong>Vorrang bei Störungen:</strong> Vertragskunden werden bevorzugt bearbeitet.",
              "Abends und am Wochenende ohne Aufschlag.",
              'In Mannheim 0 € Anfahrt, außerhalb die gleiche Staffel wie für Privathaushalte, <a href="#anfahrt">siehe unten</a>. Fernwartung ohne Anfahrt.',
              "Per Überweisung innerhalb von 14 Tagen.",
              'Nach Arbeitsplätzen, zusätzlichen Geräten und Stunden berechnet, keine Staffelpreise. Alle Positionen im <a href="geschaeftskunden.html#rechner">Rechner auf der Unternehmensseite</a>.',
            ])}
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section-navy" id="anfahrt" aria-labelledby="anfahrt-title">
    <div class="container split">
      <div>
        {section_head("Anfahrt", "Anfahrt", left=True, hid="anfahrt-title")}
        <p class="section-lead reveal" style="margin-top:-1.5rem">In Mannheim komme ich ohne Anfahrtspauschale. Außerhalb zählt die Entfernung in Luftlinie ab meinem Standort in Mannheim-Käfertal. Alle genannten Beträge sind Endpreise inklusive 19 % MwSt.</p>
      </div>
      {rows([
        ("Mannheim", "Mein Standort, hier bin ich in wenigen Minuten", "0 €"),
        ("Bis 10 km", "z. B. Viernheim, Ilvesheim, Heddesheim, Ladenburg, Edingen-Neckarhausen", "10 €"),
        ("Bis 25 km", "z. B. Schriesheim, Hirschberg, Weinheim, Hemsbach, Laudenbach, Heppenheim, Bensheim, Heidelberg", "15 €"),
        ("Mehr als 25 km", "Auf Anfrage", "nach Absprache"),
        ("Fernwartung", "Keine Anfahrt, nur die Arbeitszeit", "keine Anfahrt"),
      ], "Anfahrtspauschalen", highlight=0)}
    </div>
  </section>

  <section class="section" aria-labelledby="bsp-title">
    <div class="container">
      {section_head("Beispiele", "Beispiele aus dem Alltag", "Das sind Erfahrungswerte aus dem Alltag (inklusive 19 % MwSt.). Am Telefon nenne ich Ihnen gern vorab eine unverbindliche Einschätzung für Ihr Anliegen.", hid="bsp-title")}
      <div class="split">
        <div>
          {rows([
            ("Neuen Laptop oder PC einrichten", "Einrichten, Daten und Fotos übernehmen, Bedienung erklären", "ca. 1–2 Std. · 49–98 €"),
            ("Drucker anschließen und ins WLAN bringen", "Inklusive Einrichtung auf Handy und Tablet", "ca. 1 Std. · ab 49 €"),
            ("WLAN-Verbindung stabilisieren", "Signal prüfen, Router einstellen, bei Bedarf Verstärker einrichten", "ca. 1–2 Std. · 49–98 €"),
            ("Viren entfernen und Schutz einrichten", "Schadsoftware entfernen, System prüfen, Schutz einrichten", "ca. 1–2 Std. · 49–98 €"),
            ("Smartphone oder Tablet einrichten", "Kontakte, Fotos und WhatsApp übernehmen, Bedienung anpassen", "ca. 1 Std. · ab 49 €"),
            ("MagentaTV oder Vodafone TV einrichten", "Box anschließen, Sender sortieren, Mediathek erklären", "ca. 1 Std. · ab 49 €"),
            ("Kurze Hilfe per Fernwartung", "Eine Einstellung, ein Update, eine Frage", "ab 12,25 €"),
          ], "Beispiele für Privathaushalte")}
          <p class="table-note reveal"><strong>Material &amp; Neugeräte:</strong> Zubehör wie Kabel, Festplatten oder ein neuer WLAN-Verstärker besprechen wir vorab gemeinsam. Sie entscheiden selbst, ob Sie es selbst besorgen oder ob ich etwas Passendes mitbringe.</p>
          <p class="reveal">{link("leistungen.html", "Alle Leistungen für Ihr Zuhause ansehen")}</p>
        </div>
        <div>
          <h3 class="reveal" style="margin-bottom:.4rem">Beispiele für Unternehmen</h3>
          <p class="reveal" style="color:var(--text-muted);margin-bottom:1.25rem">Typischer Zeitaufwand. Im Wartungsvertrag sind drei Stunden inklusive.</p>
          {rows([
            ("Neuen Arbeitsplatz einrichten", "Rechner einrichten, Zugänge anlegen, Programme installieren", "ca. 1–2 Std."),
            ("Drucker ins Firmennetzwerk einbinden", "Einrichtung für alle Arbeitsplätze im Büro", "ca. 1 Std."),
            ("Microsoft 365 oder E-Mail einrichten", "Neues Postfach oder neuer Mitarbeiter", "ca. 1 Std."),
            ("WLAN mit Gästenetz einrichten", "Eigenes Netz für Kunden, getrennt vom Firmennetz", "ca. 1–2 Std."),
            ("Kurze Hilfe per Fernwartung", "Eine Einstellung, ein Update, eine Frage", "oft wenige Minuten"),
          ], "Beispiele für Unternehmen")}
          <p class="reveal" style="margin-top:1rem">{link("geschaeftskunden.html", "Alle Leistungen für Unternehmen ansehen")}</p>
        </div>
      </div>
    </div>
  </section>

  {faq("Häufige Fragen", "Häufige Fragen", None, [
    ("Wie ist die Anfahrt geregelt?", "In Mannheim ohne Pauschale. Außerhalb gilt die Staffel oben (bis 10 km 10 €, bis 25 km 15 €), einmal pro Termin. Bei Fernwartung fällt keine Anfahrt an."),
    ("Wie genau ist der Stundensatz aufgeteilt?", "Vor Ort liegt die erste Stunde bei 49 €. Danach geht es in Viertelstunden zu 12,25 € weiter. Ein Termin von 75 Minuten liegt damit bei 61,25 €. Bei Fernwartung zählt schon die erste Viertelstunde."),
    ("Muss ich vorher wissen, woran es liegt?", "Nein. Eine Beschreibung wie „Der Drucker druckt nicht mehr“ genügt. Die Ursache zu finden ist meine Aufgabe."),
    ("Was soll ich zum Termin bereithalten?", ["Alles, was zur Einrichtung gehört: E-Mail-Adresse und zugehöriges Passwort, den WLAN-Schlüssel, die Zugangsdaten Ihres Internetanbieters sowie Apple-ID oder Google-Konto samt Passwort.", "Ohne diese Angaben lassen sich viele Konten nicht einrichten, und ein vergessenes Passwort zurückzusetzen dauert oft länger als die eigentliche Arbeit. Ich notiere und speichere nichts davon."]),
    ("Wie ist der Preis bei Fernwartung?", "Es gilt derselbe Stundensatz, in Viertelstunden ab 12,25 €, ohne Anfahrt. Sie geben die Verbindung frei, sehen alles mit und beenden sie, wann Sie möchten."),
    ("Und wenn sich eine Reparatur nicht lohnt?", "Dann sage ich Ihnen, welcher Weg sich für Sie lohnt. Sie investieren nur die Zeit, die ich bis dahin gearbeitet habe."),
    ("Muss ich mich mit Technik auskennen?", "Nein. Fachkenntnisse sind nicht erforderlich. Beschreiben Sie mir, was nicht funktioniert. Ich kümmere mich um die Lösung und erkläre Ihnen alles klar und verständlich."),
    ("Rechnen Sie für Unternehmen netto ab?", 'Ja. Für Unternehmen gibt es ausschließlich den Wartungsvertrag, netto zzgl. 19 % USt.: 99 € je Arbeitsplatz und Monat, mindestens 199 € im Monat, drei Stunden inklusive, weitere Stunden 49 € netto. Auf der Rechnung ist die Umsatzsteuer gesondert ausgewiesen und damit für Sie vorsteuerabzugsfähig. Für Privathaushalte sind die 49 € der Endpreis inklusive 19 % MwSt. Alles Weitere finden Sie auf der <a href="geschaeftskunden.html">Seite für Unternehmen</a>.'),
    ("Bar oder per Überweisung?", "Bar vor Ort oder per Überweisung, wie es Ihnen lieber ist."),
    ("Kommen Sie auch abends oder am Wochenende?", "Ja, gern. Termine gibt es täglich nach Absprache, auch abends und am Wochenende, zum gleichen Preis."),
    ("Ich kenne mich mit Technik kaum aus. Ist das in Ordnung?", "Ja, natürlich. Ich erkläre alles verständlich und so oft Sie möchten. Auf Wunsch schreibe ich Ihnen die wichtigsten Schritte auf."),
  ], alt=True)}

  {cta_band("Sagen Sie mir, worum es geht.", "Am Telefon klären wir in wenigen Minuten, was zu tun ist und womit Sie rechnen können.",
            links=link("leistungen.html", "Für Privatkunden") + link("geschaeftskunden.html", "Für Unternehmen"))}
'''

# ==================================================================== ÜBER MICH
ueber_body = f'''
  <section class="page-hero" aria-labelledby="hero-title">
    <div class="container person">
      {portrait(eager=True)}
      <div>
        <p class="eyebrow reveal">Über mich</p>
        <h1 id="hero-title" class="reveal">Eymen Kumaru</h1>
        <p class="hero-lead reveal">Inhaber von Clavis IT Service. Wenn Sie anrufen, sprechen Sie direkt mit mir – und ich bin es auch, der anschließend zu Ihnen kommt.</p>
        <p class="hero-lead reveal">Geduldig, freundlich und zuverlässig bei Ihnen vor Ort in ganz Mannheim und Umgebung.</p>
        <div class="btn-row reveal">{btn_call()}{btn_wa(label="WhatsApp")}</div>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="wer-title">
    <div class="container split">
      <div>
        {section_head("Persönlich", "Wer zu Ihnen kommt", left=True, hid="wer-title")}
        <div class="prose reveal">
          <p>Ich komme direkt zu Ihnen nach Hause und kümmere mich um Ihre Technik. Dabei setze ich nur um, was wir vorher abgestimmt haben.</p>
          <p>Termine am Abend und am Wochenende sind bei mir normal.</p>
          <p>Was ich repariere, soll lange halten. Deshalb ermittle ich sorgfältig die Ursache.</p>
        </div>
      </div>
      <div>
        <h2 class="reveal" style="font-size:1.6rem;margin-bottom:1.75rem">So läuft ein Termin ab</h2>
        {steps_v([
          ("Sie rufen an.", "Eine kurze Beschreibung genügt. Oft sage ich Ihnen schon am Telefon, woran es liegt und wann ich Zeit habe."),
          ("Ich sehe es mir an.", "Ich suche die Ursache und sage Ihnen, was ich vorhabe. Sie entscheiden, was gemacht wird."),
          ("Ich setze es um.", "Drucker, WLAN und neue Geräte richte ich dort ein, wo sie stehen. Kleinere Anliegen erledige ich auch per Fernwartung. Ich nehme mir die Zeit, die Ihr Anliegen erfordert – sorgfältig und ohne Zeitdruck."),
          ("Ich weise Sie ein.", "Bevor ich gehe, gehen wir alles gemeinsam durch, damit Sie anschließend sicher damit arbeiten können. Bei späteren Fragen bin ich weiterhin für Sie erreichbar."),
        ])}
      </div>
    </div>
  </section>

  <section class="section section-alt" aria-labelledby="blick-title">
    <div class="container">
      <div class="price-card reveal">
        <h2 id="blick-title" style="font-size:1.6rem;margin-bottom:1.5rem">Auf einen Blick</h2>
        {checklist([
          "Ich gehe erst, wenn alles läuft",
          "Einzelunternehmen, immer derselbe Ansprechpartner",
          "Vor Ort und per Fernwartung",
          "Für Privathaushalte, Senioren und kleinere Unternehmen",
          "Privathaushalte: 49 € je Stunde inkl. MwSt.; Unternehmen: Wartungsvertrag",
          "In Mannheim ohne Anfahrt",
          "Termine nach Vereinbarung, auch abends und am Wochenende, telefonisch täglich von 8 bis 20 Uhr erreichbar",
          "Verständliche Erklärungen ohne Zeitdruck",
        ], "checklist checklist-2")}
        <div class="btn-row" style="margin-top:1.75rem">{btn("leistungen.html", "Leistungen für Privatkunden", arrow=True)}{btn("geschaeftskunden.html", "Leistungen für Unternehmen", arrow=True)}</div>
      </div>
    </div>
  </section>

  <section class="section section-navy" aria-labelledby="arbeit-title">
    <div class="container">
      {section_head("Haltung", "So arbeite ich", hid="arbeit-title")}
      {cards([
        ("thumbs", "Ich sage Ihnen, wenn sich etwas nicht lohnt", "Braucht ein sechs Jahre alter Laptop gleich mehrere neue Teile, sage ich Ihnen das offen, bevor Sie investieren."),
        ("file", "Schriftliche Dokumentation", "Nach größeren Aufträgen schreibe ich auf, was eingerichtet ist, welche Zugänge es gibt und wohin gesichert wird."),
        ("message", "Rückfragen jederzeit willkommen", "Auch Tage nach dem Termin erkläre ich Ihnen gern noch einmal, was eingerichtet wurde, ohne zusätzliche Kosten."),
        ("key", "Ihre Passwörter bleiben bei Ihnen", "Manche brauche ich während des Termins. Ich schreibe sie nirgends auf und speichere sie nicht."),
      ], grid="grid-4", compact=True)}
    </div>
  </section>

  <section class="section section-alt" aria-labelledby="gebiet-title">
    <div class="container area">
      <div>
        {section_head("Einsatzgebiet", "Vor Ort in Mannheim und 25 km Umkreis", left=True, hid="gebiet-title")}
        <p class="section-lead reveal" style="margin-top:-1.5rem">Mein Standort ist Mannheim-Käfertal. Von hier aus bin ich in ganz Mannheim und im Umkreis von 25 km unterwegs: von Viernheim, Ladenburg und Heidelberg bis an die Bergstraße nach Weinheim, Heppenheim und Bensheim.</p>
        {town_chips()}
      </div>
      {area_svg()}
    </div>
  </section>

  {cta_band("Am schnellsten geht es per Telefon.", "Ich freue mich auf Ihren Anruf. Alternativ erreichen Sie mich per WhatsApp oder E-Mail.",
            links=link("kontakt.html", "Alle Kontaktwege"))}
'''

# ====================================================================== KONTAKT
kontakt_body = f'''
  <section class="page-hero page-hero-simple" aria-labelledby="hero-title">
    <div class="container hero-grid">
      <div>
        <p class="eyebrow reveal">Kontakt</p>
        <h1 id="hero-title" class="reveal">IT-Service anfragen in Mannheim und Umgebung</h1>
        <p class="hero-lead reveal">Am schnellsten geht es per Telefon. In wenigen Minuten klären wir Ihr Anliegen und vereinbaren einen Termin. Sie können mir auch per WhatsApp oder E-Mail schreiben.</p>
      </div>
      {qr_card("Scannen und anrufen")}
    </div>
  </section>

  <section class="section" aria-label="Kontaktwege" style="padding-top:1rem">
    <div class="container contact-cards">
      <article class="card contact-card is-primary reveal">
        <span class="card-icon">{ic("phone")}</span>
        <h2 class="label">Anrufen</h2>
        <a class="big-link" href="{TEL}">{PHONE}</a>
        <p>Der direkteste Weg. Bin ich gerade bei einem Kunden, rufe ich Sie meist innerhalb einer Stunde zurück.</p>
      </article>
      <article class="card contact-card reveal">
        <span class="card-icon">{ic("chat")}</span>
        <h2 class="label">WhatsApp</h2>
        <a class="big-link" href="{WA}" rel="noopener">Nachricht schreiben</a>
        <p>Ideal, wenn Sie mir ein Foto vom Bildschirm oder vom Gerät senden möchten.</p>
      </article>
      <article class="card contact-card reveal">
        <span class="card-icon">{ic("mail")}</span>
        <h2 class="label">E-Mail</h2>
        <a class="big-link" href="mailto:{MAIL}">{MAIL}</a>
        <p>Für ausführlichere Anliegen. Sie bekommen meist innerhalb eines Tages Antwort.</p>
      </article>
    </div>
  </section>

  <section class="section section-alt" aria-labelledby="bereit-title">
    <div class="container split">
      <div>
        {section_head("Vorbereitung", "Halten Sie das bitte bereit", "Wenn Sie das griffbereit haben, geht der Termin schneller:", left=True, hid="bereit-title")}
        <div class="reveal">
          {checklist([
            "E-Mail-Adresse und zugehöriges Passwort",
            "WLAN-Schlüssel, steht meist auf der Rückseite des Routers",
            "Zugangsdaten Ihres Internetanbieters (Telekom, Vodafone, 1&amp;1 …)",
            "Apple-ID oder Google-Konto samt Passwort",
            "Unterlagen zu Gerät, Vertrag oder Fernsehbox",
          ])}
        </div>
        <div class="note reveal" style="margin-top:1.5rem">{ic("lock")}<div><p>Ich notiere und speichere nichts davon, die Daten bleiben bei Ihnen.</p></div></div>
      </div>
      <div class="stack">
        {note("phone", "Das hilft mir am Telefon", "Um welches Gerät geht es, seit wann ist das so, und was steht auf dem Bildschirm? Und in welchem Ort wohnen Sie? Auch wenn Sie nicht alle Angaben kennen, rufen Sie gern an.")}
        {note("clock", "Erreichbarkeit", "Telefonisch erreichen Sie mich täglich von 8 bis 20 Uhr. Termine gibt es auch abends und am Wochenende. Bin ich gerade bei einem Kunden, sprechen Sie auf die Mailbox oder schreiben per WhatsApp. Ich melde mich meist innerhalb einer Stunde.")}
        {note("message", "Verständlich erklärt", "Technisches Vorwissen ist nicht nötig. Beschreiben Sie das Problem mit Ihren eigenen Worten – Ursache und Lösung finde ich.")}
        {fern_warn()}
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="gebiet-title">
    <div class="container area">
      <div>
        {section_head("Einsatzgebiet", "IT-Service in Mannheim, Viernheim, Ladenburg, Weinheim und Umgebung", left=True, hid="gebiet-title")}
        <p class="section-lead reveal" style="margin-top:-1.5rem">Ich komme direkt zu Ihnen nach Hause. In Mannheim ohne Anfahrtspauschale, in der Umgebung gilt eine Pauschale nach Entfernung. In Viernheim, Ilvesheim, Heddesheim, Ladenburg und Weinheim bin ich regelmäßig. Softwarefragen kläre ich auch per Fernwartung. Ihr Ort ist nicht dabei? Sprechen Sie mich gern an.</p>
        {town_chips()}
        <p class="reveal" style="margin-top:1rem">{link("preise.html#anfahrt", "Anfahrtspauschalen ansehen")}</p>
      </div>
      {area_svg()}
    </div>
  </section>

  {cta_band("Rufen Sie mich an.", "Bin ich gerade im Termin, rufe ich Sie zurück, meistens innerhalb einer Stunde.",
            links=link("preise.html", "Preise ansehen"))}
'''

# ================================================================= FERNWARTUNG
TV_WIN = "https://download.teamviewer.com/download/TeamViewerQS_x64.exe"
TV_MAC = "https://download.teamviewer.com/download/TeamViewerQS.dmg"

fern_body = f'''
  <section class="page-hero" aria-labelledby="hero-title">
    <div class="container hero-grid">
      <div>
        <p class="eyebrow reveal">Fernwartung</p>
        <h1 id="hero-title" class="reveal">Fernwartung starten</h1>
        <p class="hero-lead reveal">Haben wir eine Fernwartung vereinbart? Dann laden Sie hier das kleine Programm TeamViewer QuickSupport herunter, öffnen es und rufen mich an. Eine Installation ist nicht nötig.</p>
        <div class="download-box reveal" data-download>
          <a class="btn btn-primary btn-lg" href="{TV_WIN}" rel="noopener" data-dl-main data-win="{TV_WIN}" data-mac="{TV_MAC}">{ic("download")}<span data-dl-label>Fernwartung herunterladen</span></a>
          <p class="src">Für Windows und macOS · Der Download kommt direkt vom Hersteller TeamViewer, nicht von dieser Website.</p>
          <p class="alt">Anderes System? <a href="{TV_WIN}" rel="noopener">Windows</a> · <a href="{TV_MAC}" rel="noopener">macOS</a></p>
        </div>
        <div class="mobile-hint" data-mobile-hint hidden>
          {note("smartphone", None, f'Sie sind gerade am Handy oder Tablet. Öffnen Sie diese Seite bitte am Computer, der Hilfe braucht, oder rufen Sie mich an: <a href="{TEL}">{PHONE}</a>.')}
        </div>
      </div>
      {qr_card("Danach anrufen", badge=None)}
    </div>
  </section>

  <section class="section section-navy" aria-labelledby="schritte-title">
    <div class="container">
      {section_head("In drei Schritten", "So funktioniert die Fernwartung", hid="schritte-title")}
      {steps3([
        ("Herunterladen und öffnen", "Klicken Sie auf den Knopf und öffnen Sie die heruntergeladene Datei. Unter Windows bestätigen Sie die Sicherheitsabfrage mit „Ja“, am Mac öffnen Sie die Datei per Doppelklick."),
        ("Mich anrufen", f'Im Fenster sehen Sie Ihre ID und ein Passwort. Rufen Sie mich an und lesen Sie mir beides vor: <a href="{TEL}" class="nowrap">{PHONE}</a>'),
        ("Zusehen und beenden", "Sie sehen auf Ihrem Bildschirm alles mit, was ich tue. Sie können die Sitzung jederzeit selbst beenden, indem Sie das Programm schließen. Das Passwort gilt nur für diese eine Sitzung."),
      ])}
    </div>
  </section>

  <section class="section section-alt" aria-label="Hinweise zur Fernwartung">
    <div class="container grid-2">
      {note("alert", "Nur nach Absprache", "Starten Sie eine Fernwartung nur, wenn Sie selbst mit mir gesprochen haben. Ich rufe nie unaufgefordert an und frage nie per E-Mail oder SMS nach einer ID. Meldet sich jemand so bei Ihnen, beenden Sie das Gespräch bitte sofort.", warn=True)}
      {note("info", "Kosten und Datenschutz", 'Für Privathaushalte gilt der Stundensatz ab der ersten Viertelstunde, ohne Anfahrt (<a href="preise.html">Preise</a>). Für Unternehmen gelten die Bedingungen des Wartungsvertrags. Wie TeamViewer Daten verarbeitet, steht in der <a href="datenschutz.html#fernwartung">Datenschutzerklärung</a>.')}
    </div>
  </section>
'''

PAGES2 = [
    ("preise.html", "Preise für Privat & Unternehmen | Clavis IT Service",
     "49 € pro Stunde inkl. MwSt. für Privathaushalte, Wartungsvertrag für Unternehmen ab 99 € netto je Arbeitsplatz und Monat. In Mannheim ohne Anfahrtspauschale.",
     preise_body, None, ""),
    ("ueber-mich.html", "Über mich: Eymen Kumaru | Clavis IT Service",
     "Eymen Kumaru, Inhaber von Clavis IT Service: persönliche IT-Unterstützung bei Computer, Smartphone und WLAN in Mannheim und Umgebung.",
     ueber_body, None, ""),
    ("kontakt.html", "Kontakt & Anfahrt | Clavis IT Service",
     "IT-Service anfragen: Telefon 0162 63270 36, WhatsApp oder kontakt@clavis-itservice.de. Telefonisch täglich von 8 bis 20 Uhr erreichbar, Termine nach Vereinbarung.",
     kontakt_body, None, ""),
    ("fernwartung.html", "Fernwartung starten | Clavis IT Service",
     "Fernwartung mit Clavis IT Service: TeamViewer QuickSupport herunterladen, öffnen, anrufen. Die Verbindung startet nur nach Absprache und mit Ihrer Freigabe.",
     fern_body, "", ""),
]
