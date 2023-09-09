# Tájékoztató üzemmód #

* Author: Joseph Lee, Noelia Ruiz Martínez

A bővítmény az NVDA+H billentyűparanccsal információkat ad a fókuszban lévő
vezérlők és elemek használatához.

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

## Version 20.10

* Help messages are announced in languages other than English.

## 20.06-os verzió

* Javítottak több kódolási hibát és lehetséges bugot.
* NVDA will no longer appear to do nothing or play error tones when trying
  to obtain help for certain browse mode controls.

## 20.01 verzió

* NVDA 2019.3 vagy újabb kiadás szükséges

## 3.0/19.11 verzió

* A verziószám mostantól az év.hónap formátumot követi.
* Az NVDA+H lenyomása után most már egy súgóablak jelenik meg és nem csak
  egy üzenet.

## 2.5 verzió

* Python 3 kompatibilitás.

## 2.1 verzió

* Új és frissített fordítások.

## 2.0 verzió

* Több súgóüzenetet is hozzáadtak, beleértve a terminál ablakhoz tartozókat.
* Több, a munkát elősegítő programhoz rendeltek hozzá súgóüzenetet, úgy mint
  a Microsoft Excel, Powerpoint és Windows 8 kezdőképernyő.
* Súgó üzeneteket adtak hozzá az űrlapokkal dolgozó alkalmazásokhoz
  (Internet explorer, Adobe reader, Mozilla Firefox, stb).
* Új nyelv: Dán

## 1.0 verzió

* Első verzió

[[!tag dev stable]]
