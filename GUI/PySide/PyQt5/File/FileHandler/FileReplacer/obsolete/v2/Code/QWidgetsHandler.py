import copy
import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QTextEdit,QPushButton , QFileDialog , QGroupBox, QCheckBox , QTableWidget,QTableView,QTableWidgetItem , QHeaderView,QAbstractItemView  , QMessageBox , QVBoxLayout , QHBoxLayout
from PyQt5.QtCore import QItemSelectionModel

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QRect, QObject , QModelIndex 
from PyQt5 import QtCore
from PyQt5 import Qt
from PyQt5 import QtGui
from PyQt5.QtGui import QMouseEvent
from PySide6 import Qt3DRender
# from PyQt2.QtCore import QItemSelectionModel
from PySide2 import QtCore

import PySide2
import PySide6
import PyQt5

from functools import partial

from Utility.Func.FuncChecker.FuncLooker import FuncLooker

from DirectoryHandler import DirectoryHandler
class FuncCaller:
    @staticmethod
    def CallFunc(
            enumClass
    ):
        return [e.value for e in enumClass]
    
class ObjectChecker:
    @staticmethod
    def EqualLen(
            self,
            obj,
            equalLen
    ):
        return ( obj.len == equalLen )
    @staticmethod
    def IsInstances(
            obj,
            instances : (list,tuple) 
    ) -> bool:
        if len(instances) <= 0 :
            return False        
        for inst in instances:
            if  isinstance(obj, inst):
                return True
        return False
    
class QWidgetChecker:
    @staticmethod
    def Exist(
            obj  
    ) -> bool:
        return obj != None
    @staticmethod
    def IsQtWidget(
            obj
    ) -> bool:
        return isinstance(obj,QWidget)
    
class QWidgetHandler:
    @staticmethod
    def SetGeometry(
            obj,
            position
    ):  
        if QWidgetChecker.Exist(obj) == False:
            raise Exception("ERROR!!! Object does NOT exists.")
        if QWidgetChecker.IsQtWidget(obj) == False:
            raise Exception("ERROR!!! Object does NOT in these types.")        
        obj.setGeometry(position)
        return obj
    
    def Create(
            self
    ):
        self.mainWindow = QWidget()
        return self
        
    
class TextHandler:
    @staticmethod
    def SetText(
            obj  ,
            text : QLabel ,
            alignmentMode : PyQt5.QtCore.Qt.AlignmentFlag | PyQt5.QtCore.Qt.Alignment
    ):
      if QWidgetChecker.Exist(obj) == False:
          raise Exception("ERROR!!! Object does NOT exists.")
      availableInstances = ( QLabel , QLineEdit , QTextEdit,QPushButton , QCheckBox)
      if ObjectChecker.IsInstances(obj, availableInstances ) == False:
          raise Exception("ERROR!!! Object does NOT in these types.")
      if text != None:
          obj.setText(text)
      if alignmentMode != None:
          obj.setAlignment(alignmentMode)
      return obj
    
class QApplicationHandler(QWidgetHandler):   
    def __init__(self):
        super().__init__()
    def Clear(self):
        if QApplication.instance():
            QApplication.instance().exit()
    def CreateWindow(
            self,
            title
    ):
        self.Clear()
        self.app = QApplication(sys.argv)
        self.mainWindow = QMainWindow()
        self.mainWindow.setWindowTitle(title)
        return self
    def Show(
            self
    ):
        if QWidgetChecker.Exist(self.mainWindow) == False:
            raise Exception("ERROR!!! Object does NOT exists.")
        self.mainWindow.show()
    def SysExit(
            self
    ):
        if QWidgetChecker.Exist(self.app) == False:
            raise Exception("ERROR!!! Object does NOT exists.")
        sys.exit(self.app.exec_())
        
    def Close(
            self
    ):
        if QWidgetChecker.Exist(self.mainWindow) == False:
            raise Exception("ERROR!!! Object does NOT exists.")
        self.mainWindow.close()
        
class QLabelHandler():
    def Create(
            self
    ):
        self.label = QLabel()
        return self
    
    def AddWidget(
            self,
            layout
    ):
        layout.addWidget(self.label)
        return ( self , layout )

class QLineEditHandler():
    def Create(
            self
    ):
        self.label = QLineEdit()
        return self
    def AddWidget(
            self,
            layout
    ):
        layout.addWidget(self.label)
        return ( self , layout )

class QTextEditHandler():
    def Create(
            self
    ):
        self.textEdit = QTextEdit()
        return self
    def AddWidget(
            self,
            layout
    ):
        layout.addWidget(self.textEdit)
        return ( self , layout )

class QTableViewHandler():
    def Create(
            self,
            title,
            mainWindow 
    ):
        self.tableView = QTableView()
        return self
    
    def AddWidget(
            self,
            layout
    ):
        layout.addWidget(self.tableView)
        return ( self , layout )
    
class QTableWidgetHandler():
    def Create(
            self,
            row : int,
            col : int,
    ):      
        self.tableView = QTableWidget(row,col)
        return self  
    
    def AddWidget(
            self,
            layout
    ):
        layout.addWidget(self.tableView)
        return ( self , layout )
    
class QTableWidgetItemHandler():
    def Create(
            self,
            args
    ):
        self.item  = QTableWidgetItem(args)
        return self
    
class QModelIndexHandler():
    def Create(
            self
    ):
        self.modelIndex = QModelIndex()
        return self
    
class QCheckboxHandler():
    def Create(
            self
    ):
        self.checkbox = QCheckBox()
        return self
    
    def AddWidget(
            self,
            layout
    ):
        layout.addWidget(self.checkbox)
        return ( self , layout )
    
class QPushButtonHandler():
    def Create(
            self
    ):
        self.pushButton = QPushButton()
        return self
    
    def AddWidget(
            self,
            layout
    ):
        layout.addWidget(self.pushButton)
        return ( self , layout )
    
    def ConnectClicked(
            self,
            title,
            mainWindow
    ):
        if QWidgetChecker.Exist(mainWindow) == False:
            raise Exception("ERROR!!! Object does NOT exists.")
        self.fileDialogHandler = QFileDialogHandler()
        self.pushButton.clicked.connect(
                                        partial(
                                                self.fileDialogHandler.Create,
                                                mainWindow,
                                                "Excel File",
                                                "C:\\",
                                                "Excel (*.xlsx)" ,
                                                1 
                                            ) 
                                        )
        return self
    
class QMessageBoxHandler():
    @staticmethod
    def Create(
            icon,
            text,
            informativeText,
            windowTitle
    ):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText(text)
        msg.setInformativeText(informativeText)
        msg.setWindowTitle(windowTitle)
        msg.exec()
        
class QGroupBoxHandler():
    def Create(
            self
    ):
        self.groupbox = QGroupBox()
        return self
    
    def AddWidget(
            self,
            layout
    ):
        layout.addWidget(self.groupbox)
        
    
class QHBoxLayoutHandler():
    def Create(
            self
    ):
        self.groupbox = QHBoxLayout()
        return self
        
class QVBoxLayoutHandler():
    def Create(
            self
    ):
        self.layout = QVBoxLayout()
        
    
class KeywordBox:
    def Create(
            self,
            title : str,
            placeholderText : str , 
            mainWindowPos: QRect , 
            layout : ( QVBoxLayout, QHBoxLayout )
    ):
        self.layout = layout  
        
        self.labelHandler = QLabelHandler()
        self.textEditHandler = QTextEditHandler()
        
        self.labelHandler = self.labelHandler.Create()
        self.textEditHandler = self.textEditHandler.Create()
        
        ( self.labelHandler, layout ) = self.labelHandler.AddWidget( layout )
        
        self.labelHandler.label = QWidgetHandler.SetGeometry( self.labelHandler.label , QRect(0,0,100,20) )
        self.labelHandler.label = TextHandler.SetText( 
                                                        self.labelHandler.label , title + ':' , 
                                                        PyQt5.QtCore.Qt.AlignRight
                                                      )
        
        ( self.textEditHandler , layout ) = self.textEditHandler.AddWidget( layout )
        self.textEditHandler.textEdit = QWidgetHandler.SetGeometry( self.textEditHandler.textEdit , QRect(100 + 20 , 0 ,200 ,30) )
        self.textEditHandler.textEdit = TextHandler.SetText( self.textEditHandler.textEdit , '' , PyQt5.QtCore.Qt.AlignRight)
        self.textEditHandler.textEdit.setReadOnly(False)
        self.textEditHandler.textEdit.setPlaceholderText(placeholderText)
        
        return self
    
    def AddCheckbox(
            self,
            layout
    ):
        self.checkboxHandler = QCheckboxHandler()
        self.checkboxHandler = self.checkboxHandler.Create()
        ( self.checkboxHandler , layout ) = self.checkboxHandler.AddWidget( layout )
        return ( self , layout )
    
    def AddButton(
            self,
            layout
    ):
        self.pushButtonHandler = QPushButtonHandler()
        self.pushButtonHandler = self.pushButtonHandler.Create()
        ( self.pushButtonHandler , layout ) = self.pushButtonHandler.AddWidget( layout )
        return ( self , layout )
    
    def AddStateChangeEvent(
            self
    ):
        if (self.checkboxHandler != None and self.checkboxHandler.checkbox != None) == False:
            return None
        self.checkboxHandler.checkbox.clicked.connect(self.StateChange)
    
    def StateChange(
            self
    ):
          shouldReadOnly = self.checkboxHandler.checkbox.isChecked()
          self.textEditHandler.textEdit.setReadOnly(shouldReadOnly)
          return self
                
class QFileDialogHandler:
    @staticmethod
    def CreateStatic(
            mainWindow ,
            title : str , 
            currentDirectory : str , 
            fileFilter : str ,
            saveGetMode : int
    ):
        if QWidgetChecker.Exist(mainWindow) == False:
            raise Exception("ERROR!!! Object does NOT exists.")
        match saveGetMode:
            case 1:
                fileDialog = QFileDialog.getOpenFileName(
                                                        parent = mainWindow ,
                                                        caption = "Open " + title , 
                                                        directory = currentDirectory , 
                                                        initialFilter = fileFilter
                                                    )
            case 2:
                fileDialog = QFileDialog.getOpenFileName(
                                                        parent = mainWindow ,
                                                        caption = "Save " + title , 
                                                        directory = currentDirectory , 
                                                        initialFilter = fileFilter
                                        )
            case 3:
                fileDialog = QFileDialog.getExistingDirectory(
                                                                parent = mainWindow ,
                                                                caption = "Open " + title , 
                                                                directory = currentDirectory , 
                                                                options = QFileDialog.ShowDirsOnly | QFileDialog.ShowDirsOnly
                    )
        return fileDialog
    
    def Set( 
            self,
            mainWindow : QMainWindow,
            title : str , 
            currentDirectory : str , 
            fileFilter : str ,
            saveGetMode : int
    ):
        self.mainWindow = mainWindow
        self.title = title
        self.currentDirectory = currentDirectory
        self.fileFilter = fileFilter
        self.saveGetMode = saveGetMode
        
    # Non-static method
    def Open(
              self,
      ):
          self.files = QFileDialogHandler.CreateStatic(
                                                          mainWindow = self.mainWindow,
                                                          title = self.title, 
                                                          currentDirectory = self.currentDirectory , 
                                                          fileFilter = self.fileFilter,
                                                          saveGetMode = self.saveGetMode
                                                     )
          return self.files
class DocumentHandler:
    def Create(
            self ,
            groupbox
    ):
        if QWidgetChecker.Exist(groupbox) == False:
            raise Exception("ERROR!!! Object does NOT exists.")
        self.groupbox = groupbox
    def SearchReplace(
            self
    ):
        pass
    
    def Search(
            self
    ):
        pass
    def Replace(
            self
    ):
        pass

class FileTableViewer(
        ):
    
    def Create(
            self,
            row : int,
            column : int ,
            pos : QRect ,
            tableWH : QTableWidgetHandler,
            layout : ( QVBoxLayout , QHBoxLayout )
    ):
        if row <= 0 or column <= 0 :
            raise Exception("ERROR!!! Invalid args in FileTableViewer class.")
      
        self.layout = layout
        
        tableWH = tableWH.Create( row = row, col = column)
        ( tableWH , layout ) = tableWH.AddWidget(self.layout)
        
        tableWH.tableView = QWidgetHandler.SetGeometry(obj = tableWH.tableView , position = pos )
                
        tableWH.tableView.setSelectionBehavior(QTableView.SelectRows)
        
        tableWH.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tableWH.tableView.setColumnWidth(column,pos.width()//column)
        
        tableWidgetItemHandlerList = []
        tableWidgetItemHandlerSublist = []
        for ro in range(0,row,1):     
            tableWidgetItemHandlerSublist = []
            for co in range(0,column,1):
               tableWidgetHandler_temp = QTableWidgetItemHandler()
               tableWidgetHandler_temp = tableWidgetHandler_temp.Create(args = "ro="+str(ro)+",co="+str(co))
               tableWidgetHandler_temp.item.setText(str(ro)+" "+str(co))
               tableWidgetHandler_temp.item.setBackground(QtGui.QColor(255,255,255))
               tableWidgetItemHandlerSublist.append(tableWidgetHandler_temp)
            tableWidgetItemHandlerList.append(tableWidgetItemHandlerSublist)
               
        for ro in range(0,row,1):
            for co in range(0,column,1):
                tableWidgetItemHandlerList[ro][co].item.setFlags(
                    PyQt5.QtCore.Qt.ItemIsUserCheckable |
                    PyQt5.QtCore.Qt.ItemIsSelectable |
                    PyQt5.QtCore.Qt.ItemIsEnabled
                )
                tableWH.tableView.setItem(
                    ro,
                    co,
                    tableWidgetItemHandlerList[ro][co].item
                )
                
        tableWH.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        tableWH.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        tableWH.tableView.clicked.connect( 
                partial( SelectBackground_All , tableWH.tableView ) 
            )
        
        resultList = list()
        for ro in range(0,row,1):
            tempList = list()
            for co in range(0,column,1):
                ite = tableWH.tableView.item(
                    ro,
                    co
                )
                tempTuple = (int(ite.flags() ) , )
                tempList.append ( 
                    tempTuple
            )
            resultList.append( tempList )
        return tableWH

def SelectBackground_All(
        tableView
    ):
        currentRow = copy.deepcopy( tableView.currentRow() )
        currentWidget = SelectBackground_AllRow(currentRow , tableView)
        tableWH.tableView = currentWidget
        
def SelectBackground_AllRow(
        currentRow : int , 
        tableView 
    ):
        for co in range(0,tableView.columnCount(),1): 
            tableView = SelectBackground(currentRow,co,tableView)
                   
        for co in range(0,tableView.columnCount(),1): 
            tableView.item(currentRow,co).setFlags(
                    PyQt5.QtCore.Qt.ItemIsUserCheckable |
                    PyQt5.QtCore.Qt.ItemIsSelectable |
                    PyQt5.QtCore.Qt.ItemIsEnabled
                )
                
        return tableView
            
def SelectBackground(
        currentRow : int,
        currentColumn : int,
        tableView
    ):
    currentItem = tableView.item(currentRow,currentColumn)
    currentBackgroundColor = currentItem.background()  
    nextBackgroundColor = QtGui.QColor(255,255,255)  if currentBackgroundColor != QtGui.QColor(255,255,255) else QtGui.QColor(0,100,100)

    tableView.item(currentRow,currentColumn).setBackground(  nextBackgroundColor )
    
    return tableView
    
## Try to deselect the nth QTableView when clicking the QMainWindow just after clicking the nth QTableView.

def Deselect(table):
    for ro in range(0,row,1):
        for co in range(0,column,1):
            item1 = table.item(ro,co)
            item1.setBackground(QtGui.QColor(255,255,255))

def DeselectAll(widgets):
    for elem in widgets:
        Deselect(elem)    

def ContainItem(table1,table2,selectedItem1List) -> bool :
    for ro1 in range(0,table1.rowCount(),1):
        if not ro1 in selectedItem1List:
            continue
        for ro2 in range(0,table2.rowCount(),1):
            flag = True
            for co1 in range(0,table1.columnCount(),1):
                item1 = table1.item(ro1,co1)
                item2 = table2.item(ro2,co1)
                if item1.text() != item2.text() :
                    flag = False
                    break
            if flag == True:
                return True
    return False

def MoveToRight(dummy1,table1,table2,dummy2):
    selectedItemList = [ 
        [ (ro,co,table1.item(ro,co)) for ro in range(0,table1.rowCount(),1) if table1.item(ro,co).background()!=Qt.QColor(255,255,255)] for co in range(0,table1.columnCount(),1) 
    ]

    x = [
        selectedItemList[0][co] for co in range(0,len(selectedItemList[0]),1)
    ]

    selectedItem1IndexList = [ elem[0] for elem in x ]
    
    if len(selectedItem1IndexList) <= 0 :
        QMessageBoxHandler.Create(QMessageBox.Critical,"Error",'Operation Failed.\nIt is NOT allowed to not select data.',"Error")
        return 
    if ContainItem(table1, table2, selectedItem1IndexList) == True:
        QMessageBoxHandler.Create(QMessageBox.Critical,"Error",'Operation Failed.\nIt is NOT allowed to add duplicated data.\nIt is NOT allowed that \n at least 1 row in table2 contains same text for each items for any row in table1. ',"Error")
        return 
    
    for i in range(0,len(selectedItemList),1):
        if len(selectedItemList[0]) <= 0 :
            continue
        elem = selectedItemList[0][i]
        currentRow = elem[0]
        table2.insertRow(table2.rowCount())
        for co in range(0,table2.columnCount(),1):            
            y = QTableWidgetItem(table1.item(currentRow,co))
            table2.setItem(table2.rowCount()-1,co,y)
            
def MoveToRightAll(dummy1,table1,table2,dummy2):
    item1List = [i for i in range(0,table1.rowCount(),1)]
    
    if ContainItem(table1, table2, item1List) == True:
        QMessageBoxHandler.Create(QMessageBox.Critical,"Error",'Operation Failed.\nIt is NOT allowed to add duplicated data.\nIt is NOT allowed that \n at least 1 row in table2 contains same text for each items for any row in table1. ',"Error")
        return 
    
    for ro in range(0,table1.rowCount(),1):
        table2.insertRow(table2.rowCount())
        for co in range(0,table2.columnCount(),1):            
            y = QTableWidgetItem(table1.item(ro,co))
            table2.setItem(table2.rowCount()-1,co,y)
    
def RemoveRows(table2,removeIndexList):
    removeIndexList = reversed(removeIndexList)
    for elem in removeIndexList:
        table2.removeRow(elem)
    
def Remove(dummy1,table1,table2,dummy2):
    selectedItemList = [ 
        [ (ro,co,table2.item(ro,co)) for ro in range(0,table2.rowCount(),1) if table2.item(ro,co).background()!=Qt.QColor(255,255,255)] for co in range(0,table2.columnCount(),1) 
    ]

    x = [
        selectedItemList[0][co] for co in range(0,len(selectedItemList[0]),1)
    ]

    selectedItem2IndexList = [ elem[0] for elem in x ]
    if len(selectedItem2IndexList) <= 0:
        QMessageBoxHandler.Create(QMessageBox.Critical,"Error",'Operation Failed.\nIt is NOT allowed to not select data',"Error")    
        return
    RemoveRows(table2, selectedItem2IndexList)
def RemoveAll(dummy1,table1,table2,dummy2):
    selectedItem2IndexList = [i for i in range(0,table2.rowCount(),1)]
    if len(selectedItem2IndexList) <= 0:
        QMessageBoxHandler.Create(QMessageBox.Critical,"Error",'Operation Failed.\nIt is NOT allowed to remove empty items in table2.',"Error")    
        return
    RemoveRows(table2, selectedItem2IndexList)
        
def GetInfo(obj) : return [obj,type(obj)]

if __name__ == '__main__':
    
    """
    row = 12
    column = 2
    """
    rectMainWindow = QRect(0,0,1000,1000)
 
    """
    fileTableViewer1Pos = QRect(0,200,400,400) 
    fileTableViewer2Pos = QRect(600,200,400,400)
    
    
    pushButtonHandler = QPushButtonHandler()
    searchKeywordBox = KeywordBox()
    replaceKeywordBox = KeywordBox()   
    pathKeywordBox = KeywordBox()
    
    
    fileDialogHandler = QFileDialogHandler()
        
    rightArrowPushButtonHandler = QPushButtonHandler()
    leftArrowPushButtonHandler = QPushButtonHandler()
    rightDoubleArrowPushButtonHandler = QPushButtonHandler()
    leftDoubleArrowPushButtonHandler = QPushButtonHandler()
    """
    
    inst =  QApplicationHandler()

    # widget = QWidget()
    
    inst = inst.CreateWindow('title')
    
    inst.mainWindow = QWidgetHandler.SetGeometry( inst.mainWindow ,rectMainWindow )
    
    # inst.mainWindow.setCentralWidget( widget )
    
    """
    mainLayout = QVBoxLayout(inst.mainWindow)    
    
    searchKeywordBox = searchKeywordBox.Create('Search' ,'Search',QRect(0,0,1000//2,35) , mainLayout )

    replaceKeywordBox = replaceKeywordBox.Create('Replace' ,'Replace',QRect(0,35,1000//2,35) , mainLayout )
    
    ( replaceKeywordBox , mainLayout ) = replaceKeywordBox.AddCheckbox( mainLayout )
    
    replaceKeywordBox.checkboxHandler.checkbox = QWidgetHandler.SetGeometry( replaceKeywordBox.checkboxHandler.checkbox, QRect(500-100,35,100,30) )
    replaceKeywordBox.checkboxHandler.checkbox = TextHandler.SetText(replaceKeywordBox.checkboxHandler.checkbox, 'Replace', None)
    replaceKeywordBox.AddStateChangeEvent()
    
    fileDialogHandler.Set(inst.mainWindow, 'Path', 'C:\\', '', 3)
    
    pathKeywordBox = pathKeywordBox.Create('Path' ,'Path',QRect(0,70,1000//2,35) , mainLayout)
    
    ( pathKeywordBox , mainLayout ) = pathKeywordBox.AddButton( mainLayout )
    
    pathKeywordBox.textEditHandler.textEdit.setReadOnly(True)

    pathKeywordBox.pushButtonHandler.pushButton =  QWidgetHandler.SetGeometry( pathKeywordBox.pushButtonHandler.pushButton , QRect(500 - 100,70,100,35))
    pathKeywordBox.pushButtonHandler.pushButton =  TextHandler.SetText(pathKeywordBox.pushButtonHandler.pushButton , 'Find Path', None)
    pathKeywordBox.pushButtonHandler.pushButton.clicked.connect(
        fileDialogHandler.Open      
    )

    arrowHandlerList = [
        rightArrowPushButtonHandler,
        leftArrowPushButtonHandler,
        rightDoubleArrowPushButtonHandler,
        leftDoubleArrowPushButtonHandler
    ]
    arrowTextList = [
        ">",
        ">>",
        "Remove",
        "Remove All"
    ]
    
    arrowEventList = [
        MoveToRight,
        MoveToRightAll,
        Remove,
        RemoveAll
    ]
    
    fileTableViewerPosList = [fileTableViewer1Pos,fileTableViewer2Pos]
    fileTableViewerList = list()
    fileTableViewer = FileTableViewer()    
    tableWH = QTableWidgetHandler()
    
    for i in range(0,2,1):
       
        tableWH1 = tableWH      
        ftv = fileTableViewer    
        ftv = ftv.Create(
                row = row ,  
                column = column , 
                pos = fileTableViewerPosList[i] , 
                layout = mainLayout , 
                tableWH = tableWH1 
            )
        
        ftv.tableView.setObjectName("fileTableViewer"+str(i)) ## Set name of object of QTableView    
        fileTableViewerList.append(ftv.tableView)
        
    allChildren = mainLayout.findChildren(QObject)
    currentTableView = mainLayout.findChild(QObject,"fileTableViewer"+str(i))
    allChildrenExceptQTableWidget = [
        elem for elem in allChildren if  isinstance(elem, QTableWidget)==False 
    ]
    
    allQTableWidget = [
        elem for elem in allChildren if isinstance(elem,QTableWidget) == True     
    ]
        
    ## Do it for all QtWidget object except QTableWidget object and it's inherited object.
    for elem in allChildrenExceptQTableWidget :
        ## Add a lambda func as callback event after mouse press of the elem
        elem.mousePressEvent = lambda event : (
            DeselectAll(allQTableWidget)  
        )        
           
    table1 = fileTableViewerList[0]
    table2 = fileTableViewerList[1]
    
    for i in range(0,len(arrowHandlerList),1):
        arrowHandlerList[i] = arrowHandlerList[i].Create()
        ( arrowHandlerList[i] , mainLayout ) = arrowHandlerList[i].AddWidget( mainLayout )
        arrowHandlerList[i].pushButton = QWidgetHandler.SetGeometry(obj = arrowHandlerList[i].pushButton, position = QRect(430,200 + (20 + 10 )*i,100,20))
        arrowHandlerList[i].pushButton = TextHandler.SetText(obj = arrowHandlerList[i].pushButton ,text = arrowTextList[i] , alignmentMode= None)
        arrowHandlerList[i].pushButton.clicked.connect(partial(arrowEventList[i], [] , table1,table2) )

    pushButtonHandler = pushButtonHandler.Create()
    ( pushButtonHandler , mainLayout ) = pushButtonHandler.AddWidget( mainLayout )
    pushButtonHandler.pushButton = QWidgetHandler.SetGeometry( pushButtonHandler.pushButton , QRect(0,100,100,20) )
    pushButtonHandler.pushButton = TextHandler.SetText( pushButtonHandler.pushButton , 'Search' , None)

    inst.mainWindow.mousePressEvent = lambda event : (
        print("Window Clicked")         
    )
    
    for i in range(0,len(arrowHandlerList),1):
        ( arrowHandlerList[i] , mainLayout ) =  arrowHandlerList[i].AddWidget( mainLayout )
    
    # mainLayout.setCentralWidget( )
    
    widget.setLayout( mainLayout )
    
    inst.mainWindow.setCentralWidget(widget)
    
    print ( mainLayout )
    print( mainLayout.parentWidget() )
    
    
    print( inst )
    print( inst.mainWindow )
    """
    
    inst.Show()
    inst.SysExit()
