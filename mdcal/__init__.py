from pathlib import Path

import pkg_resources

__version__ = pkg_resources.require("mdcal")[0].version

MODULE_DIR = Path(__file__).resolve().parent
