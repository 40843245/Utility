# ListHandler (1th version)
## Objective
1. Handles a list (such as check a given string src ends with in any elem of given list)

## Example
### Example 1 
#### Input 
    r = ListHandler.String.EndsWith("src.py", [".py",".pym"])
    print(r)
#### Output
    True
## API
### class ListHandler()
#### class String()
##### EndsWith 
Check a given string src ends with any elem of given list target.
Syntax :

        def EndsWith(src : str, target : list[str]):
Parameter :

1. src : source. Must be a string object.
2. target : target. Must be a list of string.

Returned Value :
Return True iff a given src ends with any elem of given list target. Otherwise, return False.

## Known issue
Unexpected Output. It should not always return True.
## Release Notes
### 2023/10/08 6:17
Initial Notes.
### 2023/10/08 7:23
Add Known issues and Fix it in version v2 (in directory ../v2/)
