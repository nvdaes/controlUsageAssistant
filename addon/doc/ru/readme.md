# Control Usage Assistant #

* Автор: Joseph Lee, Noelia Ruiz Martínez

Use this add-on to find out how to interact with the focused control.  Press
NVDA+H to obtain a short help message on interacting with the focused
control, such as checkboxes, edit fields and so on.

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

## Версия 20240324.0.0

* Improved support for edit controls and suggestions.

## Версия 2023.02.19

* The message configured for clickable objects will be reported after other
  properties.
* Compatible with NVDA 2023.1.

## Версия 2022.07.10

* Added ability to set a message for object navigation, to announce if the
  current object can be activated.

## Версия 2022.03.27

* Requires NVDA 2022.1 or later.

## Версия 22.01

* Added support for automatic messages.
* Improved support for requested messages in browse mode.

## Версия 21.10

* NVDA 2021.2 or later is required due to changes to NVDA that affects this
  add-on.

## Версия 20.10

* Help messages are announced in languages other than English.

## Версия 20.06

* Resolved many coding style issues and potential bugs with Flake8.
* NVDA will no longer appear to do nothing or play error tones when trying
  to obtain help for certain browse mode controls.

## Версия 20.01

* NVDA 2019.3 or later is required.

## Версия 3.0/19.11

* Схема версий теперь год.месяц.
* When NVDA+H is pressed, a help screen will be displayed instead of a flash
  message being shown.

## Версия 2.5

* Совместимо с Python 3.

## Версия 2.1

* Новые и обновленные переводы.

## Версия 2.0

* добавлены несколько сообщений для некоторых элементов управления, в том
  числе окна терминала.
* Добавлены сообщения справки для работы в некоторых областях приложений,
  таких как Microsoft Excel и Powerpoint и стартовый экран Windows 8.
* Добавлены сообщения справки для работы с формами в обоих режимах, обзора и
  редактирования, в виртуальных буферах документов (Internet Explorer, Adobe
  Reader, Mozilla Firefox и др.).
* Новый язык: датский.

## Версия 1.0

* Начальная версия.

[[!tag dev stable]]
