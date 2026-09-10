#!/usr/bin/env python3
"""
=====================================================================
  GARDEN BY JESS — EIGEN BEVEILIGINGSTEST (BRUTE FORCE DEMO)
  Lokale aanval op de eigen versleutelde site om de kwetsbaarheid
  van een 4-cijferige pincode te demonstreren.
  
  !! UITSLUITEND VOOR EIGEN GEBRUIK OP EIGEN SITE !!
=====================================================================
"""

import json
import base64
import time
import sys
from pathlib import Path

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend

# ─── Instellingen ────────────────────────────────────────────────
HTML_BESTAND = Path(__file__).parent / "index.html"
ITERATIES    = 100_000

# ─── Terminal kleuren ────────────────────────────────────────────
ROOD   = "\033[91m"; GROEN  = "\033[92m"
GEEL   = "\033[93m"; BLAUW  = "\033[94m"
RESET  = "\033[0m";  VET    = "\033[1m"

# ─── Banner ─────────────────────────────────────────────────────
def print_banner():
    print(f"""
{BLAUW}{VET}╔══════════════════════════════════════════════════════════╗
║    🔒 GARDEN BY JESS — EIGEN BEVEILIGINGSTEST            ║
║       Brute Force Demonstrator (4-cijferige pincode)      ║
╚══════════════════════════════════════════════════════════╝{RESET}
""")

# ─── Payload laden ───────────────────────────────────────────────
def laad_payload(pad: Path) -> dict:
    html = pad.read_text(encoding="utf-8")
    start = html.find('{\n  "salt"')
    if start == -1:
        start = html.find('{"salt"')
    if start == -1:
        raise ValueError("Versleuteld payload-blok niet gevonden in de HTML.")
    einde = html.find("</script>", start)
    return json.loads(html[start:einde].strip())

# ─── Eén code proberen ───────────────────────────────────────────
def probeer(code: str, salt: bytes, iv: bytes, ct: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32,
        salt=salt, iterations=ITERATIES, backend=default_backend()
    )
    sleutel = kdf.derive(code.encode("utf-8"))
    try:
        return AESGCM(sleutel).decrypt(iv, ct, None).decode("utf-8")
    except Exception:
        return None

# ─── Voortgangsbalk ──────────────────────────────────────────────
def balk(huidig, totaal, tempo=0, breedte=38):
    gevuld  = int(breedte * huidig / totaal)
    lijn    = "█" * gevuld + "░" * (breedte - gevuld)
    print(f"\r  [{lijn}] {huidig:04d}/{totaal}  {tempo:.0f}/s  ", end="", flush=True)

# ─── Hoofd-aanval ────────────────────────────────────────────────
def brute_force(start=0, eind=9999):
    print_banner()

    if not HTML_BESTAND.exists():
        print(f"{ROOD}  ✗ Bestand niet gevonden: {HTML_BESTAND}{RESET}")
        sys.exit(1)

    payload = laad_payload(HTML_BESTAND)
    salt = base64.b64decode(payload["salt"])
    iv   = base64.b64decode(payload["iv"])
    ct   = base64.b64decode(payload["ciphertext"])

    totaal = eind - start + 1
    print(f"  📂 Bestand:         {HTML_BESTAND.name}")
    print(f"  🧂 Salt:            {payload['salt']}")
    print(f"  🔑 IV:              {payload['iv']}")
    print(f"  📦 Ciphertext:      {len(ct):,} bytes")
    print(f"  🔁 Iteraties:       {ITERATIES:,}  (PBKDF2-SHA256)")
    print(f"  🎯 Aanvalsbereik:   {start:04d} – {eind:04d}  ({totaal:,} codes)")
    print()

    antwoord = input(f"  {GEEL}Start de aanval? (j/n): {RESET}").strip().lower()
    if antwoord not in ("j", "ja", "y", "yes"):
        print(f"\n  {BLAUW}Aanval geannuleerd.{RESET}\n")
        sys.exit(0)

    print()
    begintijd = time.time()
    gevonden  = None

    for i, num in enumerate(range(start, eind + 1), 1):
        code = f"{num:04d}"

        # Voortgangsbalk elke 5 pogingen
        if i % 5 == 0:
            verstreken = time.time() - begintijd
            tempo = i / verstreken if verstreken > 0 else 0
            balk(i, totaal, tempo)

        resultaat = probeer(code, salt, iv, ct)
        if resultaat:
            gevonden = (code, resultaat)
            break

    verstreken = time.time() - begintijd
    pogingen   = (int(gevonden[0]) - start + 1) if gevonden else totaal
    tempo      = pogingen / verstreken if verstreken > 0 else 0

    print(f"\n\n{'─'*60}")

    if gevonden:
        code, html = gevonden
        print(f"""
{GROEN}{VET}  ✅ TOEGANGSCODE GEKRAAKT!{RESET}

  🔓 Code:          {VET}{code}{RESET}
  ⏱  Tijd:          {verstreken:.1f} seconden
  🚀 Tempo:         {tempo:.0f} pogingen/seconde
  📊 Pogingen:      {pogingen:,} van de {totaal:,}

{ROOD}{VET}  ⚠️  BEWIJS: Met een 4-cijferige pincode is AES-256-GCM
     gekraakt in slechts {verstreken:.0f} sec — zonder enige server te raken!
{RESET}""")

        # Sla ontsleutelde HTML op ter verificatie
        uitvoer = HTML_BESTAND.parent / "DEMO_ontsleuteld.html"
        uitvoer.write_text(html, encoding="utf-8")
        print(f"  💾 Ontsleutelde HTML:  {uitvoer.name}")
        print(f"     Open dit bestand in de browser om de volledige winkel te zien.")

    else:
        print(f"""
{ROOD}  ✗ Niet gevonden in bereik {start:04d}–{eind:04d}{RESET}
  ⏱  Tijd: {verstreken:.1f}s  |  Tempo: {tempo:.0f}/s  |  Pogingen: {pogingen:,}
""")

    print(f"\n{'─'*60}")
    print(f"""
{GEEL}{VET}  🛡️  AANBEVELING:{RESET}
  Vervang de 4-cijferige pincode door een lange wachtzin, bv:

    {GROEN}"Lavendel&Rozemarijn2026!"{RESET}

  Dit maakt offline brute-force aanvallen miljoenen jaren
  tijdrovend — zelfs met GPU-clusters.
""")

# ─── Ingangspunt ─────────────────────────────────────────────────
if __name__ == "__main__":
    s = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    e = int(sys.argv[2]) if len(sys.argv) > 2 else 9999
    brute_force(s, e)
