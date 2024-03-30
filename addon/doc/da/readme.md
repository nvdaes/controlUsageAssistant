# Brugsassistent til kontroller #

* Author: Joseph Lee, Noelia Ruiz Martínez

Brug denne tilføjelse til at finde ud af, hvordan du interagerer med det
fokuserede kontrolelement.  Tryk på NVDA+H for at få en kort hjælp til at
interagere med det fokuserede kontrolelement, f.eks. check box og
redigeringsfelter.

Gå til NVDAs menu, undermenuen Opsætning, dialogboksen Indstillinger,
kategorien Brugsassistent til kontroller for at konfigurere
tilføjelsesindstillinger:

* Automatiske beskeder til fokus: Markeret som standard.
* Indtast beskeden, der skal bruges, når et objekt kan aktiveres: Du kan
  inkludere en kort meddelelse, der angiver standard- eller din
  konfigurerede kommando for at vide, om det aktuelle objekt har en
  tilknyttet handling, når du udfører et tastetryk som NVDA+enter i
  objektnavigation.
* Vælg output-tilstande for automatiske beskeder: Denne liste over bokse gør
  det muligt at vælge tale og punktskrift.
* Ændre toneleje for automatiske beskeder: Denne drejeknap gør det muligt at
  indstille ændringen af tonehøjden, når NVDA læser automatiske beskeder
  (fra -30 til +30).

## Version 20240324.0.0

* Improved support for edit controls and suggestions.

## Version 2023.02.19

* The message configured for clickable objects will be reported after other
  properties.
* Compatible with NVDA 2023.1.

## Version 2022.07.10

* Tilføjet mulighed for at indstille en besked til objektnavigation, for at
  meddele, om det aktuelle objekt kan aktiveres.

## Version 2022.03.27

* Kræver NVDA 2022.1 eller nyere.

## Version 22.01

* Tilføjet understøttelse af automatiske beskeder.
* Forbedret understøttelse af anmodede beskeder i browsertilstand.

## Version 21.10

* NVDA 2021.2 eller nyere er påkrævet på grund af ændringer til NVDA, der
  påvirker denne tilføjelse.

## Version 20.10

* Hjælpemeddelelser annonceres nu på andre sprog udover engelsk.

## Version 20.06

* Løst mange problemer med kodningstil og potentielle fejl med Flake8.
* NVDA vil ikke længere se ud til ikke at gøre noget eller afspille
  fejletoner, når man prøver at få hjælp til visse kontrolelementer i
  gennemsynstilstand.

## Version 20.01

* NVDA 2019.3 eller nyere er påkrævet.

## Version 3.0/19.11

* Versionskema er nu år.måned
* Når der trykkes på NVDA+H, vises der en hjælpeskærm i stedet for, at der
  vises en flashbesked.

## Version 2.5

* Kompatibel med Python 3.

## Version 2.1

* Nye og opdaterede oversættelser.

## Version 2.0

* Tilføjede hjælpemeddelelser for flere kontroller, bl.a. terminalvinduer.
* Tilføjede hjælpemeddelelser om, hvordan man arbejder med nogle områder i
  programmer, f.eks. Microsoft Excel, PowerPoint og startskærmen i Windows
  8.
* Tilføjede hjælpemeddelelser ang. hvordan man arbejder med formularer i
  både gennemsynstilstand og fokustilstand i dokumenter, som benytter en
  virtuel buffer (Internet Explorer, Adobe Reader, Mozilla Firefox, osv).
* Nyt sprog: dansk.

## Version 1.0

* Første version.

[[!tag dev stable]]
