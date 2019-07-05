from .line import CsharpLine

class CSharpParser():
    
    def __init__(self, filename, tabsize=4):
        self.filename = filename
        self.tabsize = tabsize
        self.raw_lines = []

    def parse(self):
        with open(self.filename, 'r') as file:
            for i, line in enumerate(file):
                #TODO: Handle tab sizes and remove that from line contents
                self.raw_lines.append(CsharpLine(line, i + 1, self, self.tabsize))
    
    def getLine(self, line):
        if line > len(self.raw_lines) or line <= 0:
            return None
        elif line > 0:
            return self.raw_lines[line - 1]

    def getLines(self):
        return self.raw_lines