# ContentHandler.py (all version)
## Objectives
Given a string as file content, one can 
1. find all classes and its info.

For each class, the result contains class name and all methods.

For each class, the result contains method name, argument and returned type.

For more details, see Examples.

# v1
## API
### class ContentFinder()
#### class Class()
##### def GetInfo()
Find all classes and its info.

Syntax : 

        @staticmethod
        def GetInfo(content:str):

Parameter :
1. content : string as file content.

Returned Value : 

A list that indicates all info. (See the comments of the code in ContentHandler.py and examples for more details.)

## Used Modules
My developed modules:

    REHandler
    FuncHandler
    ClassHandler
    
## Examples
### Example 1
#### Input
    s = 'class Response(): def Unknown(): pass \nclass Animal(): def Dog(): pass'
#### Output
    [['Response', ('Unknown', [['', None]], 'pass \n')], ['Animal', ('Dog', [['', None]], 'pass')]]
#### Explanation

In this example, there are two classes: Response and Animal.

In class Response, there are one method: Unknown which has no parameter and it does nothing (the keyword pass refers nothing to do).

Similary, in class Animal, there are one method: Dog which has no parameter and it does nothing (the keyword pass refers nothing to do).

# v2
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
    r = ContentFinder.Class.GetInfo(s)
#### Output
        [('DemoClass', '', 'def Func1():\n            pass\n   '), ('DemoClass', '', 'def Func2():\n            pass\n        \n        def Func1():\n            return "Method Func1 of DemoClass in demo_2.py file."\n    ')]
## Release Notes
### 2023/10/22 10:40
Initial Notes.
### 2023/10/22 11:49
Add 2th version.
