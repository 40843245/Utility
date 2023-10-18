# NestedFlatter.py (all version)
## Objectives
1. A class that flats nested array-like objects.

# 1th version
## Example 
Examples with NestedFlatter.Flat .
### Example 1 
#### Input
    items = [ [1,2,3] ,['a','b','c']]
#### Output
    ['1' '2' '3' 'a' 'b' 'c']
### Example 2 (Example with error due to inhomogeneous shape)
#### Input
     [ [ [1,2,3] ,['a','b','c'] ] , ['q','w','e'] ]

## Used Modules
    numpy
## Known issues or issues that will be improved.
1. Always returns a list (whenever the input nested array-like object is (either a nested list or a nested array))
   (not an issue, and improved in 2th version)
# 2th version
## Example 
Examples with NestedFlatter.Flat .
For more examples, see previous examples in 1th version.
### Example 1 
#### Input
    items = ( (1,2,3) ,('a','b','c' ) )
#### Output
       ('1', '2', '3', 'a', 'b', 'c')

## Release Notes
### 2023/10/18 20:34
Initial Notes.
### 2023/10/18 20:50
Update the code (for latest code, see ../v2/Code/NestedFlatter.py)
### 2023/10/18 21:02
Update the examples of 1th version.
