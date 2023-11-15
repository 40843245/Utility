import win32gui

"""
A class of wrapper of win32gui.
"""
class Win32GUIHandler():
    """
    A class of wrapper of win32gui that get current active windows.
    """
    class ActiveWindows():
        """
        Intro:
            Get all current active windows.
        Parameter:
            None
        Returned Value:
            Returns all current active windows.
        """
        @staticmethod
        def GetAllActiveWindows():
            activeWindows = list()
            toplist = list()
            win32gui.EnumWindows(lambda hWnd, 
               param: toplist.append((hWnd, win32gui.GetWindowText(hWnd))), None)
            for (hwnd, title) in toplist:
                if win32gui.IsWindowVisible(hwnd) and title != '':
                    activeWindows.append(title)
            return activeWindows        

        """
        Intro:
            Get all current active windows whose name is windowName.
        Parameter:
            1. windowName: 
                name of window
        Returned Value:
            Returns all current active windows whose name is windowName.
        """        
        @staticmethod
        def GetActiveWindows(windowName:str) -> ( str | None ) :
            if windowName is None:
                raise Exception("windowName must be a non-empty string.")
            if not isinstance(windowName, str):
                raise Exception("windowName must be a non-empty string.")
            if len(windowName) <= 0:
                raise Exception("windowName must be a non-empty string.")
                
            allActiveWindows = Win32GUIHandler.ActiveWindows.GetAllActiveWindows()
            activeWindows = list()
            for activeWindow in allActiveWindows:
                if activeWindow.count(windowName) > 0 :
                    activeWindows.append(activeWindow)
            return activeWindows
        
        """
        Intro:
            Check there exists windows whose name is windowName.
        Parameter:
            1. windowName: 
                name of window
        Returned Value:
            Returns True iff it exists. Otherwise, return False.
        """  
        @staticmethod
        def Exists(windowName:str) -> bool :
            activeWindows = Win32GUIHandler.ActiveWindows.GetActiveWindows(windowName)
            return len(activeWindows) > 0 
if __name__ == '__main__':
    windowName = 'Spyder'
    activeWindows = Win32GUIHandler.ActiveWindows.Exists(windowName)
    print(activeWindows)
