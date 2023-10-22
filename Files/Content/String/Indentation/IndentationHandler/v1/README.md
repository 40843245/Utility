# IndentationHandler.py (all version)
## Objectives
Get the info about indentation for each line with given string.

## API
For more details, see the comments in file ../v1/IndentationHandler.py
### class IndentationHandler()
#### class Indentation()
##### class String()
###### def GetIndentations()
A method that get number of indentation for each line in given string.

## Examples
NOTICE :

Be careful about letters. Both whitespace (' ') or tab ('\t') can indent in Python.
### Example 1
#### Input
    s = """
    class DemoClass():
        def Func1():
            pass
    

    class DemoClass():
        class InnerClass():
            pass
        def Func2():
            pass
    
        def Func1():
            return "Method Func1 of DemoClass in demo_2.py file."
    """
    r = IndentationHandler.Indentation.String.GetIndentations(s)
    print(s)
    print(r)
#### Output

    class DemoClass():
        def Func1():
            pass
    

    class DemoClass():
        class InnerClass():
            pass
        def Func2():
            pass
    
        def Func1():
            return "Method Func1 of DemoClass in demo_2.py file."
    
    {0: None, 1: {'whitespace': [[0, 4]], 'tab': []}, 2: {'whitespace': [[0, 8]], 'tab': []}, 3: {'whitespace': [[0, 12]], 'tab': []}, 4: {'whitespace': [[0, 4]], 'tab': []}, 5: None, 6: {'whitespace': [[0, 4]], 'tab': []}, 7: {'whitespace': [[0, 8]], 'tab': []}, 8: {'whitespace': [[0, 12]], 'tab': []}, 9: {'whitespace': [[0, 8]], 'tab': []}, 10: {'whitespace': [[0, 12]], 'tab': []}, 11: {'whitespace': [[0, 4]], 'tab': []}, 12: {'whitespace': [[0, 8]], 'tab': []}, 13: {'whitespace': [[0, 12]], 'tab': []}, 14: {'whitespace': [[0, 4]], 'tab': []}}
## Release Notes
### 2023/10/22 18:46
Initial Notes.
