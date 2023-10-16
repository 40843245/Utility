import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QWidget

from PySide6.QtWidgets import QHBoxLayout , QLayout
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QSpacerItem
from PySide6.QtWidgets import QSizePolicy

from PySide6.QtCore import QRect
from PySide6.QtCore import Qt
from PySide6.QtCore import QObject

from PySide6.QtCore import QEvent
from PySide6.QtCore import QPoint

from PySide6.QtGui import QCursor

from EventHandler import PressedHandler,ReleasedHandler

"""
A class that cuts moved QObject from src to dest (if available and needed.) 

The conditions as following:
    src is NOT None.
    dest is NOT None.
    moved is NOT None.
    src is QWidget.
    dest is QWidget.
    src is NOT equivalent to dest. (Since it is not necessary to cut a object with same window.)
    The window of moved is equivalent to src.
    
"""
class MoveHandler():
    """
    A method that cuts moved QObject from src to dest (if available and needed.) 
    """
    @staticmethod
    def Cut(src : QWidget , dest : QWidget , moved : QObject ):
        if src == None:
            raise Exception("src must not be a None object.")
        if dest == None:
            raise Exception("dest must not be a None object.")
        if moved == None:
            raise Exception("moved must not be a None object.")
        if src.isWidgetType() != True :
            raise Exception("src must be a widget object.")
        if dest.isWidgetType() != True :
            raise Exception("dest must be a widget object.")
        if isinstance(moved, QObject) != True :
            raise Exception("moved must not be a object object.")
        if src == dest :
            raise Exception("src must not be same as dest.")
        if moved.window() != src :
            raise Exception("moved must be one of widgets of src.")
            
        # Add widget moved
        dest.mainLayout.addWidget(moved,0)
        # Remove widget moved
        src.mainLayout.removeWidget(moved)
        

"""
A class that drags src QObject to position pos (in same window).    
"""
class DragHandler():
    """
    A method that drags src QObject to position pos (in same window).    
    """
    @staticmethod
    def SetGeometry(src : QObject ,pos:QPoint):
        src.setGeometry(pos.x(),pos.y(),src.width(),src.height())
        
           
"""
A class that handles events on widgets of Widget.
NOTICE about the method eventFilter.
"""
class KeyPressEater(QObject):
    def __init__(self):
        super().__init__()
        self.isPressing = False
        self.pressedObj = None
        self.oldCursorPos = None
        self.newCursorPos = None
        self.topLevelWindow = None
        self.pressedHandler = PressedHandler()
        self.releasedHandler = ReleasedHandler()
        self.SetRoot(None)
    
    """
    Override
    Override the method QObject.eventFilter
    NOTICE that 
    before use it, invoke installEventFilter.
    For more details, see Qt Official Docs.
    """
    def eventFilter(self, obj : QObject ,event : QEvent):
        eventType = event.type()
        # Mouse Pressed
        if  eventType == QEvent.MouseButtonPress :
            self.pressedHandler.Update(obj)
            self.isPressing = True
            self.Update()       
            
        # Mouse Released
        elif eventType == QEvent.MouseButtonRelease:
            self.Update()
            self.topLevelWindow = QApplication.topLevelAt(self.newCursorPos)
            
            # do nothing
            if self.topLevelWindow == None:
                return QObject.eventFilter(self, obj, event)
            
            # do nothing
            if self.pressedHandler.obj == None or self.pressedHandler.window == None :
                return QObject.eventFilter(self, obj, event)
            if obj == self.rootObj :
               return QObject.eventFilter(self, obj, event)
            # On same window
            if self.pressedHandler.window == self.topLevelWindow :
                self.DragByCursor(obj)    
                self.pressedHandler.obj = None
                self.pressedHandler.window = None
            # On different window
            else :
                MoveHandler.Cut(self.pressedHandler.window, self.topLevelWindow, obj)
                # Clear all 
                self.pressedHandler.obj = None
                self.pressedHandler.window = None
        return QObject.eventFilter(self, obj, event)
    
    """
    The root of the instance. 
    For example,
    When a Widget instance (called W1) has a KeyPressEater (stored in W1.keyPressedEater)
    W1.keyPressedEater.rootObj is W1.
    """
    def SetRoot(self,rootObj : QObject = None):
        self.rootObj = rootObj
        
    """
    Set the dict of all available Widget.
    Format :
    {
        Window1 : Widget1 ,
        Window2 : Widget2
    }
    
    where Window1 is the window of Widget1 (i.e. Widget1.window() == Window1 )
    
    """
    def SetWindows(self,windows):
        self.windows = windows
        
    """
    Update position of cursor. 
    Copy self.newCursorPos to oldCursorPos.
    Then fetches the current pos through invoking QCursor.pos() iff other is specified as None or NOT specified.
    Otherwise (i.e. other is specified as a QPoint object), self.newCursorPos will be set to other.
    """
    def Update(self,other : ( QPoint | None ) = None ):
        if other == None:
            self.oldCursorPos = self.newCursorPos
            self.newCursorPos = QCursor.pos()
        else :
            self.oldCursorPos = self.newCursorPos
            self.newCursorPos = other
            
    """
    Drag the obj to the position self.newCursorPos 
    NOTICE that
    it is with same size.
    """
    def DragByCursor(self,obj):
        DragHandler.SetGeometry(obj , self.newCursorPos)

class Widget(QWidget):      
    def __init__(self):
        super().__init__()
        self.Create()
        
    def Create(self):
        self.keyPressEater = KeyPressEater()
        
        pushButton = QPushButton()
        lineEdit = QLineEdit()

        pushButton.setText("Button")
        pushButton.setFocusPolicy(Qt.ClickFocus)
        pushButton.installEventFilter(self.keyPressEater)
        
        lineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)
        lineEdit.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        lineEdit.setGeometry(QRect(100,100,100,100))
        lineEdit.installEventFilter(self.keyPressEater)
        
        pushButton.setParent(self)
        lineEdit.setParent(self)
"""
Driver code
"""
if __name__=='__main__':
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
        
    widget1 = Widget()
    widget1.setGeometry(QRect(0,100,200,300))
    widget1.setFocusPolicy(Qt.ClickFocus)
    widget1.installEventFilter(widget1.keyPressEater)
    widget1.keyPressEater.SetRoot(widget1)
    widget1.show()
    
    widget2 = Widget()
    widget2.setGeometry(QRect(0,100,200,300))
    widget2.setFocusPolicy(Qt.ClickFocus)
    widget2.installEventFilter(widget1.keyPressEater)
    widget2.keyPressEater.SetRoot(widget1)
    widget2.show()
     
    sys.exit(app.exec())
    
