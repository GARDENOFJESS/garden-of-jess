import subprocess
import os
import sys

html_content = """<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8">
  <title>Garden by Jess - DTC eCommerce Store Improvement Plan</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
    
    @page {
      size: A4;
      margin: 12mm 14mm 14mm 14mm;
    }
    
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      color: #2D3823;
      background: #FFFFFF;
      font-size: 8.8pt;
      line-height: 1.4;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }

    .header {
      border-bottom: 2px solid #6B7A55;
      padding-bottom: 10px;
      margin-bottom: 14px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }
    .brand-title {
      font-family: 'Cormorant Garamond', Georgia, serif;
      font-size: 22pt;
      font-weight: 700;
      color: #2D3823;
      line-height: 1;
      letter-spacing: 0.5px;
    }
    .brand-subtitle {
      font-size: 8pt;
      text-transform: uppercase;
      letter-spacing: 1.6px;
      color: #6B7A55;
      font-weight: 600;
      margin-top: 3px;
    }
    .doc-meta {
      text-align: right;
      font-size: 7.8pt;
      color: #66725A;
      line-height: 1.3;
    }
    .doc-badge {
      display: inline-block;
      background: #F0ECE1;
      color: #38462B;
      padding: 2px 7px;
      border-radius: 4px;
      font-weight: 700;
      font-size: 7pt;
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 3px;
    }

    h1, h2, h3 {
      font-family: 'Cormorant Garamond', Georgia, serif;
      color: #2D3823;
      page-break-after: avoid;
    }
    h2 {
      font-size: 12.5pt;
      border-left: 3px solid #6B7A55;
      padding-left: 8px;
      margin: 12px 0 6px 0;
      line-height: 1.2;
    }
    h3 {
      font-size: 10pt;
      margin: 8px 0 4px 0;
      color: #3E4B31;
    }

    p { margin-bottom: 5px; }
    ul { margin-left: 15px; margin-bottom: 6px; }
    li { margin-bottom: 3px; }

    .summary-box {
      background: #F9F8F5;
      border: 1px solid #E5E0D5;
      border-radius: 6px;
      padding: 10px 12px;
      margin-bottom: 10px;
    }
    .summary-box li {
      margin-bottom: 4px;
    }
    .summary-box strong {
      color: #24301C;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      margin: 6px 0 10px 0;
      font-size: 7.2pt;
      line-height: 1.25;
    }
    th {
      background: #3B4A2F;
      color: #FFFFFF;
      text-align: left;
      padding: 4.5px 5px;
      font-weight: 600;
      letter-spacing: 0.3px;
      font-size: 6.8pt;
      text-transform: uppercase;
    }
    td {
      padding: 4px 5px;
      border-bottom: 1px solid #EBE7DF;
      vertical-align: top;
    }
    tr:nth-child(even) td {
      background: #FBFBF9;
    }

    .p0-badge {
      background: #FDE8E8;
      color: #9B1C1C;
      font-weight: 700;
      padding: 1.5px 4px;
      border-radius: 3px;
      display: inline-block;
      font-size: 6.8pt;
    }
    .p1-badge {
      background: #FEF08A;
      color: #713F12;
      font-weight: 700;
      padding: 1.5px 4px;
      border-radius: 3px;
      display: inline-block;
      font-size: 6.8pt;
    }
    .p2-badge {
      background: #E0E7FF;
      color: #3730A3;
      font-weight: 700;
      padding: 1.5px 4px;
      border-radius: 3px;
      display: inline-block;
      font-size: 6.8pt;
    }

    .grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      margin-bottom: 8px;
    }
    .card {
      background: #FAF9F6;
      border: 1px solid #E8E4DA;
      border-radius: 5px;
      padding: 7px 9px;
    }
    .card h4 {
      font-family: 'Cormorant Garamond', Georgia, serif;
      font-size: 10pt;
      color: #2D3823;
      margin-bottom: 3px;
      border-bottom: 1px dashed #D3CCBE;
      padding-bottom: 2px;
    }

    .page-break { page-break-before: always; }

    .footer-note {
      margin-top: 14px;
      padding-top: 6px;
      border-top: 1px solid #E5E0D5;
      font-size: 7.2pt;
      color: #7D8872;
      display: flex;
      justify-content: space-between;
    }
  </style>
</head>
<body>

  <!-- ==================== PAGINA 1 ==================== -->
  <div class="header">
    <div>
      <div class="brand-title">GARDEN by Jess</div>
      <div class="brand-subtitle">DTC eCommerce Store Improvement & Growth Plan</div>
    </div>
    <div class="doc-meta">
      <div class="doc-badge">Strategisch Groeidocument</div>
      <div><strong>Domein:</strong> gardenbyjess.store</div>
      <div><strong>Datum:</strong> September 2026</div>
      <div><strong>Locatie:</strong> Padjedijk 30, Purmerend</div>
    </div>
  </div>

  <h2>1. Executive Summary</h2>
  <div class="summary-box">
    <ul>
      <li><strong>Laagdrempelig Proefpakket (De Ontdekkingstuin):</strong> Momenteel worden uitsluitend losse 50g zakjes (€7,95) aangeboden. Voor nieuwe theekopers is de drempel om direct 6 zakjes te kopen voor gratis verzending (€45) te hoog. Een <em>Ontdekkingstuin Proefbox</em> (6x 10g voor €14,95) verhoogt de first-time buyer conversieratio met naar schatting 35–45%.</li>
      <li><strong>Directe Betalingsgateway (iDEAL & Apple Pay):</strong> De cart drawer werkt soepel qua client-side state, maar ontbeert een live transactiekoppeling (Mollie/Stripe). iDEAL vertegenwoordigt >70% van de Nederlandse transacties; directe koppeling is de absolute P0-voorwaarde voor omzet.</li>
      <li><strong>AOV Verhogers in de Cart Drawer:</strong> Het huidige gat tussen één zakje (€7,95) en gratis verzending (€45) is €37,05. Door in-cart 1-klik accessoires (RVS zeefje €4,95, maatschepje €3,50) en bundels ("Kies 3 voor €21,95") te tonen, stijgt de AOV naar schatting van ~€12 naar >€28.</li>
      <li><strong>Kruidenwijzer Quiz als E-mail Lead Machine:</strong> De quiz toont nu direct resultaten. Door een e-mailpoort in te richten ("Ontvang je persoonlijke theevoorschrift + 10% welkomstkorting"), bouwt de shop geautomatiseerd een gekwalificeerde e-maillijst op.</li>
      <li><strong>Herhaal- & Abonnementsservice (PostNL Brievenbuspakje):</strong> Een 50g zakje (ca. 25 koppen) is bij een dagelijkse drinker na 3-4 weken leeg. Een maandelijkse herhaalservice per brievenbuspost verhoogt de Customer Lifetime Value (LTV) met >120%.</li>
    </ul>
  </div>

  <h2>2. Assumptions & Missing Info</h2>
  <div class="grid-2">
    <div class="card">
      <h4>Gehanteerde Aannames</h4>
      <ul>
        <li><strong>Logistiek:</strong> PostNL brievenbuspakje met Track & Trace (~€4,15) is primair; gratis verzending staat ingesteld op €45.</li>
        <li><strong>Technologie:</strong> Snelle statische single-page frontend (HTML/CSS/JS met AES-256 staging bescherming), gereed voor headless Mollie/Stripe of Shopify.</li>
        <li><strong>Doelgroep:</strong> Bewuste theedrinkers (28–60 jaar), fytotherapie-geïnteresseerden, lokale Purmerendse bezoekers en cadeauzoekers.</li>
        <li><strong>Regelgeving:</strong> Conform NVWA/Skal geen bio-claims, focus op ambachtelijke kwaliteit, 100% natuurzuiverheid en laboratoriumtests.</li>
      </ul>
    </div>
    <div class="card">
      <h4>Aanvullende Data voor Verdere Verfijning</h4>
      <ul>
        <li>Huidige bezoekersaantallen en conversieratio (CR%).</li>
        <li>Verhouding mobiel vs. desktop verkeer (ervaringscijfer DTC thee: ~75% mobiel).</li>
        <li>Huidige brutomarges per blend voor het berekenen van maximale bundelkortingen.</li>
        <li>Omvang van eventuele bestaande offline klantenbestanden in Purmerend.</li>
      </ul>
    </div>
  </div>

  <div class="footer-note">
    <div>Garden by Jess • Ambachtelijke Theemakerij • Padjedijk 30, Purmerend</div>
    <div>Pagina 1 van 3 • Strategisch Groeidocument</div>
  </div>

  <div class="page-break"></div>

  <!-- ==================== PAGINA 2: TABEL VOLLEDIG ==================== -->
  <div class="header">
    <div>
      <div class="brand-title">GARDEN by Jess</div>
      <div class="brand-subtitle">Prioritized Improvements • Top 15 Actiepunten</div>
    </div>
    <div class="doc-meta">
      <div><strong>Status:</strong> P0 / P1 / P2 Roadmap</div>
      <div><strong>Domein:</strong> gardenbyjess.store</div>
    </div>
  </div>

  <h2>3. Prioritized Improvements (Top 15 Actiepunten)</h2>
  <table>
    <thead>
      <tr>
        <th style="width: 5%;">Prio</th>
        <th style="width: 13%;">Domein</th>
        <th style="width: 20%;">Knelpunt</th>
        <th style="width: 25%;">Aanbevolen Wijziging</th>
        <th style="width: 21%;">Waarom Belangrijk</th>
        <th style="width: 9%;">Impact / Moeite</th>
        <th style="width: 7%;">Owner</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="p0-badge">P0</span></td>
        <td><strong>Cart & Checkout</strong></td>
        <td>Geen actieve betaalgateway achter 'Afrekenen'</td>
        <td>Koppel Mollie (iDEAL, Bancontact, Apple Pay, Klarna) of Shopify Checkout</td>
        <td>Zonder betaling geen omzet; iDEAL vereist voor >70% van de NL markt</td>
        <td>High / Med</td>
        <td>Dev</td>
      </tr>
      <tr>
        <td><span class="p0-badge">P0</span></td>
        <td><strong>Merchandising</strong></td>
        <td>Alleen losse 50g zakjes (€7,95); geen starter-optie</td>
        <td>Lanceer 'De Ontdekkingstuin' Proefbox (6x 10g voor €14,95)</td>
        <td>Verlaagt instapdrempel dramatisch voor twijfelende nieuwe theeliefhebbers</td>
        <td>High / Low</td>
        <td>Founder</td>
      </tr>
      <tr>
        <td><span class="p0-badge">P0</span></td>
        <td><strong>Lead Capture</strong></td>
        <td>Kruidenwijzer Quiz toont uitslag zonder lead capture</td>
        <td>Vraag e-mailadres vóór het advies met belofte van 10% welkomstkorting</td>
        <td>Bouwt geautomatiseerd een hoogwaardige e-maildatabase van theekopers op</td>
        <td>High / Low</td>
        <td>Growth</td>
      </tr>
      <tr>
        <td><span class="p1-badge">P1</span></td>
        <td><strong>Cart Drawer</strong></td>
        <td>Verzenddrempel (€45) is te ver weg vanaf 1 zakje (€7,95)</td>
        <td>In-cart 1-klik upsells: RVS fijnmazig theezeefje (€4,95) & Maatschepje (€3,50)</td>
        <td>Dicht het gat naar gratis verzending en stuwt AOV direct boven de €20</td>
        <td>High / Med</td>
        <td>Dev / CRO</td>
      </tr>
      <tr>
        <td><span class="p1-badge">P1</span></td>
        <td><strong>Product UX</strong></td>
        <td>Zetinstructies en smaakprofielen verborgen in modal</td>
        <td>Toon 3 snelle visuele tags op de productkaart (95°C • 8-10 min • Cafeïnevrij)</td>
        <td>Kopers zien in 1 oogopslag hoe de thee bereid wordt zonder extra kliks</td>
        <td>Med / Low</td>
        <td>UI/UX</td>
      </tr>
      <tr>
        <td><span class="p1-badge">P1</span></td>
        <td><strong>E-mail & Retentie</strong></td>
        <td>Geen geautomatiseerde welkomst- en zetbegeleiding</td>
        <td>Activeer 4-delige e-mail flow (Bevestiging -> Zetgids PDF -> Smaakcheck -> Refill d21)</td>
        <td>Thee is een verbruiksproduct; herinneren stimuleert herhaalaankopen</td>
        <td>High / Med</td>
        <td>Retention</td>
      </tr>
      <tr>
        <td><span class="p1-badge">P1</span></td>
        <td><strong>Bundels</strong></td>
        <td>Geen volumevoordeel bij meerdere smaken</td>
        <td>Introduceer 'Duo / Trio Ritueel: 3 zakjes naar keuze voor €21,95 (bespaar €1,90)'</td>
        <td>Verhoogt directe orderwaarde en stimuleert kennismaking met meerdere blends</td>
        <td>High / Low</td>
        <td>Merchandiser</td>
      </tr>
      <tr>
        <td><span class="p1-badge">P1</span></td>
        <td><strong>Social Proof</strong></td>
        <td>Reviews zijn statisch geformatteerd</td>
        <td>Koppel Kiyoh, WebwinkelKeur of Trustpilot met geverifieerde kopers</td>
        <td>Externe verificatie overtuigt twijfelende kopers bij eerste aankoop</td>
        <td>Med / Med</td>
        <td>Dev</td>
      </tr>
      <tr>
        <td><span class="p1-badge">P1</span></td>
        <td><strong>Local Omnichannel</strong></td>
        <td>Fysieke locatie Padjedijk 30 niet kiesbaar bij afrekenen</td>
        <td>Voeg optie 'Gratis afhalen in Theemakerij Purmerend' toe in cart</td>
        <td>Verwijdert verzendkosten voor streekgenoten en brengt mensen naar de winkel</td>
        <td>Med / Low</td>
        <td>Dev</td>
      </tr>
      <tr>
        <td><span class="p2-badge">P2</span></td>
        <td><strong>Abonnementen</strong></td>
        <td>Geen automatische herhaalservice</td>
        <td>Lanceer 'Vast Theeritueel': maandelijkse brievenbuslevering met 10% voordeel</td>
        <td>Creëert voorspelbare maandelijkse recurring revenue (MRR) en hoge LTV</td>
        <td>High / High</td>
        <td>Founder / Dev</td>
      </tr>
      <tr>
        <td><span class="p2-badge">P2</span></td>
        <td><strong>Cadeaumarkt</strong></td>
        <td>Geen geschenkverpakking voor feestdagen/verjaardagen</td>
        <td>Bied luxe kraft geschenkdoos met handgeschreven kaartje aan (+€2,95)</td>
        <td>Thee is een traditioneel cadeauproduct; verhoogt marges en bereik</td>
        <td>Med / Med</td>
        <td>Merchandiser</td>
      </tr>
      <tr>
        <td><span class="p2-badge">P2</span></td>
        <td><strong>SEO & Content</strong></td>
        <td>Kruiden-ABC mist gerichte commerciële zoekintenties</td>
        <td>Creëer landingspagina's voor intenties: 'thee voor de maag', 'avondthee zonder cafeïne'</td>
        <td>Trekt gratis organisch zoekverkeer van mensen met concrete behoeften</td>
        <td>Med / Med</td>
        <td>SEO</td>
      </tr>
      <tr>
        <td><span class="p2-badge">P2</span></td>
        <td><strong>Mobile CRO</strong></td>
        <td>Mobiele sticky balk linkt alleen naar algemene sectie</td>
        <td>Maak mobiele balk dynamisch: toont '+ In Zakje' van de actieve theesoort</td>
        <td>Verkort frictie op mobiel drastisch en verhoogt mobiele add-to-cart rate</td>
        <td>Med / Med</td>
        <td>Dev</td>
      </tr>
      <tr>
        <td><span class="p2-badge">P2</span></td>
        <td><strong>Interactieve UX</strong></td>
        <td>Zetinstructies zijn statische tekst</td>
        <td>Bouw een 1-klik 'Start Zettimer' (8 of 10 min) met subtiel zen-geluid</td>
        <td>Unieke beleving; zorgt dat kopers de site openhouden tijdens het zetten</td>
        <td>Low / Low</td>
        <td>Dev</td>
      </tr>
      <tr>
        <td><span class="p2-badge">P2</span></td>
        <td><strong>Kwaliteit & Zuiverheid</strong></td>
        <td>Achtergrondverhaal kruidenzuiverheid kan sterker</td>
        <td>Publiceer een transparante pagina 'Laboratoriumkwaliteit & Zuiverheid'</td>
        <td>Bouwt diep vertrouwen op zonder riskante bio-claims conform wetgeving</td>
        <td>Med / Low</td>
        <td>Content</td>
      </tr>
    </tbody>
  </table>

  <div class="footer-note">
    <div>Garden by Jess • Ambachtelijke Theemakerij • Padjedijk 30, Purmerend</div>
    <div>Pagina 2 van 3 • Strategisch Groeidocument</div>
  </div>

  <div class="page-break"></div>

  <!-- ==================== PAGINA 3: ROADMAP, TESTS & KPIS ==================== -->
  <div class="header">
    <div>
      <div class="brand-title">GARDEN by Jess</div>
      <div class="brand-subtitle">Quick Wins, A/B Testing & 90-Dagen Roadmap</div>
    </div>
    <div class="doc-meta">
      <div><strong>Doelgroep:</strong> DTC Theeliefhebbers</div>
      <div><strong>Status:</strong> Implementatieplan</div>
    </div>
  </div>

  <h2>4. Quick Wins (&le; 1 Week Uitvoerbaar)</h2>
  <div class="grid-2">
    <div class="card">
      <h4>1. Visuele Zetsymbolen</h4>
      <p>Plaats op alle 6 productkaarten 3 duidelijke icoontjes: <strong>95°C</strong> (temperatuur), <strong>8-10 min</strong> (trektijd) en <strong>Cafeïnevrij</strong>.</p>
    </div>
    <div class="card">
      <h4>2. Smaakprofiel-Tags</h4>
      <p>Voeg subtiele smaaknotities toe onder elke naam (bijv. <em>Morning Rise: Pepermunt, Ginkgo, Bloemig</em> | <em>Smooth Digest: Venkel, Anijs</em>).</p>
    </div>
    <div class="card">
      <h4>3. Brievenbus-Duidelijkheid</h4>
      <p>Benadruk in de winkelmand: <em>"Past gewoon door de brievenbus — je hoeft er niet voor thuis te blijven!"</em> (PostNL Brievenbuspakje).</p>
    </div>
    <div class="card">
      <h4>4. Gratis Afhalen Purmerend</h4>
      <p>Plaats in checkout/winkelmand een radio-optie voor gratis ophalen aan de Theemakerij (Padjedijk 30, Purmerend).</p>
    </div>
    <div class="card">
      <h4>5. Cadeau-notitie Vinkje</h4>
      <p>Voeg een optie toe in de winkelwagen: <em>"Cadeautje? Wij voegen gratis een handgeschreven kaartje toe"</em> met een invoerveld.</p>
    </div>
    <div class="card">
      <h4>6. WhatsApp Theeadvies Knop</h4>
      <p>Plaats een discrete knop voor direct theeadvies van Jess: <em>"Twijfel je over welke blend bij je past? Vraag het Jess via WhatsApp"</em>.</p>
    </div>
  </div>

  <h2>5. A/B Test Hypotheses</h2>
  <table>
    <thead>
      <tr>
        <th style="width: 25%;">Test Concept</th>
        <th style="width: 35%;">Hypothese</th>
        <th style="width: 25%;">Variant A vs B</th>
        <th style="width: 15%;">Primaire KPI</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. Hero CTA: Los vs Proefbox</strong></td>
        <td>Nieuwe bezoekers converteren sneller op een compleet proefpakket van alle 6 smaken dan op losse zakjes.</td>
        <td>A: 'Ontdek de 6 Melanges'<br>B: 'Bestel de Proefbox (6 smaken voor €14,95)'</td>
        <td>Add-to-Cart & Conversieratio</td>
      </tr>
      <tr>
        <td><strong>2. Verzenddrempel Motivator</strong></td>
        <td>Een drempel van €45 is te hoog bij een order van 1 zakje (€7,95). Een '3 zakjes voor gratis brievenbuspost' verhoogt AOV sneller.</td>
        <td>A: Gratis verzending vanaf €45<br>B: Gratis brievenbuspost bij 3 zakjes (€23,85)</td>
        <td>Gemiddelde Orderwaarde (AOV)</td>
      </tr>
      <tr>
        <td><strong>3. Kruidenwijzer Lead Wall</strong></td>
        <td>Het vragen van een e-mailadres vóór de uitslag levert een hoge leadstroom op zonder dat de kooppercentage daalt.</td>
        <td>A: Directe weergave uitslag<br>B: E-mail invoer voor uitslag + 10% korting</td>
        <td>E-mail Capture Rate & Sales</td>
      </tr>
    </tbody>
  </table>

  <h2>6. 90-Dagen Uitvoeringsroadmap & KPI Matrix</h2>
  <div class="grid-2">
    <div class="card">
      <h4>Fasegewijze Planning</h4>
      <p><strong>Weken 1–2 (Fundering & Checkout):</strong> Betaalkoppeling met iDEAL/Apple Pay live zetten. Proefbox 'De Ontdekkingstuin' toevoegen aan catalogus. Zetsymbolen op kaarten.</p>
      <p><strong>Weken 3–4 (Mandwaarde & Omnichannel):</strong> In-cart upsells (theezeefje, maatschepje). Afhalen Purmerend activeren. E-mail capture op Kruidenwijzer en 3-delige welkomstflow.</p>
      <p><strong>Maand 2 (Review & Cadeau):</strong> Extern reviewsysteem koppelen. Cadeauverpakking activeren. Lokale SEO pagina's voor Purmerend en kruidenzoektermen.</p>
      <p><strong>Maand 3 (Recurrent & Schaal):</strong> Vast Theeritueel abonnement lanceren per brievenbuspakje. Seizoensspecial introduceren. Start gerichte Instagram ads.</p>
    </div>
    <div class="card">
      <h4>Doel-KPI's (Meetdoelen)</h4>
      <ul style="margin-top: 3px;">
        <li><strong>Conversieratio (CR%):</strong> Doel &ge; 2.8% – 3.5% (DTC theebenchmark)</li>
        <li><strong>Gemiddelde Orderwaarde (AOV):</strong> Doel &ge; €24,50 (gestuwd door 3-packs en zeefjes)</li>
        <li><strong>Cart Abandonment:</strong> Doel &le; 60% (door iDEAL + brievenbusduidelijkheid)</li>
        <li><strong>Quiz Lead Capture:</strong> Doel &ge; 45% e-mailconversie op voltooide quizzen</li>
        <li><strong>Herhaalaankopen (90 dagen):</strong> Doel &ge; 25% van alle eerste kopers</li>
        <li><strong>Customer Lifetime Value (LTV):</strong> Doel &ge; €65,00 over 12 maanden</li>
      </ul>
    </div>
  </div>

  <div class="footer-note">
    <div>Garden by Jess • Ambachtelijke Theemakerij • Padjedijk 30, Purmerend</div>
    <div>Pagina 3 van 3 • Strategisch Groeidocument • https://gardenbyjess.store</div>
  </div>

</body>
</html>
"""

temp_html = os.path.abspath('report_temp.html')
output_pdf = os.path.abspath('Garden_by_Jess_eCommerce_Audit_Plan.pdf')

with open(temp_html, 'w', encoding='utf-8') as f:
    f.write(html_content)

browser_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
cmd = [
    browser_exe,
    '--headless',
    '--disable-gpu',
    '--no-pdf-header-footer',
    f'--print-to-pdf={output_pdf}',
    temp_html
]

subprocess.run(cmd, check=True)
print('Optimized 3-page PDF generated! Size:', os.path.getsize(output_pdf), 'bytes')
try:
    os.remove(temp_html)
except:
    pass
