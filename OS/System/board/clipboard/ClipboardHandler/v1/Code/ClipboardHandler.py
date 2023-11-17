import pyperclip
"""
A class that handles OS's clipboard.
"""
class ClipboardHandler():
    """
    A class that handles OS's clipboard (with static method).
    """
    class Clipboard():
        """
        Intro:
            Copy the text to clipboard. It will set the text of OS's clipboard.
        Parameter:
            1. text: text for copying.
        Returned Value:
            parameter text.
        """
        @staticmethod
        def Copy(text:str = '') -> str :
            pyperclip.copy(text)
            return text
        """
        Intro:
            Copy the text to clipboard. It will set the text of OS's clipboard.
        Parameter:
            None
        Returned Value:
            Returns a string type. Returns the text of clipboard.
        """
        @staticmethod
        def Paste() -> str :
            return pyperclip.paste()
        """
        Intro:
            Append the text to clipboard. (i.e.Insert text at end). It will set the text of OS's clipboard.
        Parameter:
            1. text: text for appending.
        Returned Value:
            Returns a string type. Returns the text that will be copied to OS's clipboard.
        """
        @staticmethod
        def Append(text : str = '') -> str :
            pastedText = ClipboardHandler.Clipboard.Paste()
            copiedText = pastedText + text
            ClipboardHandler.Clipboard.Copy(copiedText)
            return copiedText
if __name__ == '__main__':
    ClipboardHandler.Clipboard.Copy('copied.')
    r = ClipboardHandler.Clipboard.Paste()
    ClipboardHandler.Clipboard.Append('append.')
