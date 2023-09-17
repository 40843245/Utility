import copy
import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QTextEdit,QPushButton , QFileDialog , QGroupBox, QCheckBox , QTableWidget,QTableView,QTableWidgetItem , QHeaderView,QAbstractItemView

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QRect, QObject , QModelIndex 
from PyQt5 import QtCore
from PyQt5 import Qt
from PyQt5 import QtGui
from PyQt5.QtGui import QMouseEvent
from PySide6 import Qt3DRender


from functools import partial

from Utility.Func.FuncChecker.FuncLooker import FuncLooker

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
        return bool(obj)
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
    
class TextHandler:
    @staticmethod
    def SetText(
            obj,
            text,
            alignmentMode
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
            self,
            title,
            mainWindow
    ):
        if QWidgetChecker.Exist(mainWindow) == False:
            raise Exception("ERROR!!! Object does NOT exists.")
        self.label = QLabel(mainWindow)
        return self

class QLineEditHandler():
    def Create(
            self,
            title,
            mainWindow 
    ):
        if QWidgetChecker.Exist(mainWindow) == False:
            raise Exception("ERROR!!! Object does NOT exists.")
        self.label = QLineEdit(mainWindow)
        return self

class QTextEditHandler():
    def Create(
            self,
            title,
            mainWindow 
    ):
        if QWidgetChecker.Exist(mainWindow) == False:
            raise Exception("ERROR!!! Object does NOT exists.")
        self.textEdit = QTextEdit(mainWindow)
        return self

class QTableViewHandler():
    def Create(
            self,
            title,
            mainWindow 
    ):
        if QWidgetChecker.Exist(mainWindow) == False:
            raise Exception("ERROR!!! Object does NOT exists.")
        self.tableView = QTableView(mainWindow)
        return self
class QTableWidgetHandler():
    def Create(
            self,
            row : int,
            col : int,
            mainWindow
    ):
        if QWidgetChecker.Exist(mainWindow) == False:
            raise Exception("ERROR!!! Object does NOT exists.")
            
        self.tableView = QTableWidget(row,col,mainWindow)
        return self   
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
            self,
            mainWindow 
    ):
        if QWidgetChecker.Exist(mainWindow) == False:
            raise Exception("ERROR!!! Object does NOT exists.")
        self.checkbox = QCheckBox(mainWindow)
        return self
    
class QPushButtonHandler():
    def Create(
            self,
            mainWindow 
    ):
        if QWidgetChecker.Exist(mainWindow) == False:
            raise Exception("ERROR!!! Object does NOT exists.")
        self.pushButton = QPushButton(mainWindow)
        return self
    
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

class QGroupBoxHandler():
    def Create(
            self,
            title,
            mainWindow 
    ):
        if QWidgetChecker.Exist(mainWindow) == False:
            raise Exception("ERROR!!! Object does NOT exists.")
        self.groupbox = QGroupBox(mainWindow)
        return self

class KeywordBox:
    def Create(
            self,
            mainWindow , 
            title : str,
            placeholderText : str , 
            mainWindowPos: QRect , 
    ):
        if QWidgetChecker.Exist(mainWindow) == False:
            raise Exception("ERROR!!! Object does NOT exists.")
        self.groupboxHandler = QGroupBoxHandler()
        self.labelHandler = QLabelHandler()
        self.textEditHandler = QTextEditHandler()
        
        self.groupboxHandler = self.groupboxHandler.Create('searchGroupboxHandler',mainWindow)
        self.groupboxHandler.groupbox = QWidgetHandler.SetGeometry( self.groupboxHandler.groupbox , mainWindowPos )
        
        self.labelHandler = self.labelHandler.Create('title', self.groupboxHandler.groupbox)
        self.labelHandler.label = QWidgetHandler.SetGeometry( self.labelHandler.label , QRect(0,0,100,20) )
        self.labelHandler.label = TextHandler.SetText( self.labelHandler.label , title + ':' , QtCore.Qt.AlignRight)
        
        self.textEditHandler = self.textEditHandler.Create('title', self.groupboxHandler.groupbox)
        self.textEditHandler.textEdit = QWidgetHandler.SetGeometry( self.textEditHandler.textEdit , QRect(100 + 20 , 0 ,200 ,30) )
        self.textEditHandler.textEdit = TextHandler.SetText( self.textEditHandler.textEdit , '' , QtCore.Qt.AlignRight)
        self.textEditHandler.textEdit.setReadOnly(False)
        self.textEditHandler.textEdit.setPlaceholderText(placeholderText)
        return self
    def AddCheckbox(
            self,
            mainWindow
    ):
        if QWidgetChecker.Exist(mainWindow) == False:
            raise Exception("ERROR!!! Object does NOT exists.")
        self.checkboxHandler = QCheckboxHandler()
        self.checkboxHandler = self.checkboxHandler.Create(mainWindow)
        return self
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
    
    # Non-static method
    def Create(
              self,
              mainWindow : QMainWindow,
              title : str , 
              currentDirectory : str , 
              fileFilter : str ,
              saveGetMode : int
      ):
          self.fileDialog = QFileDialogHandler.CreateStatic(
                                                          mainWindow = mainWindow,
                                                          title = title, 
                                                          currentDirectory = currentDirectory , 
                                                          fileFilter = fileFilter,
                                                          saveGetMode = saveGetMode
                                                     )
          return self.fileDialog
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
            mainWindow : QMainWindow
    ):
        if row <= 0 or column <= 0 :
            raise Exception("ERROR!!! Invalid args in FileTableViewer class.")
        
        tableWH = tableWH.Create( row = row, col = column, mainWindow = mainWindow)
        
        tableWH.tableView = QWidgetHandler.SetGeometry(obj = tableWH.tableView , position = pos )
        
        tableWH.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tableWH.tableView.setColumnWidth(column,pos.width()//column)
        
        tableWidgetItemHandlerList = []
        tableWidgetItemHandlerSublist = []
        for ro in range(0,row,1):
            tableWidgetItemHandlerSublist = []
            for co in range(0,column,1):
               tableWidgetHandler_temp = QTableWidgetItemHandler()
               tableWidgetHandler_temp =tableWidgetHandler_temp.Create(args = "ro="+str(ro)+",co="+str(co))
               tableWidgetHandler_temp.item.setText(str(ro)+" "+str(co))
               tableWidgetItemHandlerSublist.append(tableWidgetHandler_temp)
            tableWidgetItemHandlerList.append(tableWidgetItemHandlerSublist)
               
        for ro in range(0,row,1):
            for co in range(0,column,1):
                tableWidgetItemHandlerList[ro][co].item.setFlags(
                    QtCore.Qt.ItemIsUserCheckable |
                    QtCore.Qt.ItemIsSelectable |
                    QtCore.Qt.ItemIsEnabled
                )
                tableWH.tableView.setItem(
                    ro,
                    co,
                    tableWidgetItemHandlerList[ro][co].item
                )
                
        tableWH.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        tableWH.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        tableWH.tableView.clicked.connect( 
            lambda : (
                    print("clicked"),
                    currentWidget := tableWH.tableView  ,
                    currentRow := copy.deepcopy( currentWidget.currentRow() ) ,
                    currentColumn := copy.deepcopy( currentWidget.currentColumn() ) ,
                    currentItem := tableWH.tableView.item(currentRow,currentColumn),
                    currentBackgroundColor := currentItem.background()  ,
                    nextBackgroundColor := ( QtGui.QColor(0,100,100)  if currentBackgroundColor != QtGui.QColor(0,100,100) else QtGui.QColor(255,255,255) ) ,
                    tableWH.tableView.item(currentRow,currentColumn).setBackground(  nextBackgroundColor )
                ) 
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
        
        allChildren = mainWindow.findChildren(QWidget)
        
        allChildrenExceptQTableWidget =  [
            elem for elem in allChildren if( isinstance( elem , QTableWidget ) == False) 
        ] 

        ## Do it for all QtWidget object except QTableWidget object and it's inherited object.
        for elem in allChildrenExceptQTableWidget :
            ## Add a lambda func as callback event after mouse press of the elem
            elem.mousePressEvent = lambda event : (
                 DeselectAll(
                     tableWH.tableView
                )    
            )        
        return tableWH
    
## Try to deselect the nth QTableView when clicking the QMainWindow just after clicking the nth QTableView.

def DeselectAll(table):
    print(GetInfo(table))  
    print(GetInfo(table.objectName())) ## Get 1th QTableView's name even when clicking QMainWindow object just after 2th QTableView's . 
    for ro in range(0,row,1):
        for co in range(0,column,1):
            item1 = table.item(ro,co)
            item1.setBackground(QtGui.QColor(255,255,255))
            
def GetInfo(obj) : return [obj,type(obj)]

if __name__ == '__main__':
    
    row = 12
    column = 2
    rectMainWindow = QRect(0,0,1000,1000)
 
    fileTableViewer1Pos = QRect(0,200,400,400) 
    fileTableViewer2Pos = QRect(500,200,400,400)
    
    inst =  QApplicationHandler()
    labelHandler = QLabelHandler()
    lineEditHandler = QLineEditHandler()
    textEditHandler = QTextEditHandler()
    pushButtonHandler = QPushButtonHandler()
    searchGroupboxHandler = KeywordBox()
    replaceGroupboxHandler = KeywordBox()   
    
    rightArrowPushButtonHandler = QPushButtonHandler()
    leftArrowPushButtonHandler = QPushButtonHandler()
    rightDoubleArrowPushButtonHandler = QPushButtonHandler()
    leftDoubleArrowPushButtonHandler = QPushButtonHandler()
       
    inst.CreateWindow('title')
    inst.mainWindow = QWidgetHandler.SetGeometry( inst.mainWindow ,rectMainWindow )
    
    mainGroupboxHandler = QGroupBoxHandler()
    mainGroupboxHandler = mainGroupboxHandler.Create('title', inst.mainWindow)
    mainGroupboxHandler.groupbox = QWidgetHandler.SetGeometry( mainGroupboxHandler.groupbox , inst.mainWindow.geometry() )
    
    searchGroupboxHandler = searchGroupboxHandler.Create(mainGroupboxHandler.groupbox , 'Search' ,'Search',QRect(0,0,1000//2,35) )

    replaceGroupboxHandler = replaceGroupboxHandler.Create(mainGroupboxHandler.groupbox , 'Replace' ,'Replace',QRect(0,35,1000//2,35) )
    
    replaceGroupboxHandler = replaceGroupboxHandler.AddCheckbox(mainGroupboxHandler.groupbox)
    replaceGroupboxHandler.checkboxHandler.checkbox = QWidgetHandler.SetGeometry( replaceGroupboxHandler.checkboxHandler.checkbox, QRect(500-100,35,100,30) )
    replaceGroupboxHandler.checkboxHandler.checkbox = TextHandler.SetText(replaceGroupboxHandler.checkboxHandler.checkbox, 'Replace', None)
    replaceGroupboxHandler.AddStateChangeEvent()
    
    arrowHandlerList = [
        rightArrowPushButtonHandler,
        leftArrowPushButtonHandler,
        rightDoubleArrowPushButtonHandler,
        leftDoubleArrowPushButtonHandler
    ]
    arrowTextList = [
        ">",
        "<",
        ">>",
        "<<"
    ]
    for i in range(0,len(arrowHandlerList),1):
        elem = copy.deepcopy(arrowHandlerList[i])
        elem = elem.Create(inst.mainWindow)
        elem.pushButton = QWidgetHandler.SetGeometry(obj = elem.pushButton, position = QRect(430,200 + (20 + 10 )*i,40,20))
        elem.pushButton = TextHandler.SetText(obj = elem.pushButton ,text = arrowTextList[i] , alignmentMode= None)
    
    fileTableViewerPosList = [fileTableViewer1Pos,fileTableViewer2Pos]
    fileTableViewerList = list()
    
    for i in range(0,2,1):
        tableWH = QTableWidgetHandler()
        fileTableViewer = FileTableViewer()
        fileTableViewer = fileTableViewer.Create(
                row = row, column = column , pos = fileTableViewerPosList[i] , mainWindow = inst.mainWindow ,
                tableWH = tableWH 
            )
        fileTableViewer.tableView.setObjectName("fileTableViewer"+str(i)) ## Set name of object of QTableView
        fileTableViewerList.append(fileTableViewer)
        
        del (tableWH)
        del (fileTableViewer)
        
    print(fileTableViewerList)
    
    pushButtonHandler = pushButtonHandler.Create(mainGroupboxHandler.groupbox)
    pushButtonHandler.pushButton = QWidgetHandler.SetGeometry( pushButtonHandler.pushButton , QRect(0,100,100,20) )
    pushButtonHandler.pushButton = TextHandler.SetText( pushButtonHandler.pushButton , 'Search' , None)
    
    inst.mainWindow.mousePressEvent = lambda event : (
         print("Window Clicked")     
    )
    
    inst.Show()
    inst.SysExit()
