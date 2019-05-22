# C# Parser

This is a C# parser written in Python 3 intended to validate the code style of a [Unity](https://www.unity.com/) project, in a CI/CD pipeline.

## Idea & Background

I have decided to make this in Python 3, because I want to learn how to do this in Python. This is basically my first ever Python project.
I will have to use Python at work in the future, so I might as well get used to it right away. This application is intended to run on pull/merge requests to validate the code style set by the project owner. It can be hard to enforce a certain style in bigger projects, especially in indie game projects, where people do stuff they don't really do everyday.

1. I want this program to parse the C# code given to it, then use that parsed data to check it against some rules. I don't know how the second part will work yet, but I think the parsing will be the biggest hurdle anyway. 

2. I want to run this in a docker container to easily run it anywhere.

3. I don't want this to check if the code is "valid C# code". However this could change in the future. For now, I just want the style to be correct.