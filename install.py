import sys
import os, os.path
import shutil

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

def main(skyrim_dir):
    for node in os.listdir(os.getcwd()):
        node = os.path.join(os.getcwd(), node)
        if (os.path.isdir(node)):
            copy_tree(node, skyrim_dir)

if (__name__ == "__main__"):
    if (len(sys.argv) == 3):
        main(sys.argv[2])
    else:
        print("usage:\npython install.py <Skyrim_Directory>")