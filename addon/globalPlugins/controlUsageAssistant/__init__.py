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
import addonHandler
addonHandler.initTranslation()
from . import helpmessages

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

	# GetHelpMessage: The actual function behind the script above.
	def getHelpMessage(self, curObj):
		# Present help messages based on object class MRO, role constant, state(s) and focused app.
		# These messages (if any) will be appended to a list of help messages.
		helpMessages = []
		for entry in curObj.__class__.__mro__:
			clsName = str(entry).split("'")[1]
			if clsName in helpmessages.objectsHelpMessages:
				helpMessages.append(helpmessages.objectsHelpMessages[clsName])
		# Additional constraints.
		offset = 0
		# Just in case browse mode is active.
		if isinstance(curObj.treeInterceptor, VirtualBuffer):
			# We're dealing with virtual buffer (virtual buffer is a tree interceptor).
			offset = 200
		if offset >= 0:
			index = offset + curObj.role
		else:
			index = offset - curObj.role
		# In case offset is zero, then test for state(s).
		curState = curObj._get_states()
		if (offset == 200 or offset == -200):
			# In case we're dealing with virtual buffer, call the below method.
			helpMessages.append(self.VBufHelp(curObj, index))
		elif curObj.role == 8 and controlTypes.STATE_READONLY in curState:
			# Special case 1: WE have encountered a read-only edit field.
			helpMessages.append(_(helpmessages.helpMessages[-8]))
		else:
			# Penultimate: if we're strictly dealing with default messages either because offset is 0 or there is no offset+/-role index in the helpMessages.
			if curObj.role in helpmessages.controlTypeHelpMessages:
				helpMessages.append(helpmessages.controlTypeHelpMessages[curObj.role])
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
	VBufForms={6, 8, 13} # Forms encountered on webpages; add custom message form them in browse mode.
	# And the function for handling these:
	def VBufHelp(self, obj):
		if obj.role in self.VBufForms:
			if not obj.treeInterceptor.passThrough:
				VBufmsg = helpmessages.browseModeHelpMessages[obj.role]
			else:
				VBufmsg = helpmessages.controlTypeHelpMessages[obj.role]
				# Translators: Additional message when working with forms in focus mode.
				VBufmsg += _(" To switch to browse mode, press NVDA+SPACE or escape key")
		elif obj.role == 52:
			if not obj.treeInterceptor.passThrough:
				VBufmsg = helpmessages.browseModeHelpMessages[obj.role]
			else:
				# Translators: Help message for reading a webpage while in focus mode.
				VBufmsg = _("To use browse mode and quick navigation keys to read the webpage, switch to browse mode by pressing NVDA+SPACE")
		else:
			VBufmsg = helpmessages.controlTypeHelpMessages[obj.role]
		return VBufmsg
