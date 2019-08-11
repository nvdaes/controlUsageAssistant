# Control Usage Assistant
# A global plugin for NVDA
# Author: Joseph Lee <joseph.lee22590@gmail.com>
# Copyright 2013-2019, released under GPL.

# Press NVDA+H to hear (or read in braille) a sentence or two on interacting with a particular control.
# Extension plan: ability to get context-sensitive help on NvDA options.

import globalPluginHandler
import ui
import api
import controlTypes
from virtualBuffers import VirtualBuffer
import appModuleHandler
from appModules import powerpnt
import addonHandler
addonHandler.initTranslation()
from . import helpmessages

# AppModule and process offsets: positive = appModule, negative = process.

# App offsets: lookup the appModule.
appOffsets={
	"explorer":300,
	"powerpnt":400
	}

# Process offsets: come here when we fail to obtain appModules.
procOffsets={
	"EXCEL.EXE":-300,
	"AcroRd32.exe":-400 #This is a special case - although Adobe reader uses virtual buffer, it is not a webpage, hence different message should be given for PDF's.
	}


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# Translators: Input gesture category for Control Usage Assistant add-on.
	scriptCategory = _("Control Usage Assistant")

	# NVDA+H: Obtain usage help on a particular control.
	# Start by looking at method resolution order (MRO) for object class hierarchy.
	# Then depending on the type of control and its state(s), lookup a dictionary of control types and help messages.
	# If the control is used differently in apps, then lookup the app entry and give the customized message.
	def script_controlHelp(self, gesture):
		obj = api.getFocusObject()
		# The prototype UI message, the actual processing is done below.
		ui.browseableMessage(self.getHelpMessage(obj), title=_("Control Usage Assistant"))
	# Translators: Input help message for obtain control help command.
	script_controlHelp.__doc__=_("Presents a message on how to interact with the focused control.")

	# GetMessageOffset: Obtain message offset based on appModule and/or processes list.
	# Return value: positive = appModule, negative = processes, 0 = default.
	def getMessageOffset(self, curObj):
		curApp = curObj.appModule.appName
		curProc = appModuleHandler.getAppNameFromProcessID(curObj.processID,True)
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
		# Present help messages based on object class MRO, role constant, state(s) and focused app.
		# These messages (if any) will be appended to a list of help messages.
		helpMessages = []
		for entry in curObj.__class__.__mro__:
			clsName = str(entry).split("'")[1]
			if clsName in objMROHelpMessages:
				helpMessages.append(objMROHelpMessages[clsName])
		offset = self.getMessageOffset(curObj)
		if offset >= 0:
			index = offset + curObj.role
		else:
			index = offset - curObj.role
		# In case offset is zero, then test for state(s).
		curState = curObj._get_states()
		# A number of specific cases follows:
		# PowerPoint: differentiate between slide list and slide show.
		if isinstance(curObj, powerpnt.SlideShowWindow):
			helpMessages.append(helpmessages.helpMessages[403.1])
		# General case: if we do have an entry for the appModule/process.
		elif (offset >= 300 or offset <= -300) and index in helpmessages.helpMessages:
			helpMessages.append(helpmessages.helpMessages[index])
			# Clean the above code later.
		elif (offset == 200 or offset == -200):
			# In case we're dealing with virtual buffer, call the below method.
			helpMessages.append(self.VBufHelp(curObj, index))
		elif curObj.role == 8 and controlTypes.STATE_READONLY in curState:
			# Special case 1: WE have encountered a read-only edit field.
			helpMessages.append(_(helpmessages.helpMessages[-8]))
		else:
			# Penultimate: if we're strictly dealing with default messages either because offset is 0 or there is no offset+/-role index in the helpMessages.
			if curObj.role in helpmessages.helpMessages:
				helpMessages.append(helpmessages.helpMessages[curObj.role])
			# Last resort: If we fail to obtain any default or app-specific message (because there is no entry for the role in the help messages), give the below message.
			else:
				# Translators: Message presented when there is no help message for the focused control.
				helpMessages.append(_("No help for this control"))
		helpMessages.append("Press escape to close this help screen.")
		return "\n".join(helpMessages)

	__gestures={
		"KB:NVDA+H":"controlHelp",
	}

	# Any exceptions to lookup keys goes here.
	# First case: virtual buffer control exceptions.
	VBufForms={206, 208, 213} # Forms encountered on webpages; add custom message form them in browse mode.
	# And the function for handling these:
	def VBufHelp(self, obj, i): # i = index.
		if i in self.VBufForms:
			if not obj.treeInterceptor.passThrough:
				VBufmsg = helpmessages.helpMessages[i]
			else:
				VBufmsg = helpmessages.helpMessages[obj.role]
				# Translators: Additional message when working with forms in focus mode.
				VBufmsg += _(". To switch to browse mode, press NVDA+SPACE or escape key")
		elif i == 252:
			if not obj.treeInterceptor.passThrough:
				VBufmsg = helpmessages.helpMessages[252]
			else:
				# Translators: Help message for reading a webpage while in focus mode.
				VBufmsg = _("To use browse mode and quick navigation keys to read the webpage, switch to browse mode by pressing NVDA+SPACE")
		else:
			VBufmsg = helpmessages.helpMessages[obj.role]
		return VBufmsg
