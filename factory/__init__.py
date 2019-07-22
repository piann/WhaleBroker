import glob
import os

# for including all files with import *

subFilePathList = glob.glob("./*.py")
subFileNameList = [os.path.basename(subFilePath) for subFilePath in subFilePathList]
subFileNameList.remove("__init__.py")

__all__ = subFileNameList