import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QHBoxLayout , QVBoxLayout , QLayout
from PySide6.QtWidgets import QMessageBox 

class QMessageBoxHandler():
    @staticmethod
    def Create(icon:QMessageBox.Icon, optionsDict : dict ,parent = None):
        messageBox  = QMessageBox(parent=parent)
        messageBox.setText(optionsDict.get("text"))
        messageBox.setInformativeText(optionsDict.get("informativeText"))
        messageBox.setDetailedText(optionsDict.get("detailedText"))
        messageBox.setWindowTitle(optionsDict.get("windowTitle"))
        messageBox.setIcon(icon)
        messageBox.exec()
        
class QCriticalBoxHandler():
    @staticmethod
    def Create(optionsDict : dict , parent = None):
        QMessageBoxHandler.Create(icon = QMessageBox.Critical,optionsDict=optionsDict,parent = parent )
        
class QWarningBoxHandler():
    @staticmethod
    def Create(optionsDict : dict ,parent = None):
        QMessageBoxHandler.Create(icon = QMessageBox.Warning,optionsDict=optionsDict,parent = parent )
        
class QInfoBoxHandler():
    @staticmethod
    def Create(optionsDict : dict ,parent = None):
        QMessageBoxHandler.Create(icon = QMessageBox.Information,optionsDict=optionsDict,parent = parent )
        
class QQuestionBoxHandler():
    @staticmethod
    def Create(optionsDict : dict ,parent = None):
        QMessageBoxHandler.Create(icon = QMessageBox.Question,optionsDict=optionsDict,parent = parent )
        
class QNoIconBoxHandler():
    @staticmethod
    def Create(optionsDict : dict , parent = None):
        QMessageBoxHandler.Create(icon = QMessageBox.NoIcon,optionsDict = optionsDict,parent = parent )
        

        
class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.Create()
    def Create(self):
        mainLayout = QHBoxLayout()
        self.mainLayout = mainLayout
if __name__=='__main__':
    
    optionsDict = {
        "text":"text",
        "informativeText":"informativeText",
        "detailedText":"detailedText",
        "windowTitle":"windowTitle"
    }
    
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    widget = Widget()
    widget.setLayout(widget.mainLayout)
    widget.show()
    
    QCriticalBoxHandler().Create(optionsDict ,parent = widget)
    sys.exit(app.exec())
    
