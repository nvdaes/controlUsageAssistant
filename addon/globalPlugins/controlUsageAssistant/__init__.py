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
from virtualBuffers import VirtualBuffer # Virtual buffer handling.
import appModuleHandler # Apps.
from appModules import powerpnt # App modules with special personalities such as Powerpoint where one needs to differentiate between slides and slide shows.
import addonHandler # Addon basics.
addonHandler.initTranslation() # Internationalization.
#import tones # For debugging.
from baseObject import ScriptableObject # Input Gestures categories.

# Init:
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	
	# Script category.
	# Translators: Input gesture category for Control Usage Assistant add-on.
	scrcat_CUA = _("Control Usage Assistant")
	
	# NVDA+H: Obtain usage help on a particular control.
	# Depending on the type of control and its state(s), lookup a dictionary of control types and help messages.
	# If the control is used differently in apps, then lookup the app entry and give the customized message.
	def script_obtainControlHelp(self, gesture):
		obj = api.getFocusObject()
		# The prototype UI message, the actual processing is done below.
		ui.message(_(self.getHelpMessage(obj)))
	# Translators: Input help message for obtain control help command.
	script_obtainControlHelp.__doc__=_("Presents a short message on how to interact with the focused control.")
	script_obtainControlHelp.category = scrcat_CUA
		
	# GetMessageOffset: Obtain message offset based on appModule and/or processes list.
	# Return value: positive = appModule, negative = processes, 0 = default.
	def getMessageOffset(self, curObj):
		from apphelplist import appOffsets, procOffsets # To be used in the lookup only.
		curApp = curObj.appModule.appName # Detect which app we're running so to give custom help messages for controls.
		curProc = appModuleHandler.getAppNameFromProcessID(curObj.processID,True) # Borrowed from NVDA core code, used when appModule return fails.
		# Lookup setup:
		if curApp in appOffsets:
			# If appModule is found:
			return appOffsets[curApp]
		elif curProc in procOffsets:
			# In case appModule is not found but we do have the current process name registered.
			return procOffsets[curProc]
		elif isinstance(curObj.treeInterceptor, VirtualBuffer):
			# We're dealing with virtual buffer (virtual buffer is a tree interceptor). However, watch out for Adobe Reader (check using ternary operation).
			return -400 if (curProc == "AcroRd32.exe") else 200
		else:
			# Found nothing, so return zero to fall back to default entries.
			return 0
					
	# GetHelpMessage: The actual function behind the script above.
	def getHelpMessage(self, curObj):
		# Present help messages based on role constant, state(s) and focused app.
		msg = "" # A string (initially empty) to hold the message; needed to work better with braille.
		offset = self.getMessageOffset(curObj) # offset = lookup offset, the base for our lookup index.
		if offset >= 0: # We found an appModule. In case of 0, check object state(s).
			index = offset + curObj.role
		else: # No appModule, so work with processes.
			index = offset - curObj.role
		# In case offset is zero, then test for state(s).
		curState = curObj._get_states()
		# Let the index lookup begin.
		# A number of specific cases follows:
		# PowerPoint: differentiate between slide list and slide show.
		if isinstance(curObj, powerpnt.SlideShowWindow):
			msg = ctrltypelist.helpMessages[403.1]	
		# General case: if we do have an entry for the appModule/process.
		elif (offset >= 300 or offset <= -300) and index in ctrltypelist.helpMessages:
			msg= ctrltypelist.helpMessages[index]
			# Clean the above code later.
		elif (offset == 200 or offset == -200):
			# In case we're dealing with virtual buffer, call the below method.
			msg = self.VBufHelp(curObj, index)
		elif curObj.role == 8 and controlTypes.STATE_READONLY in curState:
			# Special case 1: WE have encountered a read-only edit field.
			msg = _(ctrltypelist.helpMessages[-8])
		else:
			# Penultimate: if we're strictly dealing with default messages either because offset is 0 or there is no offset+/-role index in the helpMessages.
			if curObj.role in ctrltypelist.helpMessages:
				msg = ctrltypelist.helpMessages[curObj.role]
			# Last resort: If we fail to obtain any default or app-specific message (because there is no entry for the role in the help messages), give the below message.
			else:
				# Translators: Message presented when there is no help message for the focused control.
				msg = _("No help for this control")
		return msg
	
	__gestures={
		"KB:NVDA+H":"obtainControlHelp",
	}
	# Any exceptions to lookup keys goes here.
	# First case: virtual buffer control exceptions.
	VBufForms={206, 208, 213} # Forms encountered on webpages; add custom message form them in browse mode.
	# And the function for handling these:
	def VBufHelp(self, obj, i): # i = index.
		if i in self.VBufForms:
			if not obj.treeInterceptor.passThrough:
				VBufmsg = ctrltypelist.helpMessages[i]
			else:
				VBufmsg = ctrltypelist.helpMessages[obj.role]
				# Translators: Additional message when working with forms in focus mode.
				VBufmsg += _(". To switch to browse mode, press NVDA+SPACE or escape key")
		elif i == 252:
			if not obj.treeInterceptor.passThrough:
				VBufmsg = ctrltypelist.helpMessages[252]
			else:
				# Translators: Help message for reading a webpage while in focus mode.
				VBufmsg = _("To use browse mode and quick navigation keys to read the webpage, switch to browse mode by pressing NVDA+SPACE")
		else:
			VBufmsg = ctrltypelist.helpMessages[obj.role]
		return VBufmsg
	
	
	# End.