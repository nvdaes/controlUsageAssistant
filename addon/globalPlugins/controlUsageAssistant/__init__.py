# Control Usage Assistant
# A global plugin for NVDA
# Author: Joseph Lee <joseph.lee22590@gmail.com>
# Copyright 2013, released under GPL.

# Press NVDA+H to hear a sentence or two on interacting with a particular control.
# Extension plan: ability to get context-sensitive help on NvDA options.

# Import please:
import globalPluginHandler # Basics of Global Plugin.
import tones # For debugging and testing, to be removed in the release.
import ui # For speaking and brailling help messages.
import api # To fetch obj properties.
import controlTypes # The heart of this module.
import ctrltypelist # The control types dictionary.
import addonHandler # Addon basics.
addonHandler.initTranslation() # Internationalization.

# Init:
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	
# 		 NVDA+H: Obtain usage help on a particular control.
	# Depending on the type of control, lookup a dictionary of control types and help messages.
	# Partially implemented.
	def script_obtainControlHelp(self, gesture):
		tones.beep(500, 100) # For testing purposes, to be removed in official release.
		myObj = api.getFocusObject()
		curControl = myObj.role
		ui.message(self.getHelpMessage(curControl)) # The actual function is below.
	
		
	def getHelpMessage(self, rolenumber): # Here, rolenumber is the role's unique ID number. See the dictionary imported above.
		if rolenumber not in ctrltypelist.helpMessages:
			# Translators: Message presented when there is no help message for the focused control.
			ui.message(_("No help for this control"))
		else:
			return ctrltypelist.helpMessages[rolenumber]
	
	
	__gestures={
		"KB:NVDA+H":"obtainControlHelp",
			}
# End.