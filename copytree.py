import os
from locale import Error
from shutil import copy2, copystat

from copy3 import Filter

def copytree(src, dst, symlinks=False):
    names = os.listdir(src)
    dst = dst.lower()
    os.makedirs(dst)
    errors = []
    class_founded = Filter(src, dst)
    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        print(dst, name)
        class_founded.setName(name)
        try:
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                copytree(srcname, dstname, symlinks)
            else:
                index = name.rfind(".")
                ext = name[index+1:]
                class_founded.setExt(ext)
                if (ext in ["html", "htm", "php", "css", "js"]) and not class_founded.patternFounded():
                    class_founded.copy3()
                else:
                    copy2(srcname, dstname)
            # XXX What about devices, sockets etc.?
        except OSError as why:
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except Error as err:
            errors.extend(err.args[0])
    try:
        copystat(src, dst)
    except OSError as why:
        # can't copy file access times on Windows
        if why.winerror is None:
            errors.extend((src, dst, str(why)))
    if errors:
        raise Error(errors)