import glob
import os

# for including all files with import *

currentDir = os.path.dirname(os.path.realpath(__file__))
subFilePathList = glob.glob(os.path.join(currentDir, "*.py"))
subFileNameList = [os.path.basename(subFilePath).split(".py")[-2] for subFilePath in subFilePathList]
subFileNameList.remove("__init__")

__all__ = subFileNameList