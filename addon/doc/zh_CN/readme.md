# Control Usage Assistant-控件使用助理 #
* Author: Joseph Lee, Noelia Ruiz Martínez
* Download [stable version][1] (compatible with NVDA 2022.1 and beyond)
* Download [development version][2] (compatible with NVDA 2022.1 and beyond)

借助此插件可了解如何与当前所聚焦的控件进行交互。例如，当聚焦到复选框、编辑框时，按 NVDA+H 来获取一段有关于使用当前控件的简短帮助。

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

## 版本 21.10

* 由于对 NVDA 的更改会影响此插件，因此需要 NVDA 2021.2 或更高版本。

## 版本 20.10

* 帮助信息支持以英语以外的语言显示。

## 版本 20.06

* 使用 Flake8 解决了许多编码风格问题和潜在的错误。
* 修复了尝试获取某些浏览模式控件的帮助时， NVDA 不执行任何操作或只播放错误提示音的 Bug。

## 版本 20.01

* 需要NVDA 2019.3或更高版本。

## 版本 3.0/19.11

* 版本方案现在为year.month。
* 现在按下NVDA + H时，将显示帮助屏幕，而不是显示提示信息。

## 版本 2.5

* 兼容Python 3。

## 版本 2.1

* 新添加和更新的翻译。

## 版本 2.0

* 增加更多控件的帮助信息，包括终端窗口（命令提示符）。
* 增加一些应用程序的窗口区域帮助信息，如Microsoft Excel、Powerpoint和Windows 8 的开始屏幕。
* 在虚拟文档中增加浏览模式和焦点模式下的帮助信息，包括Internet Explorer、 Adobe Reader 、Mozilla
  Firefox等。
* 新的语言：丹麦语。

## 版本 1.0

* 发布初始版本。

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cua

[2]: https://addons.nvda-project.org/files/get.php?file=cua-dev
