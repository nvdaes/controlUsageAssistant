# Control Usage Assistant #

* Autor: Joseph Lee, Noelia Ruiz Martínez
* Descargar [versión estable][1] (compatible con NVDA 2022.1 e posterior)

Utiliza este complemento para atopar como interactuar co control enfocado.
Preme NVDA+H para obter unha mensaxe curta de axuda na interacción co
control enfocado, como caixas de verificación, campos de edición etc.

Vai ó menú de NVDA, submenú Preferencias, diálogo Opcións, categoría Control
Usage Assistant para configurar as opcións do complemento:

* Mensaxes automáticas para o foco: Marcada por defecto.
* Escribe a mensaxe que se utilizará cando un obxecto poida ser activado:
  Poderías incluír unha mensaxe curta indicando o xesto por defecto ou aquel
  que configurases para saber se o obxecto ten unha acción asociada cando se
  prema NVDA+intro na navegación de obxectos.
* Selecciona modos de saída para mensaxes automáticas: Esta listaxe de
  caixas de verificación permite seleccionar fala e braille.
* Cambio de ton para mensaxes automáticas: Este deslizador permite
  establecer o cambio de ton cando NVDA lea mensaxes automáticas (de -30 a
  +30).

## Version 2023.02.19

* The message configured for clickable objects will be reported after other
  properties.
* Compatible with NVDA 2023.1.

## Versión 2022.07.10

* Engadida a posibilidade de configurar unha mensaxe para a navegación por
  obxectos, para anunciar se o obxecto actual se pode activar.

## Versión 2022.03.27

* Require NVDA 2022.1 ou posterior.

## Versión 22.01

* Engadido soporte para mensaxes automáticas.
* Mellorado o soporte para as mensaxes solicitadas en modo exploración.

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

[1]:
https://addons.nvda-project.org/files/get.php?file=controlUsageAssistant
