# ExcelsHandler (1th version)
## Objective
1. Manipulates many excels files. 
   (such as search and replace etc)

## API
### ExcelsHandler
Manipulates many excels files by visiting each elem of WorkbookHandler object once.

#### SetInputFullNames
Set the full path and name of many input files.

Syntax :
    
    SetInputFullNames(self,inputFullNames : list[str] )

Parameter :

1. self : Of course, is a instance itself.
2. inputFullNames : a list of string. It indicates full path and name of many input files.

Return Value : 

None

#### Load

Loads the files.

Syntax :
  
    Load(self)

Parameter :

1. self : Of course, is a instance itself.

Return Value : 

None

#### Search

Searches the keyword for loaded files. 

NOTICE that

it is case-sensitive and matching whole word only. i.e. They will be matched iff the value of cell must be exactly same of searchText.

Syntax :
  
    Search(self,searchText:str)

Parameter :

1. self : Of course, is a instance itself.
2. searchText : it should be a string type object . It is a keyword for searching.

Return Value : 

Returns a 3D-like list.

Looks like:

    [[[], [<Cell '日本動漫'.C2>, <Cell '日本動漫'.H2>, <Cell '日本動漫'.K2>, <Cell '日本動漫'.C3>, <Cell '日本動漫'.H3>, <Cell '日本動漫'.K3>, <Cell '日本動漫'.C4>, <Cell '日本動漫'.H4>, <Cell '日本動漫'.K4>]], [[], [<Cell '日本動漫'.C2>, <Cell '日本動漫'.H2>, <Cell '日本動漫'.K2>, <Cell '日本動漫'.C3>, <Cell '日本動漫'.H3>, <Cell '日本動漫'.K3>, <Cell '日本動漫'.C4>, <Cell '日本動漫'.H4>, <Cell '日本動漫'.K4>]]]

Each elem of the 3D-like list indicates the cell 

where they are matched.

Again to NOTICE that

it is case-sensitive and matching whole word only. i.e. They will be matched iff the value of cell must be exactly same of searchText.

Lists in 3th dimension indicates all matched cells in the worksheet.

Lists in 2th dimension indicates all matched cells in the workbook (in one excel file).

Lists in 1th dimension indicates all matched cells in many files.

A empty list in 3th dimension indicates that there are no matched cells in the worksheet.

A empty list in 2th dimension indicates that there are no matched cells in the workbook.

A empty list in 1th dimension indicates that there are no matched cells in many files.

#### Definition of 3D-list with RE ( regular expression )

    # {cell} refers a cell object.
    {1thDimensionalList} := ( \[ \] | \[ {cell} ( ,  {cell})*  \] )
    {2thDimensionalList} := ( \[ \] | \[ {1thDimensionalList} ( ,  {1thDimensionalList})*  \] )
    {3thDimensionalList} := ( \[ \] | \[ {2thDimensionalList} ( ,  {2thDimensionalList})*  \] )

#### Replace

Replace cells which values exactly are searchText into replaceText.

Syntax :
   
      Replace(self,searchText:str,replaceText:str):

Parameter:

1. self : Of course, is the instance itself.
2. searchText : text to be replaced for.
3. replaceText : text that will be replaced to.

Returned Value

A 2D-like list.

### WorkbookHandler
Manipulates all worksheets of one file.

#### SetInputFullName
Set the full path and name of the input file.

Similar to ExcelsHandler.SetInputFullNames . 

Syntax :

      SetInputFullName(self,inputFullName: str)

Parameter :
1. self : Of course, is the instance itself.
2. inputFullName : the full path and name of the input file.
   
Returned Value :

None

      


