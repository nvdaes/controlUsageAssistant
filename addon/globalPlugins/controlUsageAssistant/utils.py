# -*- coding: UTF-8 -*-

# controlUsageAssistant/utils.py
# Copyright 2022 Noelia Ruiz Martínez
# Released under GPL

import wx
from typing import Dict, Optional
from typing import Callable

import gui
from gui import SettingsPanel, guiHelper
import config
from speech import types
import addonHandler

addonHandler.initTranslation()

_: Callable[[str], str]

ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]

confspec: Dict[str, str] = {
	"focusMessages": "boolean(default=True)",
	"clickableObjectMessage": "string(default="")",
	"speech": "boolean(default=False)",
	"braille": "boolean(default=False)",
	"pitch": "integer(default=0)",
}


def getAutomaticSpeechSequence(message: str, speechCommand=None) -> Optional[types.SpeechSequence]:
	sequence = []
	if speechCommand is not None:
		sequence.append(speechCommand)
	sequence.append(message)
	if message:
		return sequence


class AddonSettingsPanel(SettingsPanel):

	title = ADDON_SUMMARY

	def makeSettings(self, settingsSizer):
		sHelper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: label of a dialog.
		self.focusMessagesCheckBox = sHelper.addItem(wx.CheckBox(self, label=_("&Automatic messages for focus")))
		self.focusMessagesCheckBox.SetValue(config.conf["controlUsageAssistant"]["focusMessages"])
		# Translators: label of a dialog.
		setClickableObjLabel = _("Type the message to be used when an object can be activated")
		self.setClickableObjEdit = sHelper.addLabeledControl(setClickableObjLabel, wx.TextCtrl)
		try:
			self.setClickableObjEdit.SetValue(config.conf["controlUsageAssistant"]["clickableObjectMessage"])
		except Exception:
			self.setClickableObjEdit.SetValue("")
		# Translators: label of a dialog.
		outputModesLabel = _("Sele&ct output modes for automatic messages")
		outputModesChoices = [
			# Translators: label of a dialog.
			_("Speech"),
			# Translators: label of a dialog.
			_("Braille"),
		]
		self.outputModesList = sHelper.addLabeledControl(
			outputModesLabel, gui.nvdaControls.CustomCheckListBox, choices=outputModesChoices
		)
		checkedItems = []
		if config.conf["controlUsageAssistant"]["speech"]:
			checkedItems.append(0)
		if config.conf["controlUsageAssistant"]["braille"]:
			checkedItems.append(1)
		self.outputModesList.CheckedItems = checkedItems
		self.outputModesList.Select(0)
		# Translators: label of a dialog.
		pitchLabel = _("&Pitch change for automatic messages")
		self.pitchEdit = sHelper.addLabeledControl(
			pitchLabel,
			gui.nvdaControls.SelectOnFocusSpinCtrl,
			min=-30,
			max=30,
			initial=config.conf["controlUsageAssistant"]["pitch"]
		)

	def onSave(self):
		config.conf["controlUsageAssistant"]["focusMessages"] = self.focusMessagesCheckBox.GetValue()
		config.conf["controlUsageAssistant"]["clickableObjectMessage"] = self.setClickableObjEdit.GetValue()
		config.conf["controlUsageAssistant"]["speech"] = self.outputModesList.IsChecked(0)
		config.conf["controlUsageAssistant"]["braille"] = self.outputModesList.IsChecked(1)
		config.conf["controlUsageAssistant"]["pitch"] = self.pitchEdit.GetValue()

