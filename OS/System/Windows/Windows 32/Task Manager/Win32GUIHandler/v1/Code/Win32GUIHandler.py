import win32gui

class Win32GUIHandler():
    class ActiveWindows():
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
        
        @staticmethod
        def Exists(windowName:str) -> bool :
            activeWindows = Win32GUIHandler.ActiveWindows.GetActiveWindows(windowName)
            return len(activeWindows) > 0 
if __name__ == '__main__':
    windowName = 'Spyder'
    activeWindows = Win32GUIHandler.ActiveWindows.Exists(windowName)
    #del active_windows[-4:]
    print(activeWindows)
