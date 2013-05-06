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
import api # To fetch object properties.
import controlTypes # The heart of this module.
import ctrltypelist # The control types and help messages dictionary.
import addonHandler # Addon basics.
addonHandler.initTranslation() # Internationalization.

# Init:
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	
# 		 NVDA+H: Obtain usage help on a particular control.
	# Depending on the type of control and its state(s), lookup a dictionary of control types and help messages.
	# Partially implemented.
	def script_obtainControlHelp(self, gesture):
		tones.beep(500, 100) # For testing purposes, to be removed in official release.
		ui.message(self.getHelpMessage(api.getFocusObject())) # The actual function is below.
	# Translators: Input help message for obtain control help command.
	script_obtainControlHelp.__doc__=_("Presents a short message on how to interact with the focused control.")
		
	def getHelpMessage(self, curObj): # Here, we want to present the appropriate help message based on role and state.
		curRole = curObj.role # Just an int, the key to the help messages dictionary.
		curState = curObj._get_states() # To work with states to present appropriate help message.
		if curRole not in ctrltypelist.helpMessages:
			# Translators: Message presented when there is no help message for the focused control.
			ui.message(_("No help for this control"))
		elif curRole == 8 and controlTypes.STATE_READONLY in curState:
			ui.message(_(ctrltypelist.helpMessages[-8]))
		else:
			ui.message(_(ctrltypelist.helpMessages[curRole]))
		
	
	
	__gestures={
		"KB:NVDA+H":"obtainControlHelp",
			}
# End.