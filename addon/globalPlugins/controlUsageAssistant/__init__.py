# -*- coding: UTF-8 -*-

# Control Usage Assistant
# A global plugin for NVDA
# Copyright 2013-2025 Joseph Lee, Noelia Ruiz Martínez
# Released under GPL.

import wx

import speech
from ui import browseableMessage

import NVDAObjects

# NVDA+H: Obtain usage help on a particular control.
# Start by looking at method resolution order (MRO) for object class hierarchy.
# Then depending on the type of control and its state(s), lookup a map of control types and help messages.
# If the control is used differently in apps, then lookup the app entry and give the customized message.
# Extension plan: ability to get context-sensitive help on NVDA options.

from collections.abc import Callable

import globalPluginHandler
import controlTypes
import api
from browseMode import BrowseModeDocumentTreeInterceptor
import scriptHandler
import config
from speech.commands import PitchCommand
import braille
import gui
from gui.settingsDialogs import NVDASettingsDialog
import addonHandler

from .controltypeshelp import controlTypeHelpMessages, browseModeHelpMessages
from .nvdaobjectshelp import objectsHelpMessages
from .utils import confspec, getAutomaticSpeechSequence, AddonSettingsPanel

addonHandler.initTranslation()

_: Callable[[str], str]

# How many method resolution order (MRO) level help messages to consider
# before resorting to role-based messages.
CUAMROLevel = 0


class EnhancedSuggestion(NVDAObjects.behaviors.InputFieldWithSuggestions):
	def event_suggestionsOpened(self):
		super().event_suggestionsOpened()
		self.helpText = (
			# Translators: help text for search field in Windows 10 and other places.
			_("After typing search text, press up or down arrow keys to review list of suggestions.")
		)

	def event_suggestionsClosed(self):
		self.helpText = None


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# Translators: Input gesture category for Control Usage Assistant add-on.
	scriptCategory = _("Control Usage Assistant")

	def __init__(self):
		super().__init__()
		config.conf.spec["controlUsageAssistant"] = confspec
		self.automaticHelpMessage = None
		NVDASettingsDialog.categoryClasses.append(AddonSettingsPanel)

	def terminate(self):
		NVDASettingsDialog.categoryClasses.remove(AddonSettingsPanel)

	def onSettings(self, evt):
		gui.mainFrame.popupSettingsDialog(NVDASettingsDialog, AddonSettingsPanel)

	@scriptHandler.script(
		# Translators: Input help message for command to show settings.
		description=_("Shows the Control Usage Assistant settings."),
	)
	def script_settings(self, gesture):
		wx.CallAfter(self.onSettings, None)

	@scriptHandler.script(
		# Translators: Input help message for control help command.
		description=_("Presents a message on how to interact with the focused control."),
		gesture="KB:NVDA+H",
	)
	def script_controlHelp(self, gesture):
		obj = api.getFocusObject()
		# The prototype UI message, the actual processing is done below.
		browseableMessage(
			self.getHelpMessage(obj),
			title=_("Control Usage Assistant"),
			copyButton=True,
			closeButton=True,
		)

	# GetHelpMessage: The actual function behind the script above.
	def getHelpMessage(self, curObj):
		# Present help messages based on object class MRO, role constant, state(s) and focused app.
		# If the focused object defines "helpText" method,
		# any message from there will become its help message,
		# skipping MRO and other lookup methods.
		# These messages (if any) will be appended to a list of help messages.
		helpMessages = []
		# Check if the focused object does come with a help text method.
		if hasattr(curObj, "helpText"):
			helpMessages.append(curObj.helpText)
		else:
			for entry in curObj.__class__.__mro__:
				clsName = str(entry).split("'")[1]
				if clsName in objectsHelpMessages:
					helpMessages.append(objectsHelpMessages[clsName])
		# Except for virtual buffers, do not proceed if we do have help messages from MRO lookup.
		# Additional constraints.
		# Just in case browse mode is active.
		if isinstance(curObj.treeInterceptor, BrowseModeDocumentTreeInterceptor):
			# In case we're dealing with virtual buffer, call the below method.
			helpMessages.append(self.VBufHelp(curObj.treeInterceptor.currentNVDAObject))
		if len(helpMessages) == CUAMROLevel:
			if curObj.role in controlTypeHelpMessages:
				helpMessages.append(controlTypeHelpMessages[curObj.role])
			# Last resort: If we fail to obtain any default or app-specific message
			# (because there is no entry for the role in the help messages), give the below message.
			else:
				# Translators: Message presented when there is no help message for the focused control.
				helpMessages.append(_("No help for this control"))
		# Translators: message presented at the end of help messages.
		helpMessages.append(_("Press escape to close this help screen."))
		return "\n".join(helpMessages)

	def getAutomaticHelpMessage(self, curObj):
		helpMessages = []
		if isinstance(curObj.treeInterceptor, BrowseModeDocumentTreeInterceptor):
			return None
		if hasattr(curObj, "helpText"):
			helpMessages.append(curObj.helpText)
		for entry in curObj.__class__.__mro__:
			clsName = str(entry).split("'")[1]
			if clsName in objectsHelpMessages:
				helpMessages.append(objectsHelpMessages[clsName])
		if len(helpMessages) == CUAMROLevel:
			if curObj.role in controlTypeHelpMessages:
				helpMessages.append(controlTypeHelpMessages[curObj.role])
			else:
				return None
		return "\n".join(helpMessages)

	# Any exceptions to lookup keys goes here.
	# First case: virtual buffer control exceptions.
	# Forms encountered on webpages; add custom message for them in browse mode.
	VBufForms = {
		controlTypes.Role.RADIOBUTTON,
		controlTypes.Role.EDITABLETEXT,
		controlTypes.Role.COMBOBOX,
	}

	# And the function for handling these:

	def VBufHelp(self, obj):
		if obj.role in self.VBufForms:
			if not obj.treeInterceptor.passThrough:
				VBufmsg = browseModeHelpMessages[obj.role]
			else:
				VBufmsg = controlTypeHelpMessages[obj.role]
				# Translators: Additional message when working with forms in focus mode.
				VBufmsg += _(" To switch to browse mode, press NVDA+SPACE or escape key")
		elif obj.role == controlTypes.Role.DOCUMENT:
			if not obj.treeInterceptor.passThrough:
				VBufmsg = browseModeHelpMessages[obj.role]
			else:
				VBufmsg = _(
					# Translators: Help message for reading a webpage while in focus mode.
					"To use browse mode and quick navigation keys to read the webpage, "
					"switch to browse mode by pressing NVDA+SPACE",
				)
		else:
			try:
				VBufmsg = controlTypeHelpMessages[obj.role]
			except KeyError:
				# Translators: Message presented when there's no help for this control.
				VBufmsg = _("No help for this control")
		return VBufmsg

	def shouldGetHelpAutomaticMessage(self) -> bool:
		settings = config.conf["controlUsageAssistant"]
		if settings["speech"] or settings["braille"]:
			return True
		return False

	def reportMessage(self, message):
		settings = config.conf["controlUsageAssistant"]
		if settings["speech"]:
			speechSequence = getAutomaticSpeechSequence(message, PitchCommand(settings["pitch"]))
			speech.speak(speechSequence)
		if settings["braille"]:
			braille.handler.message(message)

	def reportAutomaticHelpMessage(self, obj):
		if not self.shouldGetHelpAutomaticMessage():
			return
		try:
			message = self.getAutomaticHelpMessage(obj)
		except KeyError:
			return
		if message == self.automaticHelpMessage:
			return
		self.reportMessage(message)
		self.automaticHelpMessage = message

	def event_gainFocus(self, obj, nextHandler):
		nextHandler()
		if (
			not config.conf["controlUsageAssistant"]["focusMessages"]
			or not self.shouldGetHelpAutomaticMessage()
		):
			return
		self.reportAutomaticHelpMessage(obj)

	def getMessageForClickableObject(self):
		return config.conf["controlUsageAssistant"]["clickableObjectMessage"]

	def event_becomeNavigatorObject(self, obj, nextHandler, isFocus):
		nextHandler()
		if (
			isFocus
			or not self.shouldGetHelpAutomaticMessage()
			or obj.appModule.productName == "MicrosoftWindows.Client.CBS"
		):
			return
		message = None
		try:
			obj.getActionName()
			message = self.getMessageForClickableObject()
		except Exception:
			pass
		if message:
			wx.CallAfter(self.reportMessage, message)

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.role == controlTypes.Role.EDITABLETEXT:
			clsList.insert(0, EnhancedSuggestion)
