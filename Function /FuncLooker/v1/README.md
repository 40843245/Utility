# FuncLooker (Get info about function) (1th version)
## Objectives
      1. Get info about function
## Examples
### Example 1
#### Code
    def Func1():
            return 2
        testList = [
            Func1,
            lambda x : x + 2 , 
            2,
            dir(4),
            callable
         ]
        resultList =[
            FuncLooker.ArgLooker.GetArgsName(func=elem) for elem in testList
        ]
        print(resultList)
#### Output
    [[], ['x'], [], [], ['obj']]
## NOTICE
      Since I write a module -- FuncChecker named FuncChecker.py . 
      Please download it from  ../FuncChecker/v1/Code/FuncChecker.py (where v1 is the 1th version, I may update it in the future. Please pay attention on it.)
      Then import the module with the keyword import before use. Such as
            from FuncChecker import FuncChecker    
## Known issues
A runtime error occured -- ValueError while running inspect.signature(func) when the parameters are some keywords for basic type such as bool, int, str, dict. It will looks like this.

      ValueError: no signature found for builtin type <class 'dict'>

But I can ensure that there are no error with keywords 

      float, list, tuple.
      
## Used Modules
      1. inspect
      2. FuncChecker (my own)
## Release Notes
### 2023/09/16 20:44
initial Notes
### 2023/09/16 21:05
Added
       
      Known issues
