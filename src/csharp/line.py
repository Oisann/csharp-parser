import re

class CsharpLine(object):
    
    def __init__(self, line, line_number, in_file):
        self.content = line.split("\n", 1)[0]
        self.number = line_number
        self.file = in_file
    
    def isEmpty(self, content=None):
        if content:
            return len(content.strip()) <= 0
        return len(self.content.strip()) <= 0
    
    def updateContent(self, new_content):
        self.content = new_content
    
    def getContent(self, stripped=False):
        if stripped:
            return self.stripComments()
        return self.content

    def removeSingleLineComment(self, line=None):
        if line == None:
            line = self.content
        quoteSign = ""
        single_line_comment_removed = ""
        for index, char in enumerate(line):
            if index > 0:
                last = line[index-1]
            else:
                last = ""
            if (char == "'" or char == '"') and last != "\\":
                if len(quoteSign) == 0:
                    quoteSign = char
                else:
                    if quoteSign == char:
                        quoteSign = ""
            if len(quoteSign) == 0:
                if char == "/" and last == "/":
                    single_line_comment_removed = line[:index-1]
                    return single_line_comment_removed.rstrip()
        if len(single_line_comment_removed) == 0:
            return line
        return single_line_comment_removed
    
    def removeMultiLineCommentEnd(self, line=None):
        if line == None:
            line = self.content
        quoteSign = ""
        multi_line_comment_end = ""
        for index, char in enumerate(line):
            if index > 0:
                last = line[index-1]
            else:
                last = ""
            if (char == "'" or char == '"') and last != "\\":
                if len(quoteSign) == 0:
                    quoteSign = char
                else:
                    if quoteSign == char:
                        quoteSign = ""
            if len(quoteSign) == 0:
                if last == "*" and char == "/":
                    return line[index + 1:]
        if len(multi_line_comment_end) == 0:
            multi_line_comment_end = line
        return line
    
    def removeMultiLineComments(self, line=None, continue_to_next_line=True):
        if line == None:
            line = self.content
        quoteSign = ""
        inComment = False
        multi_line = ""
        for index, char in enumerate(line):
            if index > 0:
                last = line[index-1]
            else:
                last = ""
            if (char == "'" or char == '"') and last != "\\":
                if len(quoteSign) == 0:
                    quoteSign = char
                else:
                    if quoteSign == char:
                        quoteSign = ""
            if len(quoteSign) == 0:
                if inComment:
                    if last == "*" and char == "/":
                        inComment = False
                else:
                    if last == "/" and char == "*":
                        inComment = True
                        multi_line = multi_line[:-1]
                    else:
                        multi_line += char
            else:
                multi_line += char
        if inComment and continue_to_next_line:
            next_line = self.file.getLine(self.number + 1)
            if next_line:
                next_line.updateContent(f"/*{next_line.getContent()}")
        return multi_line

    def stripComments(self):
        line = self.content
        # whitespace???
        if self.isEmpty():
            return line
        # Remove everything behind //, ignore scanning inside a string (quotes)
        line = self.removeSingleLineComment(line=line)
        # Remove multiline comments, except inside strings.
        line = self.removeMultiLineComments(line=line, continue_to_next_line=True)
        return line