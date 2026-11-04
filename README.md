# Clavis IT Service – Website 2.0

Statische Website für Clavis IT Service (Eymen Kumaru, Mannheim): IT-Service für Privathaushalte, Senioren und kleine Unternehmen.

- 9 Seiten: Start, Unternehmen (mit Vertragsrechner), Privatkunden, Preise, Über mich, Kontakt, Fernwartung, Impressum, Datenschutz
- Reines HTML, CSS und JavaScript, kein Build-Schritt fürs Hosting
- Hell/Dunkel-Darstellung, lokale Schriften (Space Grotesk, Schibsted Grotesk, Inter), keine Cookies, kein Tracking

## Lokal ansehen

```
python -m http.server 5173
```

Dann `http://localhost:5173` im Browser öffnen.

## Inhalte ändern

Die HTML-Seiten werden aus `_generator/` erzeugt. Texte dort ändern und anschließend:

```
python -B _generator/build.py
```

Details in [`_generator/README.md`](_generator/README.md).

## Veröffentlichen

Alle Dateien außer `_generator/` und `README.md` auf den Webserver hochladen.

## Bildnachweis

Fotos von [Unsplash](https://unsplash.com) (Unsplash-Lizenz): Priscilla Du Preez, Vitaly Gariev, cornerstone accounting Services, Ritupon Baishya.
