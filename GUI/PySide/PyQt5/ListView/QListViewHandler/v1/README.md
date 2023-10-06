# QListViewHandler (1th version)
## Objective
Several classes that manipulates a QListView object, a QListWidget object and lots of QListWidgetItem object. (QListWidgetItem is an item of QListWidget)

## API
For more details, see the py file.
### class CloneHandler()
#### Clone()
Syntax :

    @staticmethod
    def Clone(src:QListWidget,dest:QListWidget):

### class InsertionHandler()
#### InsertRows():
Syntax :

    @staticmethod
    def InsertRows(src:QListWidget,dest:QListWidget,itemsIndex:list[int]):

### class RemovalHandler()
#### @staticmethod RemoveRows()
Syntax :

    @staticmethod
    def RemoveRows(dest:QListWidget,itemsIndex:list[int]):

### class SelectionHandler()
#### @staticmethod SelectAll()
Syntax :

    @staticmethod
    def SelectAll(src:QListWidget):
    
#### staticmethod DeselectAll()

    @staticmethod
    def DeselectAll(src:QListWidget):
    
### class QListWidgetItemHandler()
#### def SetItem()
Syntax :

    def SetItem(self,row,text):

### class QListWidgetHandler()
#### def InsertItems()
Syntax :

    def InsertItems(self,items : list[QListWidgetItemHandler] ):
    
#### def Clear()
Syntax :

    def Clear(self):

## Release Notes
### 2023/10/06 12:25
Initial Notes
