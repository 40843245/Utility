# NestedFlatterInhomogenous (all version)
## Objectives
Similar to the NestedFlatter class in NestedFlatter.py file.
However, it can handles the nested array-like object with inhomogenous shape (rather than NestedFlatter class which can handles nested array-like object with homogenous shape.)
But, the only con of this code, is slower ideally. 

The reason why it is:

I implement it recursivelly for all elem if elem is a list (including nested list) or tuple (including nested tuple).

And each recursive call is very expensive.

# 1th version
## Examples
### Example 1
#### Input 
    items = ( (1,2,3) ,('a','b','c' ) )
#### Output
    ('a', 'b', 'c', 1, 2, 3)
### Example 2
#### Input
    items = ( ( (1,2,3) ,('a','b','c' ) ) , ('q','w','e'))
#### Output
    ('q', 'w', 'e', 'a', 'b', 'c', 1, 2, 3)

## Release Notes
### 2023/10/18 21:36
Initial Notes.
