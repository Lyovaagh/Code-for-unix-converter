import os
import re
import json

class Filter:

    def __init__(self, src, dst, founded=""):
        self.src = src
        self.dst = dst
        self.founded = ""
        self.name = ""
        self.srcname = ""
        self.dstname = ""
        self.str_re = Filter.generateExp()
        self.cre = re.compile(self.str_re, re.IGNORECASE)

    def setName(self, name):
        self.name = name
        self.srcname = os.path.join(self.src, name)
        self.dstname = os.path.join(self.dst, name)
    
    exts = []
    @staticmethod
    def setExt(ext):
        ext = ext.lower()
        if ext not in Filter.exts:
            Filter.exts.append(ext)
            print(Filter.exts)

    @staticmethod
    def generateExp():
        path = os.path.dirname(os.path.realpath(__file__)) + os.sep
        with open(path + "config.json", "r") as read_file:
            data = json.load(read_file)
            data.insert(0, "")
            data = "|\.".join(data)
            elq = '(["]|["][\.]{1,2}[\/]).{2,}?(' + data[1:] + '){1}["]'
            print( elq )
            # print("r'" + elq + "'")
        return elq
        # return re.compile( elq )
    

    def copy3(self):
        f = open(self.srcname, "r")
        copy = open(self.dstname, "w")
        for line in f:
            copy.write(self.findElemsInLine(line))
        f.close()
        copy.close()

    def patternFounded(self):
        f = open(self.srcname, "r")
        try:
            lines = f.read()
            f.close()
            match = self.cre.search(lines)
            if match:
                return self.findPatternInAnyLine()
        except:
            return True

    def findPatternInAnyLine(self):
        f = open(self.srcname, "r")
        elq = True
        for line in f:
            if not self.isValidPattern(line):
                elq = False
                break
        f.close()
        return elq

    def isFoundedPatternLowerCase(self, founded):
        founded = founded[:-2]
        index = founded.rfind("/")
        log = True
        self.founded = ""
        if index != -1:
            founded = founded[:index]
            log = founded == founded.lower()
            self.founded = founded
        return log

    def clearLine(self, founded, line):
        founded = founded[:-3]
        index = founded.rfind("/")
        founded = founded[:index]
        return line.replace(founded, founded.lower())

    def findElemsInLine(self, line):
        match = self.cre.search(line)
        if match:
            founded = match.group(0)
            index = founded.rfind("\"")
            if index != -1:
                founded = founded[:index]
            index = founded.rfind("\"")
            if index != -1:
                founded = founded[index + 1:]
                return self.clearLine(founded, line)
        else:
            return line

    def isValidPattern(self, line):
        match = self.cre.search(line)
        if match:
            founded = match.group(0)
            index = founded.rfind("\"")
            if index != -1:
                founded = founded[:index]
            index = founded.rfind("\"")
            if index != -1:
                founded = founded[index + 1:]
                return self.isFoundedPatternLowerCase(founded)
        else:
            return True
