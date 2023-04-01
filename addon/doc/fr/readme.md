# Control Usage Assistant #

* Author: Joseph Lee, Noelia Ruiz Martínez
* Download [stable version][1] (compatible with NVDA 2022.1 and beyond)

Utilisez cette extension pour savoir comment interagir avec l'élément
actif. Appuyez sur NVDA+H sur l'objet sur lequel vous souhaitez avoir cette
information.

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

* NVDA 2021.2 ou une version ultérieure est requis en raison de
  modifications apportées à NVDA qui affectent cette extension.

## Version 20.10

* Les messages d'aide sont annoncés dans d'autres langues que l'Anglais.

## Version 20.06

* Résolution de nombreux problèmes de style de codage et de bugs potentiels
  avec Flake8.
* NVDA ne semblera plus ne rien faire ni n'émettra de son d'erreur en
  essayant d'obtenir de l'aide pour certaines commandes du mode de
  navigation.

## Version 20.01

* NVDA 2019.3 ou ultérieur est requis.

## Version 3.0/19.11

* Le schéma de version est maintenant année.mois.
* Lorsqu'on presse NVDA+H, un écran d'aide s'affichera au lieu d'un message
  flash.

## Version 2.5

* Compatible avec Python 3.

## Version 2.1

* Nouvelle langues et mises à jours d'autres

## Version 2.0

* Messages d'aides ajoutés pour plus d'éléments, comme les fenêtres de
  consoles.
* Ajout de messages d'aide pour des zones d'applications, comme Microsoft
  Excel et Powerpoint ou l'écran d'accueil Windows 8.
* Ajout de message pour les formulaires dans les navigateurs en mode
  formulaire ou mode navigation (Internet Explorer, Adobe Reader, Mozilla
  Firefox, etc.).
* Nouvelle langue : Danois

## Version 1.0

* Première version

[[!tag dev stable]]

[1]:
https://addons.nvda-project.org/files/get.php?file=controlUsageAssistant
