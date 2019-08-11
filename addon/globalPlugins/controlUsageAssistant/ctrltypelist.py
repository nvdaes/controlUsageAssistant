# Control Usage Assistant
# An add-on for NVDA
# Copyright 2013-2019 Joseph Lee, released under GPL.

# The list of control types and their help messages.

# Help Messages Dictionary: key = obj role number, with offsets added based on apps and/or states.
#a negative role number between -1 and -199 indicates restricted control, such as read-only edit field.
# A role number greater than 200 indicates additional features, such as multiline and virtual buffer instance.
# Anything beyond +/-400 means appModule or process-specific (positive = appModule, negative = process).
helpMessages = {
	# Default: universal across apps and states.
	
	# Translators: Help message for a checkbox.
	5:_("Press space to check or uncheck the checkbox"),
	# Translators: Help message for working with radio buttons.
	6:_("Use the arrow keys to choose a radio button"),
	# Translators: Help message for a list box.
	7:_("Use the arrow keys to read this box"),
	# Translators: Help message for an edit field.
	8:_("Type text here"),
	# Translators: Help message for a read-only control.
	-8:_("Use the text navigation commands to read text"),
	# Translators: Help message for a button.
	9:_("Press SPACE or ENTER to activate this button"),
	# Translators: Help message for menu items.
	11:_("Use the arrow keys to move between the menu items"),
	# Translators: Help message for pop-up menu (so-called context menu, activated by presing Applications key).
	12:_("Use up and down arrow keys to move through options in the pop-up menu"),
	# Translators: Help message for a combo box.
	13:_("Use the arrow keys to move among choices in the combo box until the desired option is found"),
	# Translators: Help message for a list view.
	15:_("Use the arrow keys to move to the next or previous item in this list"),
	# Translators: Help message for activating links.
	19:_("Press SPACE or ENTER to activate this link"),
	# Translators: Help message for working with tree view items.
	21:_("Use the up and down arrow keys to select the items. Use left arrow to collapse and right arrow to expand"),
	# Translators: Help message for navigating tabs, such as various property tabs for drive properties in My Computer.
	22:_("Use the left and right arrow keys to move between tabs, or press control+tab for next tab and control+shift+tab for previous tab"),
	# Translators: Help message for working with slider controls such as volume mixer in Windows 7.
	24:_("Use the left and down arrow keys to decrease and up and right arrow keys to increase the value in this slider. Use page up and page down to increase or decrease in larger values, and press home and end keys to select maximum and minimum value"),
	# Translators: Help message for navigating tables.
	28:_("Press control, alt and arrow keys together to move between rows and columns"),
	# Translators: Help message for navigating table cells.
	29:_("Press control, alt and arrow keys together to move between table cells"),
	# Translators: Help message for reading documents (mostly encountered in Internet Explorer windows).
	52:_("Use the arrow keys or object navigation commands to move through the document"),
	# Translators: Help message for terminal windows such as command prompt.
	82:_("Type commands in the terminal window and use review cursor commands to read the output"),
	
	# 200: Virtual Buffer.
	# Translators: Help message for radio buttons while in browse mode.
	206:_("To select a radio button, switch to focus mode by pressing NVDA+SPACE or ENTER key"),
	# Translators: Help message for edit fields while in browse mode.
	208:_("To type text into this edit field, switch to focus mode by pressing NVDA+SPACE or ENTER key"),
	# Translators: Help message for combo boxes in browse mode.
	213:_("To select an item in the combo box, switch to focus mode by pressing NVDA+SPACE or ENTER key"),
	# Translators: Help message for reading webpages.
	252:_("Use the browse mode and quick navigation commands to read through the webpage"),
	
	# App-specific case 1: AppeModule for app is present.
	
	# 300: Explorer (to deal with specific cases.
	# Translators: Message for moving between Windows 8 start screen tiles (Windows 8 only).
	329:_("Use the arrow keys to move between start screen tiles"),
	
	# 400: Microsoft powerpoint (powerpnt):
	# Translators: Message for moving between slides in slide view (a list of slides for a Powerpoint presentation).
	403:_("Use up and down arrow keys to move between slides"),
	# Translators: Help message for working with slide shows.
	403.1:_("Press SPACE or BACKSPACE to move between slides in the slide show. To end the slide show, press escape"),
	
	
	# App-specific case 2: AppeModule for app is not present (use processes).
	# -300: Excel.
	# Translators: Help message for moving between Excel spreadsheet cells.
	-329:_("Use the arrow keys to move between spreadsheet cells"),
	
	# -400: Adobe Reader (special case).
	# Translators: Help message for reading Adobe PDF documents.
	-452:"Use the browse mode and quick navigation commands to read through the PDF document"
	}
