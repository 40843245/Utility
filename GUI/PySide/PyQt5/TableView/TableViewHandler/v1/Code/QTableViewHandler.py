import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QWidget

from PySide6.QtWidgets import QHBoxLayout , QVBoxLayout , QBoxLayout , QLayout 
from PySide6.QtWidgets import QTableView, QTableWidget, QTableWidgetItem
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QAbstractItemView
from PySide6.QtWidgets import QHeaderView
from PySide6.QtWidgets import QSizePolicy

from PySide6.QtCore import QRect
from PySide6.QtCore import QSize
from PySide6.QtCore import Qt

# My own module
from ObjectHandler import ObjectHandler 

"""
A class that handles QTableWidgetItem.
"""    
class QTableWidgetItemHandler():
    def __init__(self):
        pass
    def __list__(self):
        return [self.row,self.textList]    
    def SetItem(self,row,textList:list[str]):
        self.row = row
        self.textList = textList
"""
A subclass that handles QTableWidget.
"""  
class QTableWidgetSubHandler():
    def __init__(self):
        self.tableWidget = QTableWidget()
    def ListRowsIndex(self,options):
        rowCount = self.tableWidget.rowCount()
        return [options(elem)  for elem in range(0,rowCount,1)]
    def ListColumnsIndex(self,options):
        columnCount = self.tableWidget.columnCount()
        return [ options(elem) for elem in range(0,columnCount,1)]
    def Update(self):
        self.UpdateHeaderLabels()
        self.ResizeColumsnWidthToContent()
    def UpdateHeaderLabels(self):
        self.UpdateVerticalHeaderLabels()
        self.UpdateHorizontalHeaderLabels()
        
    def UpdateVerticalHeaderLabels(self):
        self.tableWidget.setVerticalHeaderLabels( self.ListRowsIndex(lambda x : str(x) ) )
    def UpdateHorizontalHeaderLabels(self):
        self.tableWidget.setHorizontalHeaderLabels(self.ListColumnsIndex(lambda x:str(x)))
    
    #
    def ResizeOuterBoxToHorizontalHeader(self):
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    #
    def ResizeOuterBoxToVerticalHeader(self):
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
    def SetMaxOuterBox(self,size:QSize):
        self.tableWidget.setMaximumSize(size)
        self.ResizeOuterBoxToHorizontalHeader()
        self.ResizeOuterBoxToVerticalHeader()
        
"""
A class that handles QTableWidget.
"""          
class QTableWidgetHandler(QTableWidgetSubHandler):
    def __init__(self):
        super().__init__()
    
    """
    Insert items with a list of QTableWidgetItemHandler
    """
    def InsertRows(self,items : list[QTableWidgetItemHandler] ):
        items = sorted(items,key = lambda l : l.row , reverse= False)        
        for ro in range(0,len(items),1):
            row = items[ro].row
            textList = items[ro].textList
            self.tableWidget.insertRow(row)
            for co in range(0,self.tableWidget.columnCount(),1):
                tableWidgetItem = QTableWidgetItem()
                text = textList[co]
                tableWidgetItem.setText(text)
                self.tableWidget.setItem(ro,co,tableWidgetItem)
                del tableWidgetItem
            # Increase items[i].row by 1.
            # Since there are 1 more row after insertion.
            for i in range(0,len(items),1):
                items[i].row += 1
    """
    Clear the listWidget -- self.listWidget
    """
    def Clear(self):
        self.tableWidget.clear()

"""
A class that clone items.
"""
class CloneHandler():
    """
    Clone all item from src to dest.
    """
    @staticmethod
    def CloneAll(src:QTableWidget,dest:QTableWidget):
        dest.clear()
        dest.setRowCount(src.rowCount())
        dest.setColumnCount(src.columnCount())
        for ro in range(0,src.rowCount(),1):
            for co in range(src.columnCount(),1):
               tableWidgetIem = src.item(ro,co).clone()
               dest.setItem(ro,co,tableWidgetIem)        
    
    """
    Clone specific item from src to dest with given row index (named itemsIndex).
    """
    @staticmethod
    def CloneRows(src:QTableWidget,dest:QTableWidget,itemsIndex:list[int]):
        if len(itemsIndex) <= 0 :
            raise Exception("Invalid given list, it must be neither None nor empty.")
        dest.clear()
        dest.setRowCount(len(itemsIndex))
        dest.setColumnCount(src.columnCount())
        for ro in range(0,src.len(itemsIndex),1):
            if 0 <= ro and ro < src.rowCount() :
                for co in range(src.len(itemsIndex),1):
                    tableWidgetIem = src.item(ro,co).clone()
                    dest.setItem(ro,co,tableWidgetIem)

"""
A class that inserts items.
"""    
class InsertionHandler():
    @staticmethod
    def InsertRows(src:QTableWidget,dest:QTableWidget,itemsIndex:list[int]):
        for ro in range(0,len(itemsIndex),1):
            rowIndex = itemsIndex[ro]
            dest.insertRow(ro)
            if 0 <= rowIndex and rowIndex < src.rowCount():
                for co in range(0,src.columnCount(),1):
                    item = src.item(rowIndex,co).clone()
                    dest.setItem(rowIndex,co,item)
                # Increase items[i].row by 1.
                # Since there are 1 more row after insertion.
                for i in range(0,len(itemsIndex),1):
                    itemsIndex[i] += 1

"""
A class that removes items.
"""            
class RemovalHandler():
    """
    Remove items by row with given itemsIndex.
    """
    @staticmethod
    def RemoveRows(dest:QTableWidget,itemsIndex:list[int]):
        for ro in range(0,len(itemsIndex),1):
            rowIndex = itemsIndex[ro]
            if 0 <= rowIndex and rowIndex < dest.rowCount():
                for co in range(0,dest.columnCount(),1):
                    dest.takeItem(rowIndex,co)
                # Increase items[i].row by 1.
                # Since there are 1 more row after insertion.
                for i in range(0,len(itemsIndex),1):
                    itemsIndex[i] -= 1

"""
A class that handles a cell in QTableWidget object.
"""   
class CellHandler():
    """
    Set the cell as a QWidget object.
    """   
    @staticmethod
    def SetCellWidget(
            src : QTableWidget,
            rowth : int,
            colth : int,
            rowCount : int,
            columnCount : int , 
            removeHeaderFlag : ( list[bool] | None ) = None
    ):
        subTableWidgetHandler = QTableWidgetHandler()
        subTableWidgetHandler.tableWidget.setRowCount(rowCount)
        subTableWidgetHandler.tableWidget.setColumnCount(columnCount)
        subTableWidgetHandler.SetMaxOuterBox(QSize(300,40))
        
        removeHeaderFlag2 = ObjectHandler.Filler.Fill(removeHeaderFlag,"list",2,True)
        print("removeHeaderFlag2:")
        print(removeHeaderFlag2)
        
        if removeHeaderFlag2[0] == True:
            subTableWidgetHandler.tableWidget.verticalHeader().hide()
        if removeHeaderFlag2[1] == True:
            subTableWidgetHandler.tableWidget.horizontalHeader().hide()
        src.setCellWidget(rowth,colth,subTableWidgetHandler.tableWidget)
        
"""
A class that selects items.
"""    
class SelectionHandler():
    """ 
    Select each item of src
    """
    @staticmethod
    def SelectAll(src:QTableWidgetHandler):
        rowsIndex = src.ListRowsIndex(lambda x : x)
        SelectionHandler.SelectRows(src.tableWidget, rowsIndex)
            
    """ 
    Select each item in itemsIndex of src
    """
    @staticmethod
    def SelectRows(src:QTableWidget,itemsIndex):
        for ro in itemsIndex :
            if 0 <= ro and ro <src.rowCount():
                for co in range(0,src.columnCount(),1):
                    if src.item(ro,co) != None:
                        src.item(ro,co).setSelected(True)
    
    """
    Deselect each item of src
    """
    @staticmethod
    def DeselectAll(src:QTableWidgetHandler):
        rowsIndex = src.ListRowsIndex(lambda x : x)
        SelectionHandler.DeselectRows(src.tableWidget, rowsIndex)
        
        
    """ 
    Deselect each item itemsIndex in of src
    """
    @staticmethod
    def DeselectRows(src:QTableWidget,itemsIndex):
        for ro in itemsIndex :
            if 0 <= ro and ro <src.rowCount():
                for co in range(0,src.columnCount(),1):
                    if src.item(ro,co) != None:
                        src.item(ro,co).setSelected(False)

class HiddenHandler():
    class Part():
        @staticmethod
        def SetRowsDisplay(src:QTableWidget,itemsIndex,isHidden:bool):
            for ro in itemsIndex :
                if 0 <= ro and ro <src.rowCount():
                    src.setRowHidden(ro,isHidden)
        #
        @staticmethod
        def SetColumnsDisplay(src:QTableWidget,itemsIndex,isHidden:bool):
            for co in itemsIndex :
                if 0 <= co and co <src.columnCount():
                    src.setColumnHidden(co,isHidden)    
class SizeHandler():
    class Part():
        @staticmethod
        def SetRowsHeight(src:QTableWidget,height : int,rowIndex:list[int]):
            for ro in rowIndex :
                if 0 <= ro and ro < src.rowCount():
                    src.setRowHeight(ro, height)
                    
        @staticmethod
        def SetColumnsWidth(src:QTableWidget,width : int,columnIndex:list[int]):
            for co in columnIndex :
                if 0 <= co and co < src.columnCount():
                    src.setColumnWidth(co, width)
    class All():
        @staticmethod
        def SetRowsHeight(src:QTableWidgetHandler,height : int):
            rowsIndex = src.ListRowsIndex(lambda x : x)
            SizeHandler.Part.SetRowsHeight(src.tableWidget, height, rowsIndex)
                    
        @staticmethod
        def SetColumnsWidth(src:QTableWidget,width : int):
            columnsIndex = src.ListColumnsIndex(lambda x : x)
            SizeHandler.Part.SetColumnsWidth(src.tableWidget, width, columnsIndex)
                
                    
class SpanHandler():
    @staticmethod
    def Span(src:QTableWidget , size : QSize , rowIndex : list[int] , columnIndex : list[int] ):
        for ro in rowIndex :
            for co in columnIndex:
                src.setSpan(ro, co, size.width(), size.height())
        
"""
A main class about Widget .
"""  
class Widget(QWidget):
    ROWCOUNT = 1
    COLCOUNT = 2
    def __init__(self,parent = None):
        super().__init__(parent)
        self.Create()
        
    def Create(self):
        tableLayout = QHBoxLayout()
        mainLayout = QVBoxLayout()
        pushButtonLayout = QHBoxLayout()
                
        tableLayout.setSizeConstraint(QLayout.SetMinimumSize)
        
        tableWidgetHandler = QTableWidgetHandler()
        tableWidgetHandler2 = QTableWidgetHandler()
    
        tableWidgetHandler.tableWidget.setRowCount(Widget.ROWCOUNT)
        tableWidgetHandler.tableWidget.setColumnCount(Widget.COLCOUNT)        
        
        tableWidgetHandler2.tableWidget.setRowCount(Widget.ROWCOUNT)
        tableWidgetHandler2.tableWidget.setColumnCount(Widget.COLCOUNT)
        
        tableWidgetHandler.tableWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        tableWidgetHandler2.tableWidget.setSelectionMode(QAbstractItemView.MultiSelection)        
        
        tableWidgetHandler.SetMaxOuterBox(QSize(500,100))
        tableWidgetHandler2.SetMaxOuterBox(QSize(500,100))

        tableWidgetItemHandlerList = list()
        for i in range(0,10,1):
            tableWidgetItemHandler = QTableWidgetItemHandler()
            tableWidgetItemHandler.SetItem(i, ["i1:"+str(i),"i2:"+str(i)] )
            tableWidgetItemHandlerList.append(tableWidgetItemHandler)
            del tableWidgetItemHandler
        tableWidgetHandler.InsertRows(tableWidgetItemHandlerList)        
        
        tableWidgetItemHandlerList = list()
        for i in [2,4,10,3,1]:
            tableWidgetItemHandler = QTableWidgetItemHandler()
            tableWidgetItemHandler.SetItem(i, ["j1:"+str(i),"j2:"+str(i)]  )
            tableWidgetItemHandlerList.append(tableWidgetItemHandler)
            del tableWidgetItemHandler
        tableWidgetHandler.InsertRows(tableWidgetItemHandlerList)
        
        tableWidgetItemHandlerList = list()
        for i in [1,2,3,4]:
            tableWidgetItemHandler = QTableWidgetItemHandler()
            tableWidgetItemHandler.SetItem(i, ["k1:"+str(i),"2:"+str(i)] )
            tableWidgetItemHandlerList.append(tableWidgetItemHandler)
            del tableWidgetItemHandler
        tableWidgetHandler2.InsertRows(tableWidgetItemHandlerList)

        SizeHandler.All.SetColumnsWidth(tableWidgetHandler2, 20)

        tableWidgetHandler.tableWidget.resizeColumnsToContents()
        tableWidgetHandler2.tableWidget.resizeColumnsToContents()
        
        tableWidgetHandler.tableWidget.adjustSize()
        tableWidgetHandler2.tableWidget.adjustSize()
        
        tableLayout.addWidget(tableWidgetHandler.tableWidget,1)
        tableLayout.addWidget(tableWidgetHandler2.tableWidget,1)
        
        pushButton = QPushButton()
        pushButton.setText("Hello")
        
        pushButton.clicked.connect(lambda : Func1() )
        
        pushButtonLayout.addWidget(pushButton,1)
        
        mainLayout.addLayout(tableLayout)
        mainLayout.addLayout(pushButtonLayout)
                
        mainLayout.setAlignment(tableLayout,Qt.AlignLeft)
        
        self.mainLayout = mainLayout
        
        def Func1():
            print("Func1")
            tableWidgetHandler.SetMaxOuterBox(QSize(600,100))
            tableWidgetHandler2.SetMaxOuterBox(QSize(600,100))
            CellHandler.SetCellWidget(tableWidgetHandler.tableWidget,0,0,3,3)

"""
Main entry
"""  
if __name__ == '__main__':
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    widget = Widget()
    widget.setLayout(widget.mainLayout)
    widget.setGeometry(QRect(0,0,1000,0))    
    widget.show()
    sys.exit(app.exec())
