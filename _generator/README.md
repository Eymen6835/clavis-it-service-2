# Seitengenerator – Clavis IT Service

Die HTML-Seiten im Projektordner werden aus diesen Python-Dateien erzeugt.
**Änderungen bitte hier machen, nicht direkt in den `.html`-Dateien** – sonst werden sie beim nächsten Erzeugen überschrieben.

## Seiten neu erzeugen

Im Projektordner ausführen (Python 3.12 oder neuer, keine Zusatzpakete nötig):

```
python -B _generator/build.py
```

Danach sind alle 9 `.html`-Dateien und `assets/img/icons.svg` aktuell.

## Wo steht was?

| Datei | Inhalt |
|---|---|
| `core.py` | Kontaktdaten (Telefon, WhatsApp, E-Mail), Kopf- und Fußbereich, Navigation, Icons, wiederkehrende Bausteine (QR-Karte, Abschluss-Kasten, FAQ, Karten, Einsatzgebiet) |
| `pages1.py` | Start, Unternehmen (inkl. Vertragsrechner `CALC_ITEMS`), Privatkunden |
| `pages2.py` | Preise, Über mich, Kontakt, Fernwartung (TeamViewer-Links `TV_WIN` / `TV_MAC`) |
| `legal.py` | Impressum, Datenschutzerklärung |
| `build.py` | Schreibt alle Seiten |

Gestaltung und Verhalten liegen unabhängig davon in `assets/css/styles.css` und `assets/js/main.js`.

## Häufige Änderungen

- **Telefonnummer / E-Mail:** oben in `core.py` (`PHONE`, `TEL`, `WA`, `MAIL`). Die QR-Code-Grafik `assets/img/qr-anrufen.svg` muss bei neuer Nummer separat neu erzeugt werden.
- **Preise im Rechner:** `CALC_ITEMS` in `pages1.py`. Den Mindestbetrag (199 €) zusätzlich in `assets/js/main.js` (`MIN`) anpassen.
- **Fotos einsetzen:** Die Platzhalter erzeugt die Funktion `photo()` in `core.py`. An der jeweiligen Stelle in `pages1.py` / `pages2.py` den `photo(...)`-Aufruf durch ein Bild ersetzen, z. B.
  `<div class="portrait"><img src="assets/img/portrait.webp" alt="Eymen Kumaru" width="640" height="800"></div>`
