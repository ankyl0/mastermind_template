# Mastermind

Nyckelord: Datastrukturer, kontrollstruktur, Enklare AI

## Uppgiften

### Lydelse

Du ska skriva ett program som spelar det klassiska brädspelet Master Mind. I brädspelet så jobbar man med färgglada pluppar, men på datorn kör vi med siffror istället för att göra det lite svårare.

Användaren skriver in en talsekvens på fyra siffror, där varje siffra är mellan 0 och 9. Därefter är det datorns tur att gissa fram vad talsekvensen var. Det skulle kunna se ut såhär:

![image](https://user-images.githubusercontent.com/101513815/224567472-86cee8c5-5d97-4e81-9461-70429be30f65.png)

Programmet läser ett svar och kodar det till heltal genom att låta varje R vara värt 10 och varje F värt 1, t ex RFF blir 12. 

Så här kan programmet gå tillväga för att få fram sina gissningar:

Alla gamla gissningar och motsvarande svarskoder sparas. För att en gissning ska vara en rimlig lösning måste följande gälla:

1. Talet ska bestgå av fyra olika siffror.
2. Talet ska ge samma svarskod som varje gammal gissning fick som svar.

Programmet börjar med att gissa på 1023 (det första fyrsiffriga talet med fyra olika siffror). Nästa gång måste programmet välja en gissning som inte mätsäger någon av de tidigare gissningar (t ex genom att stega igenom talen från 1023 till 9876 och ta det första som uppfyller kraven ovan). Om v itittar lite näramre på detta exempel så ser vi att 1245 var programmets senaste gissning.

- Programmet ska nu söka efter ett tal som är större än 1245 och består av fyra olika siffror.
- När programmet hittat ett sådant tal (t.ex. 1246), jämför det detta med de gamla gissningarna.
  - 1023 (första gissningen) i jämförelse med 1246 ger koden 11 (RF)
  - 1245 (andra gissningen) i jämförelse med 1246 ger koden 30 (RRR) men den skulle givit 20 (RR)
- 1246 förkastas alltså, eftersom den inte gav rätt svarskod på andra gissningen.
- 1247, 1248, 1249 och 1250 förkastas av samma skäl. 1251 har inte fyra olika siffror. Programmet måste räkna upp till 1267 innan det hittar en bra gissning.
  - 1023 (första gissningen) i jämförelse med 1267 ger koden 11 (RF)
  - 1245 (andra gissningen) i jämförelse med 1267 ger koden 20 (RR)
- Alltså är 1267 en rimlig gissning och programmet skriver ut denna.

När ingen rimlig gissning existerar, ska programmet tala om detta.

Tips: Skriv en funktion compare(guess_one, guess_two) som returnerar svarskoden som erhålls då vi jämför två gissningar.

### Extralydelse

Låt gärna programmet gå att spela med ombytta roller, dvs du ska gissa på vad datorn har valt för fyrsiffrig kombination.

Exempel:

![image](https://user-images.githubusercontent.com/101513815/224567949-2e46612a-1a2a-4713-bdc8-7d780cc3693e.png)


### Krav för olika betyg

Det här är på A-nivå.

## Dokumentation & Planering

### Loggbok

Under arbetet förväntas du föra loggbok. Varje inlägg bör innehålla vad du gjort under passet och hur det gått. Skriv även gärna om du uppnått någon av milstolparna i projektplaneringen, använd gärna då ID:n för referens. Få gärna med eventuella problem du stött på och hur du löst dem (ifall du gjort det).

### Projektplan

Du påbörjar ditt projekt med att planera. Detta görs genom en projektplan med milstolpar och grindhål som ska uppnås under arbetets gång. Din projektplan bör revideras minst tre gånger under arbetet för att nå högsta bedömning. Projektplanen ska vara utförlig med detaljerade mål och uppgifter samt när deadline för dessa sker och vad som ska göras.

Projektplanen är det Google Sheet-arket som finns på classroom.

### Flödesschema

I första stadiet av projektet bör du även skissa upp ett flödesschema i förslagsvis draw.io som ska tillhöra ditt program. Tänk på vad de olika symbolerna betyder, samt att du inte har överflödiga punkter i schemat, eller att det är oläsbart.

## Författare

Niclas Lund

## Disclaimer

Uppgiften (eller inspiration till den) är ärligt stulen från EECS-skolan (gamla CSC) och kursen DD1314.
