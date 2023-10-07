# FileChecker (1th version)
## Objective
Check a given src is the specified file through its extension.
## Example
### Example 1
#### Input
    r = FileHandler.FileChecker.Microsoft.Office.Word.IsWord("test1.docx")
    print(r)
#### Output
    True
## Used Module
My developed module:

    ListHandler 
    
ListHandler module at GitHub:

https://github.com/40843245/Utility/blob/main/Object/List/ListFiller/String/v1/Code/ListHandler.py

## API
### class FileHandler()
#### class FileChecker()
##### class ProgLang()
###### class Python()
1. def IsPython()

Syntax :

    @staticmethod
    def IsPython(src)

Parameter :
1. src

Returned Value :
Returns True iff src is a python file. Otherwise, returns False.

##### class Office()
1. class Word()

def IsWord()

Syntax :

    @staticmethod
    def IsWord(src)

Parameter :
1. src

Returned Value :
Returns True iff src is a Word file. Otherwise, returns False.

2. class PowerPoint()

def IsPowerPoint()

Syntax :

    @staticmethod
    def IsPowerPoint(src)

Parameter :
1. src

Returned Value :
Returns True iff src is a PowerPoint file. Otherwise, returns False.

3. class Excel()

def IsExcel()

Syntax :

    @staticmethod
    def IsExcel(src)

Parameter :
1. src

Returned Value :
Returns True iff src is a Excel file. Otherwise, returns False.

## Release Notes
### 2023/10/08 6:34
Initial Notes.
