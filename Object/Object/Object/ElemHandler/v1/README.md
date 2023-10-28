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
#### Input
See ../v2/Examples/Example1/Input
#### Output
See ../v2/Examples/Example1/Output

## Release Notes
### 2023/10/08 8:55
Initial Notes
### 2023/10/28 17:55
Upload the 2th version.

