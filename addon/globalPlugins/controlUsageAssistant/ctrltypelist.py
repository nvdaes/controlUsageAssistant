# Control Usage Assistant
# An add-on for NVDA
# Copyright 2013 Joseph Lee, released under GPL.

# The list of control types and their help messages.
			
	# Help Messages Dictionary: key = obj role number.
	#a negative role number indicates restricted control, such as read-only edit field.
	# A role number greater than 200 indicates additional features, such as multiline and virtual buffer instance.
helpMessages = {
	# Translators: Help message for a checkbox.
	5:_("Press space to check or uncheck the checkbox"),
	# Translators: Help message for a combo box.
	6:"Use the arrow keys to choose an option",
	# Translators: Help message for a list box.
	7:"Use the arrow keys to read this box",
	# Translators: Help message for an edit field.
	8:"Type text here",
	# Translators: Help message for a read-only control.
	-8:_("Use the text navigation commands to read text"),
	# Translators: Help message for a button.
	9:"Press SPACE or ENTER to activate this button",
	# Translators: Help message for menu items.
	11:"Use the arrow keys to move between the menu items",
	# Translators: Help message for a combo box.
	13:"Use the arrow keys to move among choices in the combo box until the desired option is found",
	# Translators: Help message for a list view.
	15:"Use the arrow keys to move to the next or previous item in this list",
	# Translators: Help message for navigating tables.
	28:"Press control, alt and arrow keys together to move between rows and columns",
	# Translators: Help message for reading documents (mostly encountered in Internet Explorer windows).
	52:"Use the arrow keys or object navigation commands to move through the document"
	}
