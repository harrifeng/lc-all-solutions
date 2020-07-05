from os import listdir
from os.path import isfile, join
from pathlib import Path
from shutil import copyfile
import fileinput
import os
import re
import sys


def change_target_file(target):
    cnt = 0
    for line in fileinput.input(target, inplace=True):
        if re.search("from|Solution|^  def|    \"\"\"|    :type|    :rtype", line):
            print(line, end="")

if __name__ == "__main__":
    target_dir = "."

    pathlist = Path(target_dir).glob("**/*.py")

    for path in pathlist:
        # print(path)
        change_target_file(path)
