# ObjectHandler.flatten (1th version)
## Objective
1. Expand a list or a tuple.
## Examples
### Example 1
#### Input
    array1 = [ 1,8,9,[2,4] ]
    array2 = ObjectHandler.flatten(array1)
    print(array2)
    r = sum(array2)
    print(r)
#### Output
    [1, 8, 9, 2, 4]
    24
### Example 2
#### Input
    array1 = ( 1,8,9,(2,4) )
    array2 = ObjectHandler.flatten(array1)
    print(array2)
    r = sum(array2)
    print(r)
#### Output
    [1, 8, 9, 2, 4]
    24
### Example 3
#### Input
    array1 = [ 1,8,9,(2,4) ] 
    array2 = ObjectHandler.flatten(array1)
    print(array2)
    r = sum(array2)
    print(r)
#### Output
    [1, 8, 9, 2, 4]
    24
### Example 4
#### Input
    array1 = ( 1,8,9,[2,4] )
    array2 = ObjectHandler.flatten(array1)
    print(array2)
    r = sum(array2)
    print(r)
#### Output
    [1, 8, 9, 2, 4]
    24
## API
### class ObjectHandler()
#### def flatten()
Expand a list or a tuple.

Syntax : 

    @staticmethod
    def flatten(x):

Parameter :
1. x : src to extend.

Returned Value :
Returns the resultant after expansion of x.

## Ref
Code is modified from the question on stackoverflow,

https://stackoverflow.com/questions/2158395/flatten-an-irregular-arbitrarily-nested-list-of-lists/14781252#14781252

## Release Notes
### 2023/10/10 9:00 
Initial Notes.
