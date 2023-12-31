# ClassParser (List all members of the class) (1st version)
## Programming Language 
    Python
## Objectives
    1. Given a specified class, return all user-defined members with the class. 
    For convenience, I will define these terms. (See Definition section)
    The reason why I call it is that the returned result looks likes a tree.
    User-defined methods ( funcs ) and class (including nested func and class) are available members (i.e. they can be listed).
    However, I found a serious issue -- for func and class which is nested in a func, it is impossible to be listed.
    ( I will try to fix it in later versions. )
For more fully understand, see Example section and evaluate all example by yourself with pens and papers.
For more fully understand about known issues, see Known Issues section.

## Definition
First I redefine member of the given  class as
    
    user-defined method (similar to func) and class in the given class.

Lastly, for convenience, I will introduce the terms about tree (tree in data structure) to define these following terms.

Member tree of the class :
        
        All user-defined members with the class

Node :

        Member (which are redefined)

Child :

        Iff member y is a directly user-defined in member x, 
        it is called that member y is a child of member x.

Parent :

        Iff member y is a child of member x,
        it is called that member x is a parent of member y.

Descendent (excluding child) :

        Iff member y is a indirectly user-defined in member x (i.e. y is user-defined in x but y is NOT directly user-defined in x), 
        it is called that member y is a descendent of member x.

Ancestor (excluding parent) :

        Iff member y is a descandent of member x,
        it is called that member x is an ancestor of member y.
        Note that the definition of term -- descendent.

Child-And-Descendent (including child):
        
        Iff member y is a user-defined in member x (unless directly and indirectly user-defined member), 
        it is called that member y is a descendent of member x.
        It is the intersection of child and descendant.

Parent-And-Ancestor (including parent):

        Iff member y is a Child-And-Descendent of member x,
        it is called that member x is an Parent-And-Ancestor of member y.
        It is the intersection of parent and ancestor.
        
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
    
    r = ClassFuncParser.GetMemberTree( 
                                    target = "TestClass" , 
                                    availables = globals(),
                                    searchMode = RecursiveModeEnum.NONRECURSIVE_ALL ,
                                    result = None , 
                                    firstTime = True
                                  )

#### Output ( result in Spyder of Anaconda )
It looks like this. Although the indentation may be different, it is not important for us.

    [['Hello', 'function', []], ['Sound', 'function', []], ['a', 'class', [('a1_1', <class '__main__.TestClass.a.a1_1'>), ('a1_func1', <function               TestClass.a.a1_func1 at 0x0000024ED44E4CC0>)]], ['a1_1', 'class', [('a1_1_func1', <function TestClass.a.a1_1.a1_1_func1 at 0x0000024ED44E4E00>),           ('a1_1_func2', <function TestClass.a.a1_1.a1_1_func2 at 0x0000024ED44E4EA0>)]], ['a1_1_func1', 'function', []], ['a1_1_func2', 'function', []],            ['a1_func1', 'function', []]]
## Used Module
I have used these modules.

    Enum (built-in)
    inspect (built-in)

## Explanation of members in ClassFuncParser
### ClassFuncParser.GetMemberTree 
#### Parameter
target :
        
        The target you want to find. 
        You can think that the target is the root of the tree.
        It must be the name of class ( str type ).
        
availables :

        The availables we start to search for at first round ( in the func call -- ClassFuncFinder.GetClass(className=splittedS[0],availables=availables) )
        Note that its value should always be globals(). 
        Otherwise, one may get unexpected results.
searchMode :
    
        The mode we want to search for.

        Note that its value should be always one of enum class -- RecursiveModeEnum .
        
        VISIT_DEPTH_1 (experimental)
        NONRECURSIVE_ALL

        VISIT_DEPTH_1 indicates that it will search for only childs of the class.

        while NONRECURSIVE_ALL indicates that it will search for all Child-And-Descendant of the class through non-recursive approach. 

## NOTICE
Notice that 
        
        1. Ensure that these two files ../ClassParser.py and ../test.py are placed in same directory. 
        Otherwise, you will get error -- ModuleNotFoundError which indicates the module is missing or NOT found.

        2. Check the used modules (in Used Module section) can be used in Python.

## Known Issues
1. Child-And-Descendant of a func is NOT listed currently.
2. NOT implement the argument searchMode = VISIT_DEPTH_1 .
3. result = None , firstTime = True is dummy and useless. (I will remove it in future version.)

## Release Notes
### 2023/09/13 11:52
Initial Notes
### 2023/09/13 12:13
Fix the time of Release Notes.
