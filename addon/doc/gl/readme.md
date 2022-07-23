# Control Usage Assistant #

* Autor: Joseph Lee
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]
* Compatibilidade con NVDA: 2021.2 en diante

Utiliza este complemento para atopar como interactuar co control enfocado.
Preme NVDA+H para obter unha mensaxe curta de axuda na interacción co
control enfocado, como caixas de verificación, campos de edición etc.

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

## Versión 21.10

* Requírese NVDA 2021.2 ou posterior debido a cambios en NVDA que afectan a
  este complemento.

## Versión 20.10

* As mensaxes de axuda anúncianse en idiomas diferentes do inglés.

## Versión 20.06

* Resoltas varias incidencias de estilo do código e erros potenciais con
  Flake8.
* NVDA xa non parecerá non facer nada ou reproducirá tons de erro ao tentar
  obter axuda para certos controis en modo exploración.

## Versión 20.01

* Requírese NVDA 2019.3 ou posterior.

## Versión 3.0/19.11

* O esquema de versionado é agora ano.mes.
* Cando se prema NVDA+H, amosarase unha xanela de axuda no canto dunha
  mensaxe efímera.

## Versión 2.5

* Compatible con Python 3.

## Versión 2.1

* Traduccións novas e actualizadas.

## Versión 2.0

* Engadidas mensaxes de axuda para máis controis, incluindo a terminal de
  windows.
* Engadidas mensaxes para traballar nalgunhas áreas de aplicacións, como
  Microsoft Excel e PowerPoint e para a pantalla de inicio do Windows 8.
* Engadidas mensaxes de axuda para traballar cos formularios nos modos
  navegar e foco nos documentos do modo virtual (Internet Explorer, Adobe
  Reader, Mozilla Firefox, etc.).
* Nova lingua: Danés.

## Versión 1.0

* Versión inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cua

[2]: https://addons.nvda-project.org/files/get.php?file=cua-dev
