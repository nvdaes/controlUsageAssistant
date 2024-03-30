# Control Usage Assistant #

* Author: Joseph Lee, Noelia Ruiz Martínez

Questo componente aggiuntivo si utilizza per scoprire come interagire con il
controllo evidenziato. Premere NVDA+h per ascoltare un breve suggerimento,
ad esempio su come attivare una casella di controllo, come operare in un
campo editazione e così via.

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

## Version 20240324.0.0

* Improved support for edit controls and suggestions.

## Version 2023.02.19

* The message configured for clickable objects will be reported after other
  properties.
* Compatible with NVDA 2023.1.

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

## Novità nella versione 20.10

* I messaggi di aiuto sono letti anche in lingue diverse dall'inglese.

## Novità nella versione 20.06

* Risolti molti problemi con il codice e bug potenziali con Flake8.
* NVDA will no longer appear to do nothing or play error tones when trying
  to obtain help for certain browse mode controls.

## Novità nella versione 20.01

* E' richiesto NVDA 2019.3 o versioni successive.

## Novità nella versione 3.0/19.11

* A partire da questa versione, lo schema per il numero di versione è
  anno.mese.
* Quando si preme NVDA+h, verrà mostrata una schermata di aiuto anziché un
  messaggio flash.

## Novità nella versione 2.5

* Compatibile con python 3.

## Novità nella versione 2.1

* Traduzioni nuove e aggiornate.

## Novità nella versione 2.0

* Aggiunti messaggi di aiuto per diversi controlli, comprese le finestre
  terminale.
* Aggiunti messaggi di aiuto per lavorare in alcune sezioni di programmi,
  come Excel, Powerpoint o le videate di avvio di Windows8.
* Aggiunti messaggi d'aiuto per utilizzare i form in modalità focus e in
  modalità navigazione con il cursore virtuale (Internet Explorer, Adobe
  Reader, Mozilla Firefox, etc.).
* Nuova lingua: danese.

## Novità nella versione 1.0

* Versione iniziale.

[[!tag dev stable]]
