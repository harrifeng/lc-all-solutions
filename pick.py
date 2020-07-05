import os
from pathlib import Path
from shutil import copyfile

target_dir = "."

pathlist = Path(target_dir).glob("**/*.md")

for path in pathlist:
    src = str(path)
    dest = src.split("/")[0].replace(".", "-")
    dest = os.path.join("./md", dest + ".md")
    print(src, dest)
    copyfile(src, dest)



