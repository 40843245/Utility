# ElemHandler (1th version)
## Objective
1. Handles a list or a tuple. ( only check duplicate elem )
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

## Release Notes
### 2023/10/08 8:55
Initial Notes
