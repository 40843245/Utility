# StringHandler.py (2th version)
## Objective
1. Find the occurence of keyword in given string at beginning or at end.

## Examples
### Example 1
#### Input
    s = """  class DemoClass():
        def Func1():
            pass
    """
    keyword = ' '
    r = StringHandler.GetPrefixCount(s, keyword)
    print("How many occurences are there of '%s' in '%s' at beginning?" % (keyword,s) )
    print(r)
    
    s = """  class DemoClass():
        def Func1():
            pass
    """
    keyword = ' '
    r = StringHandler.GetSuffixCount(s, keyword)
    print("How many occurences are there of '%s' in '%s' at end?" % (keyword,s) )
    print(r)
#### Output
    How many occurences are there of ' ' in '  class DemoClass():
            def Func1():
                pass
        ' at beginning?
    2
    How many occurences are there of ' ' in '  class DemoClass():
            def Func1():
                pass
        ' at end?
    4

## API
For more details,see the comments in file ../v2/Code/StringHandler.py/
### class StringHandler()
#### def GetPrefixCount()
Get the how many occurences of prefix (which is given in ) in given string (which given in s).
#### def GetSuffixCount()
Get the how many occurences of suffix (which is given in ) in given string (which given in s).
## Release Notes
### 2023/10/22 17:22
Initial Notes.
