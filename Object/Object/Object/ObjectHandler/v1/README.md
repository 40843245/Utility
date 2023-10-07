# ObjectHandler.Filler (1th version)
## Objective
1. Fill the object with default value.

## Rule
Rule 1:

If expectedLength is not a positive integer, an exception or runtime error will be thrown.

Rule 2:
If expectedType is not one of these: 

"list" 

"tuple"

, an exception or runtime error will be thrown.

Rule 3:

If length of src is greater than or equal to expectedLength, then it will not fill anything, just convert it to a expectedType-type object.

Rule 4:

Otherwise, if src is passed as None or empty (i.e. length of src is equal to 0) , then combine src and val 

where val is filled expectedLength times with defaultElem, then converting the resultant to object with expectedType type.

Rule 5:

Otherwise, then combine src and val 

where val is filled expectedLength times with ( defaultElem - length of src ) , then converting the resultant to object with expectedType type.

For more details, see the following examples.

## Example
### Example 1
### Code
    r = ObjectHandler.Filler.Fill(
        None,
        "list",
        2,
        4
    )
    print(r)
### Output
    [4, 4]
### Explanation
src is passed as None. According to Rule 4, 4 will be filled two times, converting it to a list, getting

    [4 , 4]

### Example 2
### Code
    r = ObjectHandler.Filler.Fill(
        [ 1 ] ,
        "list",
        2,
        4
    )
    print(r)
### Output
    [1, 4]
### Explanation
According to Rule 4, fill 4 one time ( expectedLength == 2 and len(src) == 1 => expectedLength -  len(src) == 2 - 1 == 1 ), and combine a list with 1, the resultant. Lastly, converting it to list, getting

    [1 , 4]

### Example 3
### Code
    r = ObjectHandler.Filler.Fill(
        [ 1 , 5 ],
        "list",
        2,
        4
    )
    print(r)
### Output
    [1, 5]
### Explanation
According to Rule 3, does not fill anything, getting

    [1 , 5]
    
### Example 4
### Code
    r = ObjectHandler.Filler.Fill(
        [ ] ,
        "list",
        2,
        4
    )
    print(r)
### Output
    [4,4]
### Explanation
According to Rule 4, 4 will be filled two times and converts it to list, getting

    [4,4]
    
### Example 5
### Code
    r = ObjectHandler.Filler.Fill(
        [ 1 , 3 , 4] ,
        "list",
        2,
        4
    )
    print(r)
### Output
    [1, 3, 4]
### Explanation
According to Rule 3, does not fill anything, getting

    [1, 3, 4]
    
### Example 6
### Code
    r = ObjectHandler.Filler.Fill(
        ( 1 , 2 , 3) ,
        "tuple",
        2,
        4
    )
    print(r)
### Output
    [1, 3, 4]
### Explanation
According to Rule 3, does not fill anything, getting

    (1, 2, 3)    
## API
### class ObjectHandler()
#### class Filler()
##### def Fill()
Fill the source (named src) with default value (named defaultElem), up to number of expectedLength elem, if neeeded. 
Then converts it to an expectedType-type object.

For more details, see the above rules.

Syntax :
        
        @staticmethod
        def Fill(
                src : ( None | list | tuple ),
                expectedType : str ,
                expectedLength : int ,        
                defaultElem
        ):

Parameter :

1. src : source.
2. expectedType : must be a string that one of these: "list","tuple". It indicates the type that resultant will be converted to.
3. expectedLength : must be a positive integer. It indicates the expected length of returned value (if fill is required. See above rules.)
4. defaultElem : the element that is filled for.

Returned value :

returns resultant after filling.

## Release Notes
### 2023/10/07 16:19 
Initial Notes
