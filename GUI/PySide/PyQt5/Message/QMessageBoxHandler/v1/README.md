# QMessageBoxHandler (1th version)
## Objective 
A class that handles a QMessageBox object.
## Examples
See QMessageBoxHandler.py code at GitHub.

https://github.com/40843245/Utility/blob/main/GUI/PySide/PyQt5/Message/QMessageBoxHandler/v1/Code/QMessageBoxHandler.py

## API
### QMessageBoxHandler
#### def Create()
A staticmethod that create a new QMessageBox and open it. 

NOTICE that it does not close it automatically after the piece of code finishes running 

since it uses .exec() method which does NOT perform garbage collection.

Syntax :

    @staticmethod
    def Create(icon:QMessageBox.Icon, optionsDict : dict ,parent = None)

Parameter : 
1. icon : Must be QMessageBox.Icon.
2. optionsDict : Must be a dict. It can set window title, text, informative text, detailed text etc.
   
I recommend that it should contain these keys -- text, informativeText, detailedText, windowTitle.

As the word explains.

text : text.
informativeText : informative text.
detailedText : detailed text. When one clicks "Show details" button, it will show details, seeing detailedText.
windowTitle : title of window.

Format looks like this:

       optionsDict = {
        "text":"text",
        "informativeText":"informativeText",
        "detailedText":"detailedText",
        "windowTitle":"windowTitle"
    }
    
4. parent: It indicates what the parent it should be attached to. It defaults to None which means it will open a new window and does NOT attach to any window.


Returned Value :

    None

### class QCriticalBoxHandler()
#### def Create()
Calls 
    
    QMessageBoxHandler.Create(icon = QMessageBox.Critical,optionsDict=optionsDict,parent = parent )

See QMessageBoxHandler.Create section.

Syntax : 

    @staticmethod
    def Create(optionsDict : dict , parent = None):

### class QWarningBoxHandler()
#### def Create()
Calls 
    
    QMessageBoxHandler.Create(icon = QMessageBox.Warning,optionsDict=optionsDict,parent = parent )

See QMessageBoxHandler.Create section.

Syntax : 

    @staticmethod
    def Create(optionsDict : dict , parent = None):


### class QInfoBoxHandler()
#### def Create()
Calls 
    
    QMessageBoxHandler.Create(icon = QMessageBox.Information,optionsDict=optionsDict,parent = parent )

See QMessageBoxHandler.Create section.

Syntax : 

    @staticmethod
    def Create(optionsDict : dict , parent = None):

### class QQuestionBoxHandler()
#### def Create()
Calls 
    
    QMessageBoxHandler.Create(icon = QMessageBox.Question,optionsDict=optionsDict,parent = parent )

See QMessageBoxHandler.Create section.

Syntax : 

    @staticmethod
    def Create(optionsDict : dict , parent = None):

### class QNoIconBoxHandler()
#### def Create()
Calls 
    
    QMessageBoxHandler.Create(icon = QMessageBox.NoIcon,optionsDict=optionsDict,parent = parent )

See QMessageBoxHandler.Create section.

Syntax : 

    @staticmethod
    def Create(optionsDict : dict , parent = None):
    
## Release Notes
### 2023/10/09 10:50
Initial Notes.
