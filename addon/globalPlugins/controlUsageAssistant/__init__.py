# Control Usage Assistant
# A global plugin for NVDA
# Author: Joseph Lee <joseph.lee22590@gmail.com>
# Copyright 2013, released under GPL.

# Press NVDA+H to hear (or read in braille) a sentence or two on interacting with a particular control.
# Extension plan: ability to get context-sensitive help on NvDA options.

# Import please:
import globalPluginHandler # Basics of Global Plugin.
import ui # For speaking and brailling help messages.
import api # To fetch object properties.
import controlTypes # The heart of this module.
import ctrltypelist # The control types and help messages dictionary.
from apphelplist import appOffsets, procOffsets # A dictionary of appModule and process offset (see below for explanation).
import appModuleHandler # Apps.
import addonHandler # Addon basics.
addonHandler.initTranslation() # Internationalization.

# Init:
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	
		# NVDA+H: Obtain usage help on a particular control.
	# Depending on the type of control and its state(s), lookup a dictionary of control types and help messages.
	# If the control is used differently in apps, then lookup the app entry and give the customized message.
	def script_obtainControlHelp(self, gesture):
		obj = api.getCaretObject()
		# The prototype UI message, the actual processing is done below.
		ui.message(self.getHelpMessage(obj))
	# Translators: Input help message for obtain control help command.
	script_obtainControlHelp.__doc__=_("Presents a short message on how to interact with the focused control.")
		
	
	# GetHelpMessage: The actual function behind the script above.
	def getHelpMessage(self, curObj):
		# The actual process of presenting the help message based on object's role, state(s) and focused app.
		# For apps, the lookup chain is: appModule first, then executable image name then finally to default entries.
		msg = "" # A string (initially empty) to hold the message; needed to work better with braille.
		curRole = curObj.role # Just an int (role constant from control types), the key to the help messages dictionary.
		curState = curObj._get_states() # To work with states to present appropriate help message.
		curApp = curObj.appModule # Detect which app we're running so to give custom help messages for controls.
		curProc = appModuleHandler.getAppNameFromProcessID(curObj.processID,True) # Borrowed from NVDA core code, used when appModule return fails.
		# Absolute last resort: If we fail to obtain any default or app-specific message (because there is no entry for the role in the help messages), give the below message.
		if curRole not in ctrltypelist.helpMessages:
			# Translators: Message presented when there is no help message for the focused control.
			msg = _("No help for this control")
		# Special case 1: WE have encountered a read-only edit field.
		elif curRole == 8 and controlTypes.STATE_READONLY in curState:
			msg = _(ctrltypelist.helpMessages[-8])
		# App-specific messages (Todo): Find appModules, then come here to deal with proc images if there is no appModule for the current process.
		# Testing with Excel, since user can use just arrow keys for tablecell.
		elif curRole == 29 and curProc == "EXCEL.EXE":
			msg = _(ctrltypelist.helpMessages[procOffsets[curProc]+curRole]) # Turns out it works, so start applying to others.
		# Finally, deal with default messages.
		else:
			msg = _(ctrltypelist.helpMessages[curRole])
		return msg
	
		
	# For development testing:
	# GetAppName: To see if one can even print the name of the appModule.
	def script_getAppName(self, gesture):
		appObj = api.getFocusObject()
		app = appObj.appModule
		ui.message(app.appModuleName.split(".")[0])
	
	__gestures={
		"KB:NVDA+H":"obtainControlHelp",
		"KB:NVDA+G":"getAppName",
			}
# End.