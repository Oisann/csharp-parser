#!/usr/bin/env python3

import os.path

from csharp import parser

def main():
    dirname = os.path.dirname(__file__)
    file = parser.CSharpParser(os.path.join(dirname, "../csharp_test_files/basic.cs"))
    file.parse()
    for line in file.getLines():
        print(line.getContent(True) + "$" + str(line.indentation) + "-" + str(line.isEmpty()))

if __name__ == "__main__":
    main()