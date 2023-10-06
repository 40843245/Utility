import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QWidget

from PySide6.QtWidgets import QHBoxLayout , QVBoxLayout , QLayout
from PySide6.QtWidgets import QListView, QListWidget , QListWidgetItem
from PySide6.QtWidgets import QAbstractItemView

from PySide6.QtCore import QRect
from PySide6.QtCore import Qt

"""
A class that clone items.
"""
class CloneHandler():
    """
    Clone all item from src to dest.
    """
    @staticmethod
    def Clone(src:QListWidget,dest:QListWidget):
        dest.clear()
        for ro in range(0,src.count(),1):
            dest.addItem(src.item(ro).clone())

"""
A class that inserts items.
"""    
class InsertionHandler():
    @staticmethod
    def InsertRows(src:QListWidget,dest:QListWidget,itemsIndex:list[int]):
        for ro in range(0,len(itemsIndex),1):
            rowIndex = itemsIndex[ro]
            if 0 <= rowIndex and rowIndex < src.count():
                item = src.item(rowIndex)
                dest.addItem(item.clone())
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
    def RemoveRows(dest:QListWidget,itemsIndex:list[int]):
        for ro in range(0,len(itemsIndex),1):
            rowIndex = itemsIndex[ro]
            print(rowIndex)
            if 0 <= rowIndex and rowIndex < dest.count():
                dest.takeItem(rowIndex)
                # Increase items[i].row by 1.
                # Since there are 1 more row after insertion.
                for i in range(0,len(itemsIndex),1):
                    itemsIndex[i] -= 1

"""
A class that selects items.
"""    
class SelectionHandler():
    """ 
    Select each item of src
    """
    @staticmethod
    def SelectAll(src:QListWidget):
        for ro in range(0,src.count(),1):
            src.item(ro).setSelected(True)
            
    """ 
    Select each item in itemsIndex of src
    """
    @staticmethod
    def SelectItems(src:QListWidget,itemsIndex):
        for ro in itemsIndex :
            if 0 <= ro and ro <src.count():
                src.item(ro).setSelected(True)
    
    """
    Deselect each item of src
    """
    @staticmethod
    def DeselectAll(src:QListWidget):
        for ro in range(0,src.count(),1):
            src.item(ro).setSelected(False)
    
    """ 
    Deselect each item itemsIndex in of src
    """
    @staticmethod
    def DeselectItems(src:QListWidget,itemsIndex):
        for ro in itemsIndex :
            if 0 <= ro and ro <src.count():
                src.item(ro).setSelected(False)
    

"""
A class that handles QListWidgetItem.
"""    
class QListWidgetItemHandler():
    def __init__(self):
        pass
    def __list__(self):
        return [self.row,self.text]
    def SetItem(self,row,text):
        self.row = row
        self.text = text

"""
A class that handles QListWidget.
"""          
class QListWidgetHandler():
    def __init__(self):
        self.listWidget = QListWidget()
    
    """
    Insert items with a list of QListWidgetItemHandler
    """
    def InsertItems(self,items : list[QListWidgetItemHandler] ):
        items = sorted(items,key = lambda l : l.row , reverse= False)        
        for ro in range(0,len(items),1):
            row = items[ro].row
            text = items[ro].text
            listWidgetItem = QListWidgetItem()
            listWidgetItem.setText(text)
            self.listWidget.insertItem(row,listWidgetItem)
            # Increase items[i].row by 1.
            # Since there are 1 more row after insertion.
            for i in range(0,len(items),1):
                items[i].row += 1
            del listWidgetItem
    
    """
    Clear the listWidget -- self.listWidget
    """
    def Clear(self):
        self.listWidget.clear()
    
"""
A main class about Widget .
"""  
class Widget(QWidget):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.Create()
        
    def Create(self):
        mainLayout = QHBoxLayout()
        listWidgetHandler = QListWidgetHandler()
        listWidgetHandler2 = QListWidgetHandler()
        
        listWidgetHandler.listWidget.setGeometry(QRect(0,0,100,100))
        listWidgetHandler2.listWidget.setGeometry(QRect(200,0,100,100))
        
        listWidgetHandler.listWidget.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        listWidgetHandler2.listWidget.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        
        listWidgetItemHandlerList = list()
        for i in range(0,10,1):
            listWidgetItemHandler = QListWidgetItemHandler()
            listWidgetItemHandler.SetItem(i, "i:"+str(i))
            listWidgetItemHandlerList.append(listWidgetItemHandler)
            del listWidgetItemHandler
        listWidgetHandler.InsertItems(listWidgetItemHandlerList)        
        
        listWidgetItemHandlerList = list()
        for i in [2,4,10,3,1]:
            listWidgetItemHandler = QListWidgetItemHandler()
            listWidgetItemHandler.SetItem(i, "j:"+str(i))
            listWidgetItemHandlerList.append(listWidgetItemHandler)
            del listWidgetItemHandler
        listWidgetHandler.InsertItems(listWidgetItemHandlerList)
        
        listWidgetItemHandlerList = list()
        for i in [1,2,3,4]:
            listWidgetItemHandler = QListWidgetItemHandler()
            listWidgetItemHandler.SetItem(i, "k:"+str(i))
            listWidgetItemHandlerList.append(listWidgetItemHandler)
            del listWidgetItemHandler
        listWidgetHandler2.InsertItems(listWidgetItemHandlerList)
        
        itemsIndex = [1,3,4]
        InsertionHandler.InsertRows(listWidgetHandler.listWidget, listWidgetHandler2.listWidget, itemsIndex)
        
        itemsIndex = [0,2]
        RemovalHandler.RemoveRows(listWidgetHandler2.listWidget, itemsIndex)
        
        mainLayout.addWidget(listWidgetHandler.listWidget)
        mainLayout.addWidget(listWidgetHandler2.listWidget)
        self.mainLayout = mainLayout
    
"""
Main entry
"""  
if __name__ == '__main__':
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    widget = Widget()
    widget.setLayout(widget.mainLayout)
    widget.show()
    sys.exit(app.exec())
    
