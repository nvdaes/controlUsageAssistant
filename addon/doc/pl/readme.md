# Control Usage Assistant #

* Autor: Joseph Lee
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]
* Zgodność z NVDA: 2021.2 i nowsze

Użyj tego dodatku, aby dowiedzieć się w jaki sposób pracować z aktualną
kontrolką.  Naciśnij NvDA+H aby uzyskać krótką pomoc dotyczącą używania
bieżącej kontrolki, (pola wyboru, pola edycji, itd.)

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

## Wersja 21.10

* NVDA 2021.2 lub nowsza jest wymagana ze względu na zmiany w NVDA, które
  mają wpływ na ten dodatek.

## Wersja 20.10

* Wiadomości pomocy są ogłaszane w językach innych niż angielski.

## Wersja20.06

* Naprawiono mnóstwo błędów dotyczących stylu samego kodu oraz potencjalnych
  błędów dotyczących Lintera flake8.
* NVDA nie będzie już wydawać się nic robić ani odtwarzać dźwięków błędów
  podczas próby uzyskania pomocy dla niektórych elementów sterujących trybem
  przeglądania.

## Wersja 20.01

* Wymagana jest wersja NVDA 2019.3 lub nowsza.

## Wersja 3.0/19.11

* Shemat wersji teraz jest rok.miesiąc.
* Gdy skrót NVDA+H jest naciśnięty, Zamiast komunikatu błyskawicznego,
  pokazywane jest okno pomocy.

## Wersja 2.5

* Zgodny z Pythonem 3.

## Wersja 2.1

* Nowe i zaktualizowane tłumaczenia.

## Wersja 2.0

* Dodane instrukcje dla większej liczby kontrolek w tym dotyczące okna
  terminala.
* Dodane instrukcje jak pracować w niektórych obszarach aplikacji, w tym
  Microsoft Excel i Powerpoint oraz na ekranie startowym Windows 8.
* Dodane instrukcje jak pracować z formularzami w trybie czytania i trybie
  formularza (Internet Explorer, Adobe Reader, Mozilla Firefox, etc.).
* Nowy język: duński.

## Wersja 1.0

* Pierwsza wersja.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cua

[2]: https://addons.nvda-project.org/files/get.php?file=cua-dev
