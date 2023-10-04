# StringHandler (1th version)
## Objective
1. Split the given string as target with given a list of string.
## API
### class StringHandler
#### Split
Syntax:

    @staticmethod
    def Split( content:str,delimList : list[str] ):

Parameter:
1. content: The string as target that will be spliited.
2. delimList : The list of delimiter. It should be the list of string that will split for.

Returned Value:
A list of tuple looks like this.
    
    [ 
        (  counter , smallestFoundIndexCorr , tempList  ) 
    ]
    
where 

the counter refers the jth word,

smallestFoundIndexCorr refers index that it is splitted by the delimiter,

tempList refers that the splitted string.

## Example
### Example 1 
#### Input
content :

    a1 b2 c3\n d4

delimList : 

    [ ' ','\n','\t']
    
#### Expected Output

    [(1, 0, 'a1'), (2, 0, 'b2'), (3, 1, 'c3'), (4, 0, ''), (5, -1, 'd4')]

#### Explanation

The string "a1 b2 c3\n d4" will be splitted with one of the delimiters ' ' (i.e. whitespace), '\n' (i.e. breakline), and '\t' (i.e. tab).

Since there is ' ' between "a1" and "b2", which is in delimList, which is the 0th index of delimList. 

Thus, it is added -- (1, 0, 'a1') .

Since there is '\n' between "c3" and " ", which is in delimList, which is the 1th index of delimList. 

Thus, it is added -- (3, 1, 'c3') .

Since there is '\n' between "\n" and "d4", which is in delimList, which is the 0th index of delimList. 

Thus, it is added -- (4, 0, '') .

Since there is no chars after "d4". 

Thus, it is added -- (5, -1, 'd4') . 

#### Output
    
    [(1, 0, 'a1'), (2, 0, 'b2'), (3, 1, 'c3'), (4, 0, ''), (5, -1, 'd4')]

## Used Module

    Nothing

## Release Notes
### 2023/10/04 15:47 
Initial Notes.
