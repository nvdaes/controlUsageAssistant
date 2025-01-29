# Control Usage Assistant/control types help messages
# An add-on for NVDA
# Copyright 2019-2021 Joseph Lee, released under GPL.

# Provides help messages for control roles and states, mirroring control types module in NVDA Core.
# Each help messages dictionary records control roles and help messages.
# If specific states are found, help messages will come from state-specific subsets.

from typing import Callable

import controlTypes
import addonHandler

addonHandler.initTranslation()

_: Callable[[str], str]

# Default help messages for controls: key = role, value = messages.
# Source: NVDA pull request for issue 2699 (context-sensitive help)

controlTypeHelpMessages = {
	# Translators: Help message for a checkbox.
	controlTypes.Role.CHECKBOX: _("Press space bar to check or uncheck this check box."),
	# Translators: Help message for working with radio buttons.
	controlTypes.Role.RADIOBUTTON: _("Use the arrow keys to choose a radio button."),
	# Translators: Help message for a list box.
	controlTypes.Role.STATICTEXT: _("Use the arrow keys to read this box."),
	# Translators: Help message for an edit field.
	controlTypes.Role.EDITABLETEXT: _("Type text here."),
	# Translators: Help message for a button.
	controlTypes.Role.BUTTON: _("Press SPACE or ENTER to activate this button."),
	# Translators: Help message for menu items.
	controlTypes.Role.MENUITEM: _("Use the arrow keys to move between the menu items."),
	# Translators: Help message for pop-up menu (so-called context menu, activated by presing Applications key).
	controlTypes.Role.POPUPMENU: _("Use up and down arrow keys to move through options in the pop-up menu."),
	controlTypes.Role.COMBOBOX: _(
		# Translators: Help message for a combo box.
		"Use the arrow keys to move among choices in the combo box until the desired option is found.",
	),
	# Translators: Help message for a list view.
	controlTypes.Role.LISTITEM: _("Use the arrow keys to move to the next or previous item in this list."),
	# Translators: Help message for activating links.
	controlTypes.Role.LINK: _("Press SPACE or ENTER to activate this link."),
	controlTypes.Role.TREEVIEWITEM: _(
		# Translators: Help message for working with tree view items.
		"Use the up and down arrow keys to select the items. "
		"Use left arrow to collapse and right arrow to expand.",
	),
	controlTypes.Role.TAB: _(
		# Translators: Help message for navigating tabs,
		# such as various property tabs for drive properties in My Computer.
		"Use the left and right arrow keys to move between tabs, "
		"or press control+tab for next tab and control+shift+tab for previous tab.",
	),
	controlTypes.Role.SLIDER: _(
		# Translators: Help message for working with slider controls such as volume mixer in Windows 7.
		"Use the left and down arrow keys to decrease "
		"and up and right arrow keys to increase the value in this slider. "
		"Use page up and page down to increase or decrease in larger values, "
		"and press home and end keys to select maximum and minimum value.",
	),
	# Translators: Help message for working with progress bars.
	controlTypes.Role.PROGRESSBAR: _("This is a progress bar, used to show progress of an operation."),
	# Translators: Help message for navigating tables.
	controlTypes.Role.TABLE: _(
		"Press control, alt and arrow keys together to move between rows and columns."
	),
	controlTypes.Role.TABLECELL: _(
		# Translators: Help message for navigating table cells.
		"Press Control+Alt+arrow keys to other table cells. "
		"Pressing left or right arrow keys will navigate between columns, "
		"and up and down arrow keys will navigate by row.",
	),
	controlTypes.Role.DOCUMENT: _(
		# Translators: Help message for reading documents (mostly encountered in Internet Explorer windows).
		"Use the arrow keys or object navigation commands to move through the document.",
	),
	controlTypes.Role.TERMINAL: _(
		# Translators: Help message for terminal windows such as command prompt.
		"Type commands in the terminal window and use review cursor commands to read the output.",
	),
}

# Virtual Buffer.
browseModeHelpMessages = {
	controlTypes.Role.RADIOBUTTON: _(
		# Translators: Help message for radio buttons while in browse mode.
		"To select a radio button, switch to focus mode by pressing NVDA+SPACE or ENTER key.",
	),
	controlTypes.Role.EDITABLETEXT: _(
		# Translators: Help message for edit fields while in browse mode.
		"To type text into this edit field, switch to focus mode by pressing NVDA+SPACE or ENTER key.",
	),
	controlTypes.Role.COMBOBOX: _(
		# Translators: Help message for combo boxes in browse mode.
		"To select an item in the combo box, switch to focus mode by pressing NVDA+SPACE or ENTER key.",
	),
	controlTypes.Role.DOCUMENT: _(
		# Translators: Help message for reading webpages.
		"Use the browse mode and quick navigation commands to read through the webpage.",
	),
}
