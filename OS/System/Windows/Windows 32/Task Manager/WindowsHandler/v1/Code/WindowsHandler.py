from Win32GUIHandler import Win32GUIHandler
from ThreadScheduler import LoopHandler

import timeit
import asyncio

"""
A class that handles current running windows.
"""
class WindowsHandler():
    """
    Intro:
        Returned it (as close callback) when the window whose name is windowName is just closed.
    Parameter:
        1. windowName: name of window.
    Returned Value:
        None
    """
    @staticmethod
    async def JustClosed(windowName:str) -> bool:
        exists = Win32GUIHandler.ActiveWindows.Exists(windowName)
        if exists == False:
            raise Exception("windowsName does NOT exist")
        prevActiveWindows = Win32GUIHandler.ActiveWindows.GetActiveWindows(windowName)
        while True:
            currExists = Win32GUIHandler.ActiveWindows.Exists(windowName)
            if currExists == False:
                break
            currActiveWindows = Win32GUIHandler.ActiveWindows.GetActiveWindows(windowName)
            await asyncio.sleep(1)
        
"""
Driver code
"""   
if __name__ == '__main__':
    startTime = timeit.default_timer()
    """
    main code
    """ 
    async def main():
        try:
            windowName = 'Microsoft'
            await WindowsHandler.JustClosed(windowName)
        except Exception as ex:
            print(ex)
    """
    Intro:
        It is called iff the coroutine function main is just done.
    Parameter:
        None
    Returned Value:
        None
    """
    def doneCallback():
        endTime = timeit.default_timer()
        print("It took %d seconds." %(endTime - startTime) ) 
        
    done_callback = doneCallback
    LoopHandler.GetRunningLoop(lambda t: done_callback() , main)
    
    
