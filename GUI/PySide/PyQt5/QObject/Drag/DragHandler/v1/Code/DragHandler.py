import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QWidget

from PySide6.QtWidgets import QHBoxLayout , QVBoxLayout , QLayout
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QSpacerItem
from PySide6.QtWidgets import QSizePolicy

from PySide6.QtCore import QRect
from PySide6.QtCore import Qt
from PySide6.QtCore import QObject

from PySide6.QtCore import QEvent
from PySide6.QtCore import QPoint

#from PySide6.QtGui import QResizeEvent
#from PySide6.QtGui import QDragMoveEvent
#from PySide6.QtGui import QKeyEvent
#from PySide6.QtGui import QDragEnterEvent
#from PySide6.QtGui import QMouseEvent
#from PySide6.QtGui import QDrag
#from PySide6.QtGui import QDropEvent
from PySide6.QtGui import QCursor

class DragHandler():
    def __init__(self):
        pass
    @staticmethod
    def SetGeometry(src:QWidget,pos:QPoint):
        src.setGeometry(pos.x(),pos.y(),src.width(),src.height())
        
class KeyPressEater(QObject):
    def __init__(self):
        super().__init__()
        self.isPressing = False
        self.pressedObj = None
        self.oldCursorPos = None
        self.newCursorPos = None
        
        
    def eventFilter(self, obj : QObject ,event : QEvent):
        eventType = event.type()
        if  eventType == QEvent.MouseButtonPress :
            self.isPressing = True
            self.pressedObj = obj 
            return QObject.eventFilter(self, obj, event)
        elif eventType == QEvent.MouseButtonRelease:
            self.DragByCursor()
            return QObject.eventFilter(self, obj, event)
        return QObject.eventFilter(self, obj, event)
    def DragByCursor(self):
        self.oldCursorPos = self.newCursorPos
        self.newCursorPos = QCursor.pos()
        DragHandler.SetGeometry(self.pressedObj, self.newCursorPos)
    
class Widget(QWidget): 
    def __init__(self):
        super().__init__()
        self.Create()
    def Create(self):
        self.keyPressEater = KeyPressEater()
        
        mainLayout = QHBoxLayout()
        pushButton = QPushButton()
        
        lineEdit = QLineEdit()
        
        spacerItem = QSpacerItem(100, 100)
        
        pushButton.setText("Button")
        pushButton.installEventFilter(self.keyPressEater)
        
        lineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)
        lineEdit.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        lineEdit.setGeometry(QRect(100,100,100,100))
        lineEdit.installEventFilter(self.keyPressEater)
                     
        mainLayout.addWidget(lineEdit,0)
        mainLayout.addSpacerItem(spacerItem)
        mainLayout.addWidget(pushButton,0)
        
        self.mainLayout = mainLayout
    
if __name__=='__main__':
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
        
    widget = Widget()
    widget.setLayout(widget.mainLayout)
    widget.setGeometry(QRect(0,0,1000,1000))
    widget.show()
    sys.exit(app.exec())
    
