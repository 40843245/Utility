# DragHandler.py (1th version)
## Objective
After mouse pressing then mouse releasing, the QObject will be moved from old cursor position to new cursor position.
## API
### class DragHandler()

A class that drags QObject.

#### def SetGeometry()

Set the src to pos.

The new position of src after changed will be equal to 

    pos.x() , pos.y() , src.width() , src.height()

The method setGeometry will be executed.

The code of the func is :

    src.setGeometry(pos.x(),pos.y(),src.width(),src.height())
    
Syntax :

    def SetGeometry(src:QWidget,pos:QPoint)

Parameter :

1. src : must be a QObject as source.

2. pos : must be a QPoint. Indicates the position after changed.

Returned Value :

    None

### class KeyPressEater():
NOTICE that 

it inherits QObject class.

The syntax of class definition is :

    class KeyPressEater(QObject):
    
#### def eventFilter()

NOTICE that 

the method overrides QObject.eventFilter.

Syntax :

    def eventFilter(self, obj : QObject ,event : QEvent)

Parameter :

1. obj : must be a QObject. Indicates the QObject that is handled.
2. event : must be a QEvent. Indicates the type of event that is handled.

Returned Value :

    Returns a bool value. Indicates whether to continue to filter it out. Returning True indicates that stop it being handled further. 

    Otherwise (i.e. Returning False) indicates that continue it being handled further.

For more details, see the website in See Also section.

##### See Also

Qt Official Website :

https://doc.qt.io/qt-6/qobject.html#eventFilter

#### def DragByCursor()

Updates the variable about cursor ( such as self.oldCursorPos and self.newCursorPos ) and set the geometry of QObject self.pressedObj.

NOTICE that 

it will invoke the method (my own developed) DragHandler.SetGeometry.

Syntax : 
    
    def DragByCursor(self):

Parameter :

    None

Returned Value :

    None

## NOTICE 
NOTICE that

To use the eventFilter method, 

first, instantiate the KeyPressEater (which defined in 1th of code, see the See Also section) by 

    self.keyPressEater = KeyPressEater()

next, invoke the method installEventFilter of a QObject object (or its subclass object).

such as 

    lineEdit = QLineEdit()
    
    lineEdit.installEventFilter(self.keyPressEater)

For more details, see the 1th version of code. 

### See Also

The 1th version of code is available at GitHub.

https://github.com/40843245/Utility/blob/main/GUI/PySide/PyQt5/QObject/Drag/DragHandler/v1/Code/DragHandler.py

## Demo

Demo video at YT :

https://youtu.be/eGwXALVloTk

## Website of Document and Code

Doc (README.md) :

https://github.com/40843245/Utility/blob/main/GUI/PySide/PyQt5/QObject/Drag/DragHandler/v1/README.md

Code (DragHandler.py) :

https://github.com/40843245/Utility/blob/main/GUI/PySide/PyQt5/QObject/Drag/DragHandler/v1/Code/DragHandler.py

Demo video : 

https://youtu.be/eGwXALVloTk

## Known issues
1. Many QObjects can be on same y axis since it is implemented by QLayout.
   
## Newer version
Known issues are available at latest version in DragHandler/OtherWindow/
## Release Notes
### 2023/10/15 19:15
Initial Notes.
### 2023/10/16 15:06
Added Known issues and update newer version.

