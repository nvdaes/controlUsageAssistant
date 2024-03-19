# Control Usage Assistant/NVDA objects help messages
# An add-on for NVDA
# Copyright 2019-2021 Joseph Lee, released under GPL.

# Provides help messages for built-in NVDA objects, mirroring NVDA objects collection in NVDA Core.
# Each help message records objects to a general help message.
# This module also serves as a home for messages for overlay classes found in app modules and global plugins.
# Other add-ons should update this dictionary with help messages for their own overlay classes.

from typing import Callable

import addonHandler

addonHandler.initTranslation()

_: Callable[[str], str]

# Help messages for objects: key = string representation of a class name, value = generic help message.
# Base API classes (such as NVDAObjects.NVDAObject) are not included.
# Source: NVDA pull request for issue 2699 (context-sensitive help)

objectsHelpMessages = {
	# "NVDAObjects.behaviors.EditableTextWithSuggestions": _(
	# Translators: help text for search field in Windows 10 and other places.
	# "After typing search text, press up or down arrow keys to review list of suggestions."
	# ),
	"NVDAObjects.behaviors.EditableText": _(
		# Translators: Help message for edit boxes.
		"Use arrow keys to move the cursor across text. You may type text here."
	),
	"NVDAObjects.IAccessible.adobeAcrobat.Document": _(
		# Translators: Help message for reading Adobe PDF documents.
		"Use the browse mode and quick navigation commands to read through the PDF document."
	),
	# Translators: Help message for moving between Excel spreadsheet cells.
	"NVDAObjects.window.excel.ExcelCell": _("Use the arrow keys to move between spreadsheet cells."),
}

# In some apps, two or more controls behave the same, such as Start screen tiles in Windows 8.x.
commonAppModuleOverlayClassHelpMessages = {
	# Translators: Message for moving between Windows 8 start screen tiles (Windows 8 only).
	"appModules.explorer.StartScreenTiles": _("Use the arrow keys to move between start screen tiles."),
}

# Specific to app module overlay classes.
appModuleOverlayObjectsHelpMessages = {
	# Translators: Message for Calculator's display field.
	"appModules.calc.Display": "Enter or review calculations using Calculator commands.",
	# The below two items are really the same control type.
	"appModules.explorer.GridListTileElement": commonAppModuleOverlayClassHelpMessages[
		"appModules.explorer.StartScreenTiles"
	],
	"appModules.explorer.GridTileElement": commonAppModuleOverlayClassHelpMessages[
		"appModules.explorer.StartScreenTiles"
	],
	# Translators: Message for moving between slides in slide view
	# (a list of slides for a Powerpoint presentation).
	"appModules.powerpnt.DocumentWindow": _("Use up and down arrow keys to move between slides."),
	# Translators: Help message for working with slide shows.
	"appModules.powerpnt.SlideShowWindow": _(
		# Translators: Help message for working with slide shows.
		"Press SPACE or BACKSPACE to move between slides in the slide show. "
		"To end the slide show, press escape."
	),
}

# And combine the above two maps.
objectsHelpMessages.update(appModuleOverlayObjectsHelpMessages)
