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

    
