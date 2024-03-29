# Assistente para Uso de Controlos #

* Author: Joseph Lee, Noelia Ruiz Martínez

Utilize este extra para descobrir como interagir com o controlo sob o foco.
Pressione NVDA+H para obter uma breve mensagem de ajuda sobre como interagir
com os controlos sob o foco, tais como caixas de verificação, campos de
edição e assim por diante.

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

## Versão 21.10

* É necessário o NVDA 2021.2 ou posterior devido a alterações do NVDA que
  afectam este extra.

## Versão 20.10

* As mensagens de ajuda são anunciadas em outras línguas para além do
  inglês.

## Versão 20.06

* Resolvidos vários problemas de estilo de codificação e potenciais bugs com
  Flake8.
* O NVDA deixará de parecer não fazer nada ou reproduzir tons de erro ao
  tentar obter ajuda para certos controlos do modo de navegação.

## Versão 20.01

* Requere o NVDA 2019.3 ou posterior.

## Versão 3.0/19.11

* O esquema da versão é agora ano.mês.
* Quando o atalho NVDA+H é pressionado, será mostrado um ecrã de ajuda em
  vez de ser mostrada uma mensagem flash.

## Versão 2.5

* Compatível com Python 3.

## Versão 2.1

* Traduções novas e actualizadas.

## Versão 2.0

* Mensagens de ajuda para mais controlos adicionados, incluindo janelas de
  terminal.
* Adicionadas mensagens de ajuda para trabalhar em algumas áreas de
  aplicativos, como o Microsoft Excel e Powerpoint e o Ecrã de início do
  Windows 8.
* Adicionadas mensagens de ajuda para trabalhar com formulários nos modos de
  navegação e foco em documentos de buffer virtuais (Internet Explorer,
  Adobe Reader, Mozilla Firefox, etc.).
* Novo idioma: dinamarquês.

## Versão 1.0

* Versão inicial.

[[!tag dev stable]]
