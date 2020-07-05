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
    question = "/".join([parent, "question.md"])
    print(path, question)

    with open(path) as fp:
        src_data = fp.read()

    data = "\n```python\n" + src_data + "```\n"

    with open(question, "a") as fp:
        fp.write(data)


if __name__ == "__main__":
    target_dir = "."

    pathlist = Path(target_dir).glob("**/*.py")

    for path in pathlist:
        p = str(path)
        if "harr" not in p:
            append_to_question(p)
