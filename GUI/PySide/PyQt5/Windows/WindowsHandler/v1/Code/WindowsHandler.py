from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QPoint

""" 
A class that handles about lots of window.
"""
class WindowsHandler():
    """
    Check the position pos is in window except src.
    NOTICE that
    if src is None, it always returns False.
    """
    @staticmethod
    def PosInOtherWindow( windows : list[QWidget] = list(), src = None , pos : QPoint = QPoint(0,0) ):
        if src == None:
            return False
        for window in windows :
            if window == None:
                continue
            if src == window :
                continue
            if window.rect().contains(pos,True) == True:
                return True
        return False
