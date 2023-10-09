# OfficeFilesHandler (1th version)
## Objective
Handles Microsoft Office files. 
1. It can search and replace text.
## API
### class OfficeFilesHandler()
#### def SearchAll()
Search all occurences of text in the given fullname.

Syntax :

    @staticmethod
    def SearchAll(
        fullname : str ,
        searchText : str
    ):

Parameter :
1. fullname : The full name of file.
2. searchText : text to search.

Returned Value :

Info about all occurences of text after searching.

#### def ReplaceAll()
Replace all text in the given fullname.

Syntax :

    @staticmethod
    def ReplaceAll(
        fullname : str ,
        searchText : str,
        replaceText : str
    ):

Parameter :
1. fullname : The full name of file.
2. searchText : text to search.
3. replaceText : text to replace.

Returned Value :

Info about all occurences of text after searching.

## Release Notes
### 2023/10/09 11:20
Initial Notes.
