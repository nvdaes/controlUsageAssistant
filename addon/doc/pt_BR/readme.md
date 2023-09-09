# Assistente para Uso de Controles (Control Usage Assistant) #

* Author: Joseph Lee, Noelia Ruiz Martínez

Use este complemento para descobrir como interagir com o controle
focalizado. Pressione NVDA+H para obter uma mensagem curta de ajuda sobre a
interação com o controle em foco, como caixas de seleção, campos de edição e
assim por diante.

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

## Versão 21.10

* O NVDA 2021.2 ou posterior é necessário devido a mudanças no NVDA que
  afetam este complemento.

## Versão 20.10

* As mensagens de ajuda são anunciadas em outros idiomas além do inglês.

## Versão 20.06

* Foram resolvidos muitos problemas de estilo de codificação e possíveis
  erros com o Flake8.
* O NVDA não mais parecerá não fazer nada ou reproduzir tons de erro ao
  tentar obter ajuda para certos controles do modo de navegação.

## Versão 20.01

* É necessário NVDA 2019.3 ou posterior.

## Versão 3.0/19.11

* Esquema de versões agora é ano.mês.
* Quando NVDA+H for pressionada, será exibida uma tela de ajuda ao invés de
  ser mostrada uma mensagem rápida.

## Versão 2.5

* Compatível com Python 3.

## Versão 2.1

* Traduções novas e atualizadas.

## Versão 2.0

* Adicionadas mensagens de ajuda para mais controles, incluindo janelas de
  terminal.
* Adicionadas mensagens de ajuda para trabalhar com algumas áreas de
  aplicativos, como o Microsoft Excel e Powerpoint e a tela inicial do
  Windows 8.
* Adicionadas mensagens de ajuda para trabalhar com formulários em ambos os
  modos de navegação e de foco em documentos com exibidor virtual (Internet
  Explorer, Adobe Reader, Mozilla Firefox, etc.).
* Novo idioma: Dinamarquês.

## Versão 1.0

* Versão inicial.

[[!tag dev stable]]
