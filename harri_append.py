from os import listdir
from os.path import isfile, join
from pathlib import Path
from shutil import copyfile
import fileinput
import os
import re
import sys

def append_to_question(path):
    parent = path.split("/")[0]
    question = "/".join([parent, "questin.md"])
    print(path, question)


if __name__ == "__main__":
    target_dir = "."

    pathlist = Path(target_dir).glob("**/*.py")

    for path in pathlist:
        p = str(path)
        if "harr" not in p:
            append_to_question(p)
