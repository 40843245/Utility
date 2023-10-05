# PowerpointHandler (1th version)
## Objectvie
1. Manipulate one powerpoint file ( .ppt or .pptx )
## API
### PowerPointHandler
#### SetInputFullName
Set the full path and name for input file.

Syntax :

    SetInputFullName(self,inputFullName : str)
    
Parameter :

1. inputFullName : The full path and name for input file.
    
Returned Value :

None

#### Load
Loads the input file.

Syntax :

    Load(self)
    
Parameter :

1. inputFullName : The full path and name for input file.
    
Returned Value :

None

#### GetSlider
Returns the pageIndex th slider object.

Syntax :

    GetSlider(self,pageIndex)
    
Parameter :

1. pageIndex : The page index.
    
Returned Value :

None

#### GetSliders
Returns slider object of each page.

Syntax :

    GetSliders(self)
    
Parameter :

1. pageIndex : The page index.
    
Returned Value :

None

#### SearchAll

Returns all occurences with searchText.

Syntax :

    SearchAll(self,searchText : str):
    
Parameter :

1. searchText : Text to search for.
    
Returned Value :

A list of tuple.

#### ReplaceAll

Replace all occurences with searchText to replaceText.

Syntax :

    ReplaceAll(self,searchText:str,replaceText:str):
    
Parameter :

1. searchText : Text to search for.
2. replaceText : Text to be searched.
    
Returned Value :

A list of tuple.

## Used Module
My Developement Module :
      
      StringHandler

Modules that are both NOT builtin and developed by meself.

      pptx : To dowmload, use pip install python-pptx
## Release Notes
### 2023/10/05 8:07
Initial Notes
