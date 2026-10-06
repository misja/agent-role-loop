# Geselecteerd bewijs voor #34

Werkelijke Vibe 2.19.0-runs op 6 oktober 2026. Het [uitvoeringsregister](../34-uitvoering.md)
belegt herkomst, scope en beperkingen. Geen ruwe providertranscripten, redeneerinhoud,
credentials of accountidentiteit. Run-json bevat geselecteerde metadata, beschikbare
modeltools, daadwerkelijke toolrequests en hun fouten; een request is geen succes.
Testbestanden zijn menselijke stdout/stderr/exitcode, niet Mistral-shelluitvoer.

Hoofdketen: C0/C1/C2/C4, C5-main/C6-main, boekenplank-build en test-rood/groen.
Negatief: C5-negatief/C6-negatief, boekenplank-negatief en zwakke/volledige tests.
Herstel: C5-herstel/C6-herstel, herstel-diff/stand/controle en boekenplank-herstel.
De tellerregistratie in deze herstelrun was te laat; de documenten houden die fout
zichtbaar. Een eventuele vervolgproef krijgt eigen bronnen zonder deze te vervangen.
AGENTS-proef.md is een niet-actieve snapshot, geen nieuwe projectingang.

Reproduceer de productsuites met Python 3.10+ in een aparte map: kopieer controleer.py
en de gewenste boekenplank-variant als boekenplank.py. `python3 -B controleer.py werk
volledig` verwacht build/herstel exit0 en negatief S4fail/exit1. Deze lokale herhaling
is geen nieuwe modelaanroep of herstelronde. Commitverwijzingen wijzen naar de
lokale tijdelijke Git-repository; bron-/productbytes en hashbewijs blijven hier bewaard.
