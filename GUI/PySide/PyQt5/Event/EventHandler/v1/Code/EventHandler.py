from PySide6.QtCore import QObject

"""
A class that handles about QWidget (QObject object and its)
"""
class WidgetHandler():
    def __init__(self):
        self.Update(None)
    """
    Update.
    Update the attrs obj and window.
    """
    def Update(self,obj : ( QObject | None ) ) :
        if obj != None:
            self.obj = obj 
            self.window = obj.window()
        else :
            self.obj = None
            self.window = None
 
"""
A class about press event.
"""
class PressedHandler(WidgetHandler):
    def __init__(self):
        super().__init__()

"""
A class about release event.
"""
class ReleasedHandler(WidgetHandler):
    def __init__(self):
        super().__init__()    

"""
A class about focus in event.
"""
class FocusInHandler(WidgetHandler):
    def __init__(self):
        super().__init__()

"""
A class about focus out event.
"""
class FocusOutHandler(WidgetHandler):
    def __init__(self):
        super().__init__()
