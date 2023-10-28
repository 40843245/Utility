# ElemHandler (all version)
## Objective
1. Handles a list or a tuple.
# v1
## Example
### Example 1
#### Input
    elems = [1,2,3,4,5]
    r = ElemHandler.HasSameElem(elems)
    print(r)
    
    elems = [1,2,3,4,4]
    r = ElemHandler.HasSameElem(elems)
    print(r)
    
    elems = [1,1,2]
    r = ElemHandler.HasSameElem(elems)
    print(r)
    
    elems = []
    r = ElemHandler.HasSameElem(elems)
    print(r)
    
    elems = (1,2)
    r = ElemHandler.HasSameElem(elems)
    print(r)
    
    elems = (2,2)
    r = ElemHandler.HasSameElem(elems)
    print(r)
    
    elems = tuple()
    r = ElemHandler.HasSameElem(elems)
    print(r)
#### Output
    False
    True
    True
    False
    False
    True
    False
## API
### class ElemHandler()
#### HasSameElem
Check elems has duplication elem.

Syntax :

    @staticmethod
    def HasSameElem( elems : (list|tuple)):

Parameter :
1. elems : Must be a list or tuple.

Returned Value :

Returns True iff they have duplicated elem. Otherwise, returns False.

# v2
## Examples
### Example 1
See 

https://github.com/40843245/Utility/tree/main/Object/Object/Object/ElemHandler/%20v2/Code/Ex/Ex1

#### Input
See ../v2/Code/Ex/Ex1/Input.py
#### Output
See ../v2/Code/Ex/Ex1/Output.py

## API
For more details, see the comment in py file ../v2/Code/ElemHandler.py
### class ElemsFinder()
#### def GetOtherElem()
#### def GetTheseElem()
#### def Diff()
#### def IndicesOfSameKeys()
#### def NestedValuesOfSameKeys()
## Release Notes
### 2023/10/08 8:55
Initial Notes
### 2023/10/28 17:55
Upload the 2th version.
### 2023/10/28 18:00
Upload the test data of 2th version.

