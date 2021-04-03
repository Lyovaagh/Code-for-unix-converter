import os
import re
from argparse import ArgumentParser

"""Clear founded item and replace in originalLine

Parameters:
founded (string): founded  string with (.PHP|.html|.htm|.js|.css) for cleaning
originalLine (string): current line
Returns:
string:Returning originalLine

files encoding UTF-8
https://extendsclass.com/regex-tester.html#python
"""
pathSign = "/"

cre = re.compile(
    r'(["]|["][\.]{1,2}[\/]).{2,}?(\.PHP|\.html|\.htm|\.js|\.css){1}["]', re.IGNORECASE)


def clearLine(founded, originalLine):
    elq = founded
    if founded[:3] == "src":
        index = founded.find("\"")
        if index != -1:
            founded = founded[index+1:]
            index = founded.find("\"")
            if index != -1:
                founded = founded[:index]
                elq = founded
                index = founded.find(".")
                if index != -1:
                    index = founded.rfind(pathSign)
                    if index != -1:
                        originalLine = originalLine.replace(
                            founded, founded[:index].lower() + founded[index:])
    else:
        elq = founded
        index = founded.find(".")
        if index != -1:
            index = founded.rfind(pathSign)
            if index != -1:
                originalLine = originalLine.replace(
                    founded, founded[:index].lower() + founded[index:])
    return originalLine


"""find reExpress and Clearer originalLine

Parameters:
originalLine (string): Original Line for prepafre

Returns:
string:Returning originalLine

"""


def findElemsInLine(originalLine):
    match = cre.search(originalLine)
    if match:
        founded = match.group(0)
        index = founded.rfind("\"")
        if index != -1:
            founded = founded[:index]
        index = founded.rfind("\"")
        if index != -1:
            founded = founded[index+1:]
            originalLine = clearLine(founded, originalLine)
            return originalLine
    else:
        return originalLine


"""Summary or Description of the Function recursiveFiles

Parameters:
lowerPath (string): corrected line for replacing
originalPath (string): line for replacing
Returns:
void:Returning void

"""


def prepareLinks(lowerPath, originalPath):
    # convert also pats in links
    fout = open(lowerPath + "/." + originalPath, "w+", encoding="utf8")

    with open(lowerPath + pathSign + originalPath, encoding="utf8") as fin:
        # with file.open() as fin:
        for originalLine in enumerate(fin):
            # originalLine with filtered src and href
            originalLine = findElemsInLine(originalLine)
            if args.rtrim:
                originalLine = originalLine.rtrim()
            fout.write(originalLine)

        fin.close()
        fout.close()
        if args.replace:
            os.remove(lowerPath + pathSign + originalPath)
            os.rename(lowerPath + "/." + originalPath, lowerPath + pathSign + originalPath)


"""Summary or Description of the Function recursiveFiles

Parameters:
path (string): Description of path for converting to Unis
src (string): name of directory with program for converting
Returns:
int:Returning void

"""


def recursiveFiles(path, src):
    lowerPath = path + pathSign
    originalPath = lowerPath + src
    files = os.listdir(originalPath)
    if not len(files):
        return

    isNotLower = not src.islower()
    dest = src.lower()
    lowerPath = lowerPath + dest
    if isNotLower:
        # convert directory name to lower case
        os.rename(originalPath, lowerPath)

    for originalPath in files:
        isDirectory = os.path.isdir(lowerPath + pathSign + originalPath)
        # isFile = os.path.isfile(lowerPath + pathSign + originalPath)
        if isDirectory:
            recursiveFiles(lowerPath, originalPath)
        else:
            f_name, f_ext = os.path.splitext(originalPath)
            if f_ext in [".html", ".htm", ".php", ".js"]:
                # convert also pats in links
                prepareLinks(lowerPath, originalPath)


def main():
    parser = ArgumentParser()
    parser.add_argument("input_directory", help="Read data from this directory")
    # parser.add_argument("-t", "--trim", dest="filename", help="trim lines", metavar="FILE")
    parser.add_argument("-t", "--rtrim", action="store_true",
                        help="stripped char=' ' from the end of the linees")
    parser.add_argument("-r", "--replace", action="store_true",
                        help="stripped char=' ' from the end of the linees")
    args = parser.parse_args()
    # print(args.input_directory, args.rtrim, args.replace)
    path = args.input_directory
    index = path.rfind(pathSign)
    if index != -1:
        recursiveFiles(path[:index], path[index+1:])


# main()
if __name__ == '__main__':
    main()
# path = "C:/temp/programs/PreparePythonCodeForUnix/aaa"
