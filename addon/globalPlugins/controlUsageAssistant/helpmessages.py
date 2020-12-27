# Control Usage Assistant
# An add-on for NVDA
# Copyright 2013-2021 Joseph Lee, released under GPL.

# A database of help messages, organized by object type, control type, and app messages (if any).
# Structure mirrors that of control types module, NVDA objects collection,
# and app modules list from NVDA Core source code.
# Each part is stored within their own help module files for extensibility,
# with all of them being collected under this module.

from .controltypeshelp import *
from .nvdaobjectshelp import *
