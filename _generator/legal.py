# -*- coding: utf-8 -*-
from core import *


def legal_page(title, inner):
    return f'''
  <section class="page-hero page-hero-simple" aria-labelledby="hero-title">
    <div class="container"><h1 id="hero-title">{title}</h1></div>
  </section>
  <section class="legal">
    <div class="container">
{inner}
    </div>
  </section>
'''


impressum = legal_page("Impressum", '''
      <p class="lead">Angaben gemäß § 5 Digitale-Dienste-Gesetz (DDG).</p>

      <h2>Diensteanbieter</h2>
      <p>Eymen Kumaru<br>Clavis IT Service<br>Mannheimer Straße 57a<br>68309 Mannheim<br>Deutschland</p>

      <h2>Kontakt</h2>
      <p>Telefon: <a href="tel:+491626327036">0162 63270 36</a><br>E-Mail: <a href="mailto:kontakt@clavis-itservice.de">kontakt@clavis-itservice.de</a><br>Internet: clavis-itservice.de</p>

      <h2>Unternehmensform</h2>
      <p>Einzelunternehmen. „Clavis IT Service“ ist eine Geschäftsbezeichnung, keine eingetragene Firma. Eine Eintragung ins Handelsregister besteht nicht.</p>

      <h2>Umsatzsteuer</h2>
      <p>Die Leistungen unterliegen der Regelbesteuerung. Alle Preise für Privatkunden sind Endpreise inklusive 19 % gesetzlicher Umsatzsteuer. Preise für Unternehmen verstehen sich zuzüglich der gesetzlichen Umsatzsteuer.</p>

      <h2>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h2>
      <p>Eymen Kumaru<br>Mannheimer Straße 57a<br>68309 Mannheim</p>

      <h2>Verbraucherstreitbeilegung</h2>
      <p>Die Europäische Kommission hat ihre Plattform zur Online-Streitbeilegung (OS) zum 20. Juli 2025 eingestellt; ein Verweis darauf entfällt daher. Ich bin nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen (§ 36 Verbraucherstreit&shy;beilegungsgesetz).</p>

      <h2>Haftung für Inhalte und Links</h2>
      <p>Für eigene Inhalte bin ich nach § 7 Abs. 1 DDG verantwortlich. Für die Inhalte verlinkter Websites ist deren Anbieter verantwortlich. Erfahre ich von einem Rechtsverstoß auf dieser Seite oder in einem verlinkten Angebot, entferne ich den Inhalt bzw. den Link umgehend.</p>

      <h2>Urheberrecht</h2>
      <p>Texte und Gestaltung dieser Website unterliegen dem deutschen Urheberrecht. Wer sie über die gesetzlichen Grenzen hinaus verwenden möchte, braucht meine schriftliche Zustimmung.</p>

      <h2>Bildnachweis</h2>
      <p>Die Fotos auf dieser Website stammen, abgesehen von meinem Porträt, von Unsplash und werden unter der Unsplash-Lizenz verwendet.</p>

      <h2>Verwendete Schriftarten</h2>
      <p>Diese Website verwendet die Schriftarten Space Grotesk, Schibsted Grotesk und Inter, die alle unter der SIL Open Font License 1.1 stehen. Die Schriftdateien werden zusammen mit dieser Website ausgeliefert; eine Verbindung zu Schriftanbietern wie Google Fonts besteht nicht.</p>

      <p class="stand">Stand: November 2026</p>''')

datenschutz = legal_page("Datenschutzerklärung", '''
      <p class="lead">Diese Website kommt ohne Cookies, ohne Analyse-Werkzeuge und ohne externe Schriftarten aus. Was dennoch an Daten anfällt, steht hier.</p>

      <h2>1. Verantwortlicher</h2>
      <p>Eymen Kumaru<br>Clavis IT Service<br>Mannheimer Straße 57a<br>68309 Mannheim<br>Telefon: <a href="tel:+491626327036">0162 63270 36</a><br>E-Mail: <a href="mailto:kontakt@clavis-itservice.de">kontakt@clavis-itservice.de</a></p>

      <h2>2. Überblick: Was diese Website nicht tut</h2>
      <p>Damit Sie nicht zwischen den Absätzen suchen müssen, hier die Kurzfassung. Auf dieser Website gibt es:</p>
      <ul>
        <li>keine Cookies und keine Speicherung zu Analyse-, Werbe- oder Wiedererkennungszwecken,</li>
        <li>keine Analyse- oder Tracking-Dienste (kein Google Analytics, kein Matomo, keine Pixel),</li>
        <li>keine externen Schriftarten, alle Schriften werden zusammen mit der Website ausgeliefert,</li>
        <li>keine Karten-, Video- oder Social-Media-Einbindungen,</li>
        <li>kein Kontaktformular, keine Newsletter-Anmeldung, keine Registrierung,</li>
        <li>keine Weitergabe von Daten zu Werbezwecken.</li>
      </ul>
      <p>Es gibt daher nichts, wozu Sie einwilligen müssten, und deshalb steht auf dieser Website auch kein Einwilligungsbanner.</p>
      <p>Eine einzige Angabe wird lokal in Ihrem Browser abgelegt (localStorage, Eintrag clavis-theme): Ihre Auswahl zwischen heller und dunkler Darstellung. Sie entsteht nur, wenn Sie den Schalter in der Kopfzeile betätigen, und dient allein dazu, die Seite beim nächsten Aufruf so anzuzeigen, wie Sie es eingestellt haben. Sie verlässt Ihr Gerät nicht, wird nicht an mich übertragen und lässt keinen Rückschluss auf Ihre Person zu. Sie können sie jederzeit löschen, indem Sie die Websitedaten in Ihrem Browser entfernen.</p>

      <h2>3. Hosting und Aufruf der Website</h2>
      <p>Diese Website wird über GitHub Pages bereitgestellt, einen Dienst von GitHub. Für Nutzerinnen und Nutzer im Europäischen Wirtschaftsraum ist dies die GitHub B.V., Prins Bernhardplein 200, 1097 JB Amsterdam, Niederlande; Muttergesellschaft ist die GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA.</p>
      <p>Beim Aufruf dieser Website verarbeitet GitHub technisch notwendige Daten, die Ihr Browser übermittelt, insbesondere Ihre IP-Adresse, Datum und Uhrzeit des Zugriffs, die abgerufene Datei sowie Browser- und Geräteangaben. GitHub nutzt diese Daten, um die Website auszuliefern und die Sicherheit des Dienstes zu gewährleisten, und speichert sie dafür in eigenen Protokolldateien. Auf diese Protokolle habe ich keinen Zugriff; die IP-Adressen kann ich daher weder kürzen noch auswerten.</p>
      <p><strong>Zweck und Rechtsgrundlage:</strong> Zuverlässige, schnelle und sichere Bereitstellung dieser Website. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse).</p>
      <p><strong>Übermittlung in die USA:</strong> Dabei können Daten an die GitHub, Inc. in den USA übermittelt werden. GitHub ist nach dem EU-U.S. Data Privacy Framework zertifiziert; die Übermittlung stützt sich auf den Angemessenheitsbeschluss der EU-Kommission (Art. 45 DSGVO).</p>
      <p><strong>Speicherdauer:</strong> Wie lange GitHub die Zugriffsdaten speichert, richtet sich nach der Datenschutzerklärung von GitHub (docs.github.com/site-policy/privacy-policies/github-general-privacy-statement).</p>

      <h2>4. Verschlüsselung</h2>
      <p>Diese Website nutzt eine SSL- bzw. TLS-Verschlüsselung, erkennbar am „https://“ in der Adresszeile und am Schloss-Symbol Ihres Browsers. Daten, die Sie an diese Website übermitteln, können dadurch nicht von Dritten mitgelesen werden.</p>

      <h2>5. Kontaktaufnahme</h2>
      <h3>5.1 Telefon und E-Mail</h3>
      <p>Wenn Sie mich anrufen oder mir schreiben, werden Ihre Rufnummer bzw. E-Mail-Adresse und die Angaben, die Sie mitteilen, zur Bearbeitung Ihres Anliegens verarbeitet. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO (vorvertragliche Maßnahmen bzw. Vertragserfüllung), im Übrigen Art. 6 Abs. 1 lit. f DSGVO. Bitte beachten Sie, dass unverschlüsselte E-Mails auf dem Übertragungsweg grundsätzlich von Dritten gelesen werden könnten.</p>
      <p>Mein E-Mail-Postfach liegt bei Microsoft 365. Anbieter ist die Microsoft Ireland Operations Limited, One Microsoft Place, South County Business Park, Leopardstown, Dublin 18, Irland. E-Mails an mich werden dort gespeichert. Eine Übermittlung an die Microsoft Corporation in den USA ist möglich. Die Microsoft Corporation ist nach dem EU-U.S. Data Privacy Framework zertifiziert; die Übermittlung stützt sich auf den Angemessenheitsbeschluss der EU-Kommission (Art. 45 DSGVO).</p>
      <h3>5.2 WhatsApp</h3>
      <p>Auf dieser Website finden Sie Verweise auf WhatsApp. Es handelt sich um reine Verlinkungen. Beim Aufruf der Seite werden keine Daten an WhatsApp oder Meta übertragen und keine Inhalte von dort geladen.</p>
      <p>Wenn Sie mir per WhatsApp schreiben, erhalte ich Ihre Nachricht in der App WhatsApp Business auf meinem Smartphone. Anbieter ist die WhatsApp Ireland Limited, Merrion Road, Dublin 4, D04 X2K5, Irland. Dabei werden Ihre Rufnummer, Ihr WhatsApp-Profilname und der Inhalt Ihrer Nachrichten verarbeitet. Die Nachrichten selbst sind Ende-zu-Ende-verschlüsselt, WhatsApp verarbeitet aber Nutzungs- und Verbindungsdaten. Dabei können Daten an die WhatsApp LLC und die Meta Platforms, Inc. in den USA übermittelt werden. Beide sind nach dem EU-U.S. Data Privacy Framework zertifiziert (Art. 45 DSGVO). Auf Umfang und Zweck dieser Verarbeitung durch WhatsApp habe ich keinen Einfluss.</p>
      <p>Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO (Ihre Anfrage bzw. Ihr Auftrag), im Übrigen Art. 6 Abs. 1 lit. f DSGVO (mein berechtigtes Interesse, Anfragen auf dem Weg zu beantworten, den Sie selbst gewählt haben). Die Nutzung ist freiwillig. Sie erreichen mich genauso gut per Telefon oder E-Mail.</p>
      <h3>5.3 Speicherdauer</h3>
      <p>Anfragen, aus denen kein Auftrag entsteht, lösche ich spätestens nach sechs Monaten. Daten aus abgeschlossenen Aufträgen bewahre ich auf, solange gesetzliche Aufbewahrungspflichten bestehen, insbesondere die handels- und steuerrechtlichen Fristen von sechs bzw. zehn Jahren (§ 257 HGB, § 147 AO).</p>

      <h2>6. Datenverarbeitung beim Einsatz vor Ort</h2>
      <p>Bei der Arbeit an Ihren Geräten kann es unvermeidbar sein, dass ich personenbezogene Daten zur Kenntnis nehme, etwa Dateinamen, E-Mails oder Fotos. Dafür gilt:</p>
      <ul>
        <li>Ich sehe mir ausschließlich das an, was zur Lösung Ihres Problems erforderlich ist.</li>
        <li>Ich fertige keine Kopien Ihrer Daten an, außer Sie beauftragen mich ausdrücklich damit (z. B. bei einer Datensicherung oder einem Geräteumzug).</li>
        <li>Zugangsdaten und Passwörter, die Sie mir für die Einrichtung nennen, notiere und speichere ich nicht. Sie werden ausschließlich während des Termins verwendet.</li>
        <li>Alle Informationen, die mir dabei bekannt werden, behandle ich vertraulich.</li>
      </ul>
      <p>Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO (Erfüllung des mit Ihnen geschlossenen Vertrags).</p>

      <h2 id="fernwartung">7. Fernwartung</h2>
      <p>Auf Ihren ausdrücklichen Wunsch biete ich Unterstützung per Fernwartung an. Dabei wird eine verschlüsselte Verbindung zu Ihrem Gerät aufgebaut, über die ich Ihren Bildschirm sehen und, soweit Sie das freigeben, Eingaben vornehmen kann.</p>
      <ul>
        <li>Die Verbindung kommt nur auf Ihre aktive Freigabe hin zustande; ohne Ihre Zustimmung ist kein Zugriff möglich.</li>
        <li>Sie sehen während der gesamten Sitzung alles auf Ihrem eigenen Bildschirm mit.</li>
        <li>Sie können die Sitzung jederzeit selbst beenden.</li>
        <li>Nach dem Ende der Sitzung besteht kein Zugriff mehr. Ich richte keine dauerhaften Zugänge ein.</li>
        <li>Es werden keine Bildschirmaufzeichnungen angefertigt und keine Daten von Ihrem Gerät kopiert.</li>
      </ul>
      <p>Für den Verbindungsaufbau nutze ich TeamViewer (TeamViewer Germany GmbH, Bahnhofsplatz 2, 73033 Göppingen, Deutschland). Dabei verarbeitet TeamViewer technische Verbindungsdaten, z. B. IP-Adresse, Geräte- und Sitzungskennung, Zeitpunkt und Dauer. Nach eigenen Angaben überträgt TeamViewer Daten im Allgemeinen nicht aus der EU bzw. dem EWR hinaus; Ausnahmen (etwa in die USA oder nach Australien) sichert TeamViewer mit EU-Standardvertragsklauseln ab. Rechtsgrundlage ist Art. 6 Abs. 1 lit. a DSGVO (Ihre Einwilligung) sowie Art. 6 Abs. 1 lit. b DSGVO (Vertragserfüllung). Sie sind nicht verpflichtet, Fernwartung zu nutzen, der Vor-Ort-Termin bleibt jederzeit die gleichwertige Alternative.</p>
      <p>Das Programm TeamViewer QuickSupport laden Sie über die Seite <a href="fernwartung.html">„Fernwartung starten“</a> direkt von den Servern von TeamViewer herunter, nicht von dieser Website. Beim Klick auf den Download-Link übermittelt Ihr Browser dafür Ihre IP-Adresse und technische Browserdaten an TeamViewer.</p>

      <h2>8. Empfänger von Daten</h2>
      <p>Eine Weitergabe Ihrer Daten findet nur statt, soweit dies zur Vertragserfüllung erforderlich ist oder gesetzliche Vorgaben es verlangen, etwa an das Finanzamt oder an ein Steuerbüro im Rahmen der Buchführung. Außerdem setze ich die oben genannten Dienstleister ein: GitHub (Bereitstellung dieser Website), Microsoft (E-Mail), WhatsApp (Nachrichten) und TeamViewer (Fernwartung). Eine Weitergabe zu Werbezwecken erfolgt nicht.</p>

      <h2>9. Ihre Rechte</h2>
      <p>Sie haben jederzeit das Recht:</p>
      <ul>
        <li>Auskunft über die zu Ihrer Person gespeicherten Daten zu verlangen (Art. 15 DSGVO),</li>
        <li>die Berichtigung unrichtiger Daten zu verlangen (Art. 16 DSGVO),</li>
        <li>die Löschung Ihrer Daten zu verlangen, soweit keine Aufbewahrungspflichten entgegenstehen (Art. 17 DSGVO),</li>
        <li>die Einschränkung der Verarbeitung zu verlangen (Art. 18 DSGVO),</li>
        <li>Ihre Daten in einem gängigen Format zu erhalten (Datenübertragbarkeit, Art. 20 DSGVO),</li>
        <li>der Verarbeitung aus Gründen Ihrer besonderen Situation zu widersprechen, soweit sie auf Art. 6 Abs. 1 lit. f DSGVO beruht (Art. 21 DSGVO),</li>
        <li>eine erteilte Einwilligung jederzeit zu widerrufen, mit Wirkung für die Zukunft (Art. 7 Abs. 3 DSGVO).</li>
      </ul>
      <p>Dafür genügt eine formlose Nachricht an <a href="mailto:kontakt@clavis-itservice.de">kontakt@clavis-itservice.de</a>.</p>

      <h2>10. Beschwerderecht bei der Aufsichtsbehörde</h2>
      <p>Wenn Sie der Ansicht sind, dass die Verarbeitung Ihrer Daten gegen die DSGVO verstößt, können Sie sich bei einer Datenschutz-Aufsichtsbehörde beschweren. Zuständig ist der Landesbeauftragte für den Datenschutz und die Informationsfreiheit Baden-Württemberg, Lautenschlagerstraße 20, 70173 Stuttgart.</p>

      <h2>11. Keine automatisierte Entscheidungsfindung</h2>
      <p>Eine automatisierte Entscheidungsfindung einschließlich Profiling nach Art. 22 DSGVO findet nicht statt.</p>

      <h2>12. Änderungen dieser Erklärung</h2>
      <p>Diese Datenschutzerklärung wird angepasst, sobald sich die Rechtslage oder die tatsächliche Datenverarbeitung ändert. Für einen erneuten Besuch gilt jeweils die dann veröffentlichte Fassung.</p>

      <p class="stand">Stand: Oktober 2026</p>''')

PAGES3 = [
    ("impressum.html", "Impressum | Clavis IT Service",
     "Impressum und Anbieterkennzeichnung nach § 5 DDG für Clavis IT Service, Eymen Kumaru, Mannheim.", impressum, "", ""),
    ("datenschutz.html", "Datenschutzerklärung | Clavis IT Service",
     "Datenschutzerklärung nach DSGVO für Clavis IT Service. Keine Cookies, keine Analyse-Tools, keine externen Schriftarten.", datenschutz, "", ""),
]
