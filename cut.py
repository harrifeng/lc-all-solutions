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
        print(line)
        if line == '    """':
            cnt += 1
        if cnt == 2:
            break


if __name__ == "__main__":
    target_dir = "."

    pathlist = Path(target_dir).glob("**/*.py")

    for path in pathlist:
        change_target_file(path)
