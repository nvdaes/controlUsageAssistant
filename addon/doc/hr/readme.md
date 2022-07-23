# Pomoćnik za primjenu kontrola #

* Autor: Joseph Lee
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]
* NVDA kompatibilnost: 2021.2 i novija verzija

Koristi ovaj dodatak i saznaj kako koristiti fokusiranu kontrolu. Pritisni
NVDA+H za dobivanje kratke poruke o tome kako koristiti fokusirane kontrole,
kao što su potvrdni okviri, polja za uređivanje i tome slično.

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

## Verzija 21.10

* NVDA 2021.2 ili novija verzija je potrebna zbog promjena NVDA čitača koje
  utječu na ovaj dodatak.

## Verzija 20.10

* Poruke pomoći najavljuju se na jezicima koji nisu engleski.

## Verzija 20.06

* Riješeni su mnogi problemi sa stilom kodiranja kao i potencijalne greške s
  Flake8.
* NVDA se više neće ponašati kao da ništa ne radi ili reproducirat zvukove
  greške prilikom pokušaja dohvaćanja pomoći za određene kontrole u modusu
  čitanja.

## Verzija 20.01

* Potreban je NVDA 2019.3 ili noviji.

## Verzija 3.0/19.11

* Shema za određivanje verzije je sada godina.mjesec.
* Kad se pritisne NVDA+H, prikazat će se prozor pomoći umjesto poruke.

## Verzija 2.5

* Kompatibilnost s Python 3.

## Verzija 2.1

* Novi i ažurirani prijevodi.

## Verzija 2.0

* Dodane su nove poruke pomoći za daljnje kontrole, uključujući prozore
  neredbenog retka.
* Dodane su nove poruke pomoći za rad u nekim područjima aplikacija, kao što
  su Microsoft Excel i Powerpoint i Windows 8 početni ekran.
* Dodane su nove poruke pomoći za rad u modusima čitanja i fokusa za
  dokumente koji koriste virtualni spremnik (Internet Explorer, Adobe
  Reader, Mozilla Firefox, itd.).
* Novi jezik: Danski.

## Verzija 1.0

* Prva verzija.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cua

[2]: https://addons.nvda-project.org/files/get.php?file=cua-dev
