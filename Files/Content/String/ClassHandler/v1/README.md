# ClassHandler.py (all version)
## Objectives
1. Get the info about classes in specified string as file content.

# v1
## Examples
### Example 1
#### Input
    s = """
    class DemoClass():
        def Func2():
            pass
        
        def Func1():
            return "Method Func1 of DemoClass in demo_2.py file."
    """
    r = ClassHandler.Class.String.GetInfo(s)
#### Output
    ('DemoClass', '', 'def Func2():\n            pass\n        \n        def Func1():\n            return "Method Func1 of DemoClass in demo_2.py file."\n    ')
#### Explanation
There are one class in the file content : DemoClass.

## API
### class ClassHandler()
#### class Class()
##### class String()
###### def GetInfo()
Get the info about classes in specified string as file content.
   
Syntax :

            @staticmethod
            def GetInfo(s : str):

Parameter : 
1. s : string as content.

Returned Value :

Info about class in s.

## Used Modules
  
    None
## Used At
It is used at

    ContentHandler
# v2 
## Fixed
Many classes in the string s can be splitted as well. (In 1th version, it will always get one class which does not work expectedly.)

## Examples
### Example 1
#### Input
    s = """
    class DemoClass():
        def Func1():
            pass
    

    class DemoClass():
        def Func2():
            pass
    
        def Func1():
            return "Method Func1 of DemoClass in demo_2.py file."
    """
    r = ClassHandler.Class.String.GetInfo(s)
#### Output
    [('DemoClass', '', 'def Func1():\n            pass'), ('DemoClass', '', 'def Func2():\n            pass\n    \n        def Func1():\n            return "Method Func1 of DemoClass in demo_2.py file."\n    ')]
## Release Notes
### 2023/10/22 11:01 
Initial Notes.
### 2023/10/12 11:39 
Add the 2th version.
