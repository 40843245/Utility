# ListHandler (1th version)
## Objective
A class that checks the given string ends with in any elem of the given list.
## API
### class ListHandler()
#### class String()
##### def EndsWith()
Checks the given string ends with in any elem of the given list.

Syntax :

    @staticmethod
    def EndsWith(src : str, target : list[str])
        
Parameter : 
1. src : Source. Must be a str.
2. target : Target. Must be a list of str.

Returned Value :

Returns True iff src ends with any elem of target. Otherwise, returns False.
