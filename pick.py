import os
from pathlib import Path
from shutil import copyfile

target_dir = "."

pathlist = Path(target_dir).glob("**/*.md")

for path in pathlist:
    src = str(path)
    dest = os.path.join("./md", src.split("/")[0] + ".md")
    print(src, dest)
    copyfile(src, dest)



