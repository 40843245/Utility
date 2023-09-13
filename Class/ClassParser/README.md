# ClassParser (List all members of the class) (1st version)
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

Descandent (excluding child) :

        Iff member y is a indirectly user-defined in member x (i.e. y is user-defined in x but y is NOT directly user-defined in x), 
        it is called that member y is a descandent of member x.

Ancestor (excluding parent) :

        Iff member y is a descandent of member x,
        it is called that member x is an ancestor of member y.
        Note that the definition of term -- descandent.
        
## Examples
### Input Class
### Settings

###
