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
      
## Used Modules
      1. inspect
      2. FuncChecker (my own)
## Release Notes
### 2023/09/16 20:44
initial Notes
