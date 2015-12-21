import sys
import os, os.path
import shutil

SKYRIM_DIRECTORY = "F:\Games\TSEV Skyrim LE"

def copy_tree(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copy_tree(s, d)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                shutil.copy2(s, d)

def main():
    mod_dir = os.path.join(os.getcwd(), "mods")
    
    for node in os.listdir(mod_dir):
        node = os.path.join(mod_dir, node)
        if (os.path.isdir(node)):
            copy_tree(node, SKYRIM_DIRECTORY)

if (__name__ == "__main__"):
    main()