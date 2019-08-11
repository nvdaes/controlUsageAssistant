# Control Usage Assistant/control types help messages
# An add-on for NVDA
# Copyright 2019 Joseph Lee, released under GPL.

# Provides help messages for control roles and states, mirroring control types module in NVDA Core.
# Each help messages dictionary records control roles and help messages.
# If specific states are found, help messages will come from state-specific subsets.

import controlTypes

# Default help messages for controls: key = role, value = messages.
# Source: NVDA pull request for issue 2699 (context-sensitive help)

controlTypeHelpMessages = {
	# Translators: Help message for a checkbox.
	controlTypes.ROLE_CHECKBOX:_("Press space bar to check or uncheck this check box."),
	# Translators: Help message for working with radio buttons.
	controlTypes.ROLE_RADIOBUTTON:_("Use the arrow keys to choose a radio button."),
	# Translators: Help message for a list box.
	controlTypes.ROLE_STATICTEXT:_("Use the arrow keys to read this box."),
	# Translators: Help message for an edit field.
	controlTypes.ROLE_EDITABLETEXT:_("Type text here."),
	# Translators: Help message for a button.
	controlTypes.ROLE_BUTTON:_("Press SPACE or ENTER to activate this button."),
	# Translators: Help message for menu items.
	controlTypes.ROLE_MENUITEM:_("Use the arrow keys to move between the menu items."),
	# Translators: Help message for pop-up menu (so-called context menu, activated by presing Applications key).
	controlTypes.ROLE_POPUPMENU:_("Use up and down arrow keys to move through options in the pop-up menu."),
	# Translators: Help message for a combo box.
	controlTypes.ROLE_COMBOBOX:_("Use the arrow keys to move among choices in the combo box until the desired option is found."),
	# Translators: Help message for a list view.
	controlTypes.ROLE_LISTITEM:_("Use the arrow keys to move to the next or previous item in this list."),
	# Translators: Help message for activating links.
	controlTypes.ROLE_LINK:_("Press SPACE or ENTER to activate this link."),
	# Translators: Help message for working with tree view items.
	controlTypes.ROLE_TREEVIEWITEM:_("Use the up and down arrow keys to select the items. Use left arrow to collapse and right arrow to expand."),
	# Translators: Help message for navigating tabs, such as various property tabs for drive properties in My Computer.
	controlTypes.ROLE_TAB:_("Use the left and right arrow keys to move between tabs, or press control+tab for next tab and control+shift+tab for previous tab."),
	# Translators: Help message for working with slider controls such as volume mixer in Windows 7.
	controlTypes.ROLE_SLIDER:_("Use the left and down arrow keys to decrease and up and right arrow keys to increase the value in this slider. Use page up and page down to increase or decrease in larger values, and press home and end keys to select maximum and minimum value."),
	# Translators: Help message for navigating tables.
	controlTypes.ROLE_TABLE:_("Press control, alt and arrow keys together to move between rows and columns."),
	# Translators: Help message for navigating table cells.
	controlTypes.ROLE_TABLECELL:_("Press Control+Alt+arrow keys to other table cells. Pressing left or right arrow keys will navigate between columns, and up and down arrow keys will navigate by row."),
	# Translators: Help message for reading documents (mostly encountered in Internet Explorer windows).
	controlTypes.ROLE_DOCUMENT:_("Use the arrow keys or object navigation commands to move through the document."),
	# Translators: Help message for terminal windows such as command prompt.
	controlTypes.ROLE_TERMINAL:_("Type commands in the terminal window and use review cursor commands to read the output."),

	# 200: Virtual Buffer.
	# Translators: Help message for radio buttons while in browse mode.
	206:_("To select a radio button, switch to focus mode by pressing NVDA+SPACE or ENTER key."),
	# Translators: Help message for edit fields while in browse mode.
	208:_("To type text into this edit field, switch to focus mode by pressing NVDA+SPACE or ENTER key."),
	# Translators: Help message for combo boxes in browse mode.
	213:_("To select an item in the combo box, switch to focus mode by pressing NVDA+SPACE or ENTER key."),
	# Translators: Help message for reading webpages.
	252:_("Use the browse mode and quick navigation commands to read through the webpage."),
}

# Translators: Help message for a read-only control.
#-8:_("Use the text navigation commands to read text."),
