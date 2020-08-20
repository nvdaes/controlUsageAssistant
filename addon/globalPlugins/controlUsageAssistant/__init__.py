# Control Usage Assistant
# A global plugin for NVDA
# Author: Joseph Lee <joseph.lee22590@gmail.com>
# Copyright 2013-2020, released under GPL.

# Press NVDA+H to hear (or read in braille) a sentence or two on interacting with a particular control.
# Extension plan: ability to get context-sensitive help on NvDA options.

import globalPluginHandler
import ui
import api
from virtualBuffers import VirtualBuffer
import scriptHandler
import addonHandler
addonHandler.initTranslation()
from . import helpmessages

# How many method resolution order (MRO) level help messages to consider before resorting to role-based messages.
CUAMROLevel = 0


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# NVDA+H: Obtain usage help on a particular control.
	# Start by looking at method resolution order (MRO) for object class hierarchy.
	# Then depending on the type of control and its state(s), lookup a dictionary of control types and help messages.
	# If the control is used differently in apps, then lookup the app entry and give the customized message.
	
	@scriptHandler.script(
		# Translators: Input help message for control help command.
		description=_("Presents a message on how to interact with the focused control."),
		# Translators: Input gesture category for Control Usage Assistant add-on.
		category=_("Control Usage Assistant"),
		gesture="KB:NVDA+H"
	)
	def script_controlHelp(self, gesture):
		obj = api.getFocusObject()
		# The prototype UI message, the actual processing is done below.
		ui.browseableMessage(self.getHelpMessage(obj), title=_("Control Usage Assistant"))

	# GetHelpMessage: The actual function behind the script above.
	def getHelpMessage(self, curObj):
		# Present help messages based on object class MRO, role constant, state(s) and focused app.
		# If the focused object defines "helpText" method, any message from there will become its help message, skipping MRO and other lookup methods.
		# These messages (if any) will be appended to a list of help messages.
		helpMessages = []
		# Check if the focused object does come with a help text method.
		if hasattr(curObj, "helpText"):
			helpMessages.append(curObj.helpText)
		else:
			for entry in curObj.__class__.__mro__:
				clsName = str(entry).split("'")[1]
				if clsName in helpmessages.objectsHelpMessages:
					helpMessages.append(helpmessages.objectsHelpMessages[clsName])
		# Except for virtual buffers, do not proceed if we do have help messages from MRO lookup.
		# Additional constraints.
		# Just in case browse mode is active.
		if isinstance(curObj.treeInterceptor, VirtualBuffer):
			# In case we're dealing with virtual buffer, call the below method.
			helpMessages.append(self.VBufHelp(curObj))
		if len(helpMessages) == CUAMROLevel:
			if curObj.role in helpmessages.controlTypeHelpMessages:
				helpMessages.append(helpmessages.controlTypeHelpMessages[curObj.role])
			# Last resort: If we fail to obtain any default or app-specific message (because there is no entry for the role in the help messages), give the below message.
			else:
				# Translators: Message presented when there is no help message for the focused control.
				helpMessages.append(_("No help for this control"))
		helpMessages.append("Press escape to close this help screen.")
		return "\n".join(helpMessages)

	# Any exceptions to lookup keys goes here.
	# First case: virtual buffer control exceptions.
	VBufForms = {6, 8, 13}  # Forms encountered on webpages; add custom message form them in browse mode.
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
			try:
				VBufmsg = helpmessages.controlTypeHelpMessages[obj.role]
			except KeyError:
				VBufmsg = _("No help for this control")
		return VBufmsg
