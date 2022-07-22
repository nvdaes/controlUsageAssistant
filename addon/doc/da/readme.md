# Brugsassistent til kontroller #

* Forfatter: Joseph Lee
* Download [stabil version][1]
* Download [development version][2]
* NVDA compatibility: 2021.2 and later

Brug denne tilføjelse til at finde ud af, hvordan du interagerer med det
fokuserede kontrolelement.  Tryk på NVDA+H for at få en kort hjælp til at
interagere med det fokuserede kontrolelement, f.eks. check box og
redigeringsfelter.

Go to NVDA's menu, Preferences submenu, Settings dialog, Control Usage
Asistant category to configure add-on settings:

* Automatic messages for focus: Checked by default.
* Type the message to be used when an object can be activated: You may
  include a short message indicating the default or your configured gesture
  to know if the current object has an associated action when pressing a
  gesture like NVDA+enter in object navigation.
* Select output modes for automatic messages: This list of checkboxes allows
  to select speech and braille.
* Pitch change for automatic messages: This spin box allows to set the pitch
  change when NVDA reads automatic messages (from -30 to +30).

## Version 2022.07.10

* Added ability to set a message for object navigation, to announce if the
  current object can be activated.

## Version 2022.03.27

* Requires NVDA 2022.1 or later.

## Version 22.01

* Added support for automatic messages.
* Improved support for requested messages in browse mode.

## Version 21.10

* NVDA 2021.2 or later is required due to changes to NVDA that affects this
  add-on.

## Version 20.10

* Hjælpemeddelelser annonceres nu på andre sprog udover engelsk.

## Version 20.06

* Løst mange problemer med kodningstil og potentielle fejl med Flake8.
* NVDA will no longer appear to do nothing or play error tones when trying
  to obtain help for certain browse mode controls.

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

[1]: https://addons.nvda-project.org/files/get.php?file=cua

[2]: https://addons.nvda-project.org/files/get.php?file=cua-dev
