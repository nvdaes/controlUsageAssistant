# Control Usage Assistant #

* Author: Joseph Lee, Noelia Ruiz Martínez
* Download [stable version][1]
* NVDA compatibility: 2021.3 and later

Use this add-on to find out how to interact with the focused control.
Press NVDA+H to obtain a short help message on interacting with the focused control, such as checkboxes, edit fields and so on.

Go to NVDA's menu, Preferences submenu, Settings dialog, Control Usage Asistant category to configure add-on settings:

* Select output modes for automatic messages: This list of checkboxes allows to select speech and braille.
* Pitch change for automatic messages: This spin box allows to set the pitch change when NVDA reads automatic messages.

## Note

Be aware: automatic messages shouldn't be spoken in documents that support browse mode, but sometimes this cannot be avoided due to focus changes. To prevent this, you can disable these messages for specific applications using NVDA's configuration profiles.

## Version 2022.03.27

* Compatible with NVDA 2021.3 and later.

## Version 22.01

* Added support for automatic messages.
* Improved support for requested messages in browse mode.

## Version 21.10

* NVDA 2021.2 or later is required due to changes to NVDA that affects this add-on.

## Version 20.10

* Help messages are announced in languages other than English.

## Version 20.06

* Resolved many coding style issues and potential bugs with Flake8.
* NVDA will no longer appear to do nothing or play error tones when trying to obtain help for certain browse mode controls.

## Version 20.01

* NVDA 2019.3 or later is required.

## Version 3.0/19.11

* Version scheme is now year.month.
* When NVDA+H is pressed, a help screen will be displayed instead of a flash message being shown.

## Version 2.5

* Compatible with Python 3.

## Version 2.1

* New and updated translations.

## Version 2.0

* Help messages for more controls added, including terminal windows.
* Added help messages for working in some areas of applications, such as Microsoft Excel and Powerpoint and Windows 8 start screen.
* Added help messages for working with forms in both browse and focus modes in virtual buffer documents (Internet Explorer, Adobe Reader, Mozilla Firefox, etc.).
* New language: Danish.

## Version 1.0

* Initial version.

[1]: https://addons.nvda-project.org/files/get.php?file=cua
