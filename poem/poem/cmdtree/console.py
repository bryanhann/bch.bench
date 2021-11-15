import sys
from poem.cmdtree.class_CMD import CMD
from pathlib import Path
def usage4path():
    path = Path(sys.argv[1])
    print('hello', sys.argv)
    cmd = CMD(path)
    print(cmd.dusage)
