# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
	# add-on Name
	"addon-name" : "controlUsageAssistant",
	# Add-on description
	# TRANSLATORS: Summary for this add-on to be shown on installation and add-on information.
	"addon-summary" : _("Control Usage Assistant - get brief help on interacting with the focused control"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on installation and add-on information
	"addon-description" : _("""Allows you to find out how to interact with the focused control, useful for new computer users new to Windows and to NvDA.
	Press NvDA+H to get a short help message on using the focused control, such as moving through tables, checkboxes and so on."""),
	# version
	"addon-version" : "1.0Beta2",
	# Author(s)
	"addon-author" : "Joseph Lee <joseph.lee22590@gmail.com>",
	# URL for the add-on documentation support
	"addon-url" : None
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "globalPlugins", "controlUsageAssistant", "*.py")]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
