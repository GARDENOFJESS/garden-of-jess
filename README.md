# Garden by Jess — Ambachtelijke Kruidenthee

Officiële webwinkel en botanische ervaring voor **Garden by Jess**, ambachtelijke theemelanges met fytotherapeutische zorg samengesteld.

## 🌿 De 6 Kenmerkende Melanges
Elk geleverd in een 50-grams aroma- en lichtwerend stazakje voor **€7,95**:
1. **Morning Rise** — Munt, lavendel, ginkgo, duizendblad, braamblad, salie, brandnetelzaad.
2. **Painless** — Moerasspirea, wilgenbast, witte peper.
3. **Refresh** — Salie, laurier, limoenblad, citroenverbena, heermoes, brandnetel.
4. **Immunitea** — Olijfblad, berkenblad, rozemarijn, cacaoboon.
5. **Smooth Digest** — Artisjok, duizendblad, steranijs, venkel.
6. **Breath Free** — Koningskaars, ijslandsmos, dropplant, wilde tijm, rode klaver.

## 📍 Fysiek Verkooppunt & Proeflokaal
- **Winkel:** G&W Gezondheidswinkel Bio Rosa
- **Adres:** Padjedijk 30, 1441 BR Purmerend
- **Telefoon:** 0299-420905

## 🚀 Live Hosting via GitHub Pages
Deze website is volledig statisch (HTML5, modern CSS3 met custom variables, responsive grid, vanilla ES6 JS) en vereist geen actieve backend server.
- Schakel GitHub Pages in via: **Settings > Pages > Branch: main / root**

## Lokaal ontwikkelen

De bewerkbare HTML staat in `_src/`. De HTML in de hoofdmap en `pages/` is de versleutelde uitvoer. `_src/` en `build_encrypted.py` zijn bewust genegeerd door Git: bewaar hiervan een privéback-up. Bewerk de gegenereerde HTML niet rechtstreeks.

1. Pas de bronpagina's aan. Gedeelde verbeteringen staan in `assets/storefront.css` en `assets/storefront.js`.
2. Voer `python build_encrypted.py` uit (vereist het Python-pakket `cryptography`).
3. Start `python -m http.server 8765 --bind 127.0.0.1` en open `http://127.0.0.1:8765`.
4. Controleer de toegangspoort, collectie, winkelmand en contactpagina. De lokale regressietest `_src/verify-storefront.cjs` gebruikt Playwright en Microsoft Edge.

De winkelmand bewaart alleen productnamen en aantallen lokaal in de browser. Prijs en afbeelding komen uit de catalogus. Online betalen is nog niet gekoppeld: de selectie gaat naar de contactpagina, waar de bezoeker zelf een e-mail kan opstellen en versturen. Er wordt geen betaling, bestelling of nieuwsbriefinschrijving verwerkt.

Zie `SITE_AUDIT.md` voor de bevindingen, uitgevoerde verbeteringen en resterende aansluitingen.
