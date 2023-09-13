# LocalModuleFinder (Find all local module) (1st version)
## Programming Language 
    Python
## Objectives
    1. Find all local module
For more fully understand, see Example section and evaluate all example by yourself with pens and papers.
For more fully understand about known issues, see Known Issues section.

## Examples
Refer to the example class in the file ../test.py .
### Example1
#### Input Class

    class TestClass:
    def Hello():
        def HelloWorld():
            print("HelloWorld!!!")
        print("Hello!!!")
    def Sound():
        class Animal:
            class Dog:
                def Bark():
                    print("Bark!!!")
            class Cat:
                def Mow():
                    print("Mow!!!")
        print("Sound!!!")
    class a:
        def a1_func1():
            print("a1_func1!!!")
        class a1_1:
            def a1_1_func1():
                print("a1_1_func1!!!")
            @staticmethod
            def a1_1_func2():
                print("a1_1_func2!!!")
                
#### Arguments
    
    print(LocalModuleFinder.GetLocalModules())

#### Output ( result in Spyder of Anaconda )
    Reloaded modules: LocalModuleFinder
    [('OtherTestFunc1', <function OtherTestFunc1 at 0x00000291261DD1C0>), ('OtherTestFunc2', <function OtherTestFunc2 at 0x00000291261DD260>)]
    
## Used Module
I have used these modules.

     sys (built-in)
     inspect (built-in)
     types (built-in)

## Explanation of members in ClassFuncParser
### LocalModuleFinder.GetLocalModules
#### Parameter
None
#### Returned Value
    
    A list containing all local modules in the file where the method LocalModuleFinder.GetLocalModules locates at.

## NOTICE
Notice that 
        
        1. Ensure that these two files ../LocalModuleFinder.py and ../test.py are placed in same directory. 
        Otherwise, you will get error -- ModuleNotFoundError which indicates the module is missing or NOT found.

        2. Here, it will return all local modules for the file LocalModuleFinder.py NOT test.py due to the meaning of the code.
        If you want to list local modules for test.py, just paste the LocalModuleFinder to test.py to define the class LocalModuleFinder.

## Known Issues
1. Here, it will return all local modules for the file LocalModuleFinder.py NOT test.py due to the meaning of the code. ( Almost Impossible to resolve it)

## Release Notes
### 2023/09/13 13:28
Initial Notes

### Ref
Thanks to the author alecxe to reply in stackoverflow.

![image](https://github.com/40843245/Utility/assets/75050655/7bcbad28-66b6-4c5e-aecc-6cfc676cf28b)

![image](https://github.com/40843245/Utility/assets/75050655/2d81c99f-c897-4376-8c03-3732bc27f51d)



https://stackoverflow.com/questions/18451541/getting-a-list-of-locally-defined-functions-in-python

