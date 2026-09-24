# Garden by Jess — audit en verbeteringen

Datum: 24 september 2026. Scope: lokale broncode en gegenereerde website; geen publicatie.

## Projectstructuur

- Statische HTML, inline CSS en JavaScript; geen npm-app of actieve backend.
- `_src/` bevat de lokale, onversleutelde bron. `build_encrypted.py` genereert zeven versleutelde pagina's met een toegangspoort.
- `assets/` bevat productfotografie, merkbeelden, kruidengegevens en scripts.
- `snippets/` en `templates/` bevatten Shopify Liquid; deze draaien niet op de statische site.
- Drukwerkbestanden en PDF-documenten staan naast de website. Deze zijn niet allemaal achter de toegangspoort geplaatst.

## Uitgevoerd

- Kortere hero met duidelijke smaakbeschrijving en prijs; bestaande botanische uitstraling behouden.
- Gedeelde CSS voor focusmarkeringen, grotere bedieningselementen, mobiel en minder beweging.
- Winkelmand begint leeg, bewaart de gekozen producten, ondersteunt meer/minder per product en toont een bruikbare lege toestand.
- Productdetails en collectie voegen dezelfde productidentiteit toe; geen dubbele regels door genummerde namen.
- Opgeslagen productgegevens worden gecontroleerd; prijzen en afbeeldingen worden uit de catalogus hersteld.
- Collectiefilter gebruikt geen impliciete globale `event` meer en communiceert de actieve keuze.
- Dialogen krijgen labels, focusbeheer, Escape, Tab-begrenzing en scrollvergrendeling. Gesloten panelen zijn inert.
- FAQ is met toetsenbord bedienbaar. Skiplink, live winkelmandtotalen en uitgesteld laden van productafbeeldingen toegevoegd.
- De oude afrekenlink bevestigde een bestelling zonder transactie. Deze leidt nu met de selectie naar contact en vermeldt duidelijk dat online betalen nog niet beschikbaar is.
- Contact opent een e-mailconcept en claimt geen verzending. De nieuwsbrief die alleen een alert toonde is vervangen door een contactlink.
- De gegenereerde poort heeft een invoerlabel en foutmelding voor hulptechnologie. Na succesvolle ontsleuteling verschijnt niet nogmaals de oude toegangspoort.

## Verificatie

De lokale Playwright-test controleert de gegenereerde site in Microsoft Edge: toegang, lege winkelmand, aantallen en totaal, dezelfde melange vanuit details, herstel na herladen, selectie op contact, filters, verwijderen, breedtes 375/768/1024/1440, mobiel menu, Escape/Tab en reduced motion. Ook JavaScript-syntax en Git-whitespace gecontroleerd. Dit is geen volledige WCAG- of prestatiecertificering.

## Openstaande punten voor de eigenaar

1. **Betalen en bestellingen:** kies en configureer een echte checkout/provider, voorraad- en bestelverwerking. De huidige contactroute vraagt uitsluitend informatie aan.
2. **Contact:** controleer de bestaande mailbox `care@gardenbyjess.store`. Een e-mailconcept vereist een geconfigureerde mailapp; een serverformulier is nog niet aangesloten.
3. **Inhoud controleren:** de bestaande reviewaantallen, keuringsclaims, verpakkingseigenschappen, levertijden en gezondheidsinhoud hebben geen onderliggende bewijsstukken in deze audit. Bevestig deze inhoud voor publicatie.
4. **Privacytekst:** noemt diensten en gegevensverwerking die niet allemaal in deze statische implementatie zijn aangesloten. Laat deze aansluiten op de werkelijk gekozen diensten.
5. **Vindbaarheid:** de versleutelde pagina's zijn niet als normale winkelpagina's leesbaar voor crawlers. `robots.txt` verwijst bovendien naar Shopify-routes en sitemaps die niet als lokale bestanden bestaan. Stem dit af op de gewenste publieke lancering.
6. **Bronbeheer:** bron en bouwer zijn lokaal en Git-genegeerd. Bewaar ze privé; een clone van de publieke repo alleen is niet voldoende voor regeneratie. De bestaande korte toegangscode en browseropslag zijn alleen geschikt voor dit besloten voorbeeld, niet voor klantaccounts.
7. **Documentatie:** oude Markdown-artikelen gebruiken andere productnamen/prijzen dan de huidige collectie; werk die bij voordat ze opnieuw worden gebruikt.

Geen externe formulieren verstuurd, geen betaling uitgevoerd en geen Git push of deployment gedaan.
