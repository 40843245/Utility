# QTableViewHandler (1th version)
## Objective
Several class that handles QTableView object, QTableWidget , QTableWidgetItem.
## Example
See my code QTableViewHandler.py at GitHub.

https://github.com/40843245/Utility/blob/main/GUI/PySide/PyQt5/TableView/TableViewHandler/v1/Code/QTableViewHandler.py

## API
For details of API, see the comment of the .py file at shown above.
### class QTableWidgetItemHandler()
    def __list__(self)
    
    def SetItem(self,row,textList:list[str])
### class QTableWidgetSubHandler()

    def __init__(self)

    def ListRowsIndex(self,options)

    def ListColumnsIndex(self,options)

    def UpdateVerticalHeaderLabels(self)

    def UpdateHorizontalHeaderLabels(self)
    
    def ResizeOuterBoxToHorizontalHeader(self)

    def ResizeOuterBoxToVerticalHeader(self)
    
    def SetMaxOuterBox(self,size:QSize)
### class QTableWidgetHandler(QTableWidgetSubHandler)

    def __init__(self)
    
    def InsertRows(self,items : list[QTableWidgetItemHandler] )

    def Clear(self)
### class CloneHandler()
    
    @staticmethod 
    def CloneAll(src:QTableWidget,dest:QTableWidget)
  
    @staticmethod 
    def CloneRows(src:QTableWidget,dest:QTableWidget,itemsIndex:list[int])
### class InsertionHandler()

    @staticmethod 
    def InsertRows(src:QTableWidget,dest:QTableWidget,itemsIndex:list[int])
### class RemovalHandler()

    @staticmethod 
    def RemoveRows(dest:QTableWidget,itemsIndex:list[int])
### class CellHandler()

    @staticmethod
    def SetCellWidget(
            src : QTableWidget,
            rowth : int,
            colth : int,
            rowCount : int,
            columnCount : int , 
            removeHeaderFlag : ( list[bool] | None ) = None
    )
### class SelectionHandler()
    @staticmethod
    def SelectAll(src:QTableWidgetHandler):

    @staticmethod
    def SelectRows(src:QTableWidget,itemsIndex):

    @staticmethod
    def DeselectAll(src:QTableWidgetHandler):

    @staticmethod
    def DeselectRows(src:QTableWidget,itemsIndex):
### class HiddenHandler()
#### class Part()
        @staticmethod
        def SetRowsDisplay(src:QTableWidget,itemsIndex,isHidden:bool)

        @staticmethod
        def SetColumnsWidth(src:QTableWidget,width : int,columnIndex:list[int])

#### class All()
        @staticmethod
        def SetRowsHeight(src:QTableWidgetHandler,height : int)

        @staticmethod
        def SetColumnsWidth(src:QTableWidget,width : int):
### class SpanHandler()
    @staticmethod
    def Span(src:QTableWidget , size : QSize , rowIndex : list[int] , columnIndex : list[int] )
    
## Release Notes
### 2023/10/07 17:14
Initial Notes.
