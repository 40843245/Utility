# ArgvsHandler.py (1th version)
## Objectives
Given a string as arguments , it can get info (name, type hinting etc) for each parameter.
## Examples
### Example 1
#### Input
    s = """
    argv1 : list,argv2 : tuple ,argv3 : dict
    """
    r = ArgvsHandler.Argv.String.GetInfo(s)
#### Output
    [['argv1', 'list'], ['argv2', 'tuple'], ['argv3', 'dict']]
## API
### class ArgvsHandler()
#### class Argv()
##### class String()
###### def GetInfo()
Syntax :

            @staticmethod
            def GetInfo(s:str):

Parameter :
1. s : string as file content.

Returned Value :

A list that indicates name of parameter and type hinting of parameter for each parameter.

## Release Notes
### 2023/10/22 11:12
Initial Notes.
