from OfficeFiles import ExcelsHandler 
from OfficeFiles import DocxHandler
from OfficeFiles import PowerPointHandler

import FileChecker

class OfficeFilesHandler():
    @staticmethod
    def SearchAll(
        fullname : str ,
        searchText : str
    ):
        if FileChecker.FileHandler.FileChecker.Microsoft.Office.PowerPoint.IsPowerPoint(fullname) == True:
            print(fullname+" is a PowerPoint.")
            powerpointHandler = PowerPointHandler.PowerPointHandler()
            powerpointHandler.SetInputFullName(fullname)
            powerpointHandler.Load()
            r = powerpointHandler.SearchAll(searchText)
            return r
        elif FileChecker.FileHandler.FileChecker.Microsoft.Office.Word.IsWord(fullname) == True:
            print(fullname+" is a Word.")
            documentHandler = DocxHandler.DocumentHandler()
            documentHandler.SetInputFullName(  fullname  )
            documentHandler.Load()
            documentHandler.CopyToSaveFileName()
            r = documentHandler.SearchAll(searchText)
            
        elif FileChecker.FileHandler.FileChecker.Microsoft.Office.Excel.IsExcel(fullname) == True:
            print(fullname+" is a Excel.")
            excelsHandler = ExcelsHandler.ExcelsHandler()
            excelsHandler.SetInputFullNames( [ fullname ] )
            excelsHandler.Load()
            r = excelsHandler.SearchAll(searchText)
            return r
    #
    @staticmethod
    def ReplaceAll(
        fullname : str ,
        searchText : str,
        replaceText : str
    ):
        if FileChecker.FileHandler.FileChecker.Microsoft.Office.PowerPoint.IsPowerPoint(fullname) == True:
            print(fullname+" is a PowerPoint.")
            powerpointHandler = PowerPointHandler.PowerPointHandler()
            powerpointHandler.SetInputFullName(fullname)
            powerpointHandler.CopyToSaveFullName()
            powerpointHandler.Load()
            r = powerpointHandler.ReplaceAll(searchText,replaceText)
            return r
        elif FileChecker.FileHandler.FileChecker.Microsoft.Office.Word.IsWord(fullname) == True:
            print(fullname+" is a Word.")
            spellChecker = {
                searchText : replaceText
            }
            documentHandler = DocxHandler.DocumentHandler()
            documentHandler.SetInputFullName(  fullname  )
            documentHandler.Load()
            documentHandler.CopyToSaveFileName()
            documentHandler.SetSpellChecker(spellChecker)
            r = documentHandler.ReplaceAll()
            return r
            
        elif FileChecker.FileHandler.FileChecker.Microsoft.Office.Excel.IsExcel(fullname) == True:
            print(fullname+" is a Excel.")
            excelsHandler = ExcelsHandler.ExcelsHandler()
            excelsHandler.SetInputFullNames( [ fullname ] )
            excelsHandler.CopyToSaveFullNames()
            excelsHandler.Load()
            r = excelsHandler.ReplaceAll(searchText,replaceText)
            return r
        
if __name__ == '__main__':
    directory = r"C:\Users\40843\OneDrive\Utility\GUI\PySide\PySide6\QTableViewHandler\OfficeFiles"
    name = "test.pptx"
    slash = '\\'    
    fullpath = directory + slash + name

    r = OfficeFilesHandler.SearchAll(fullpath,"Bullet")
    print(r)
    
    print('-'*20)
    
    directory = r"C:\Users\40843\OneDrive\Utility\GUI\PySide\PySide6\QTableViewHandler\OfficeFiles"
    name = "Book2.xlsx"
    slash = '\\'
    
    fullpath = directory + slash + name
    r = OfficeFilesHandler.SearchAll(fullpath,"前輩有夠煩")
    print(r)
    
    directory = r"C:\Users\40843\OneDrive\Utility\GUI\PySide\PySide6\QTableViewHandler\OfficeFiles"
    name = "Document.docx"
    slash = '\\'
    fullpath = directory + slash + name
    
    r = OfficeFilesHandler.SearchAll(fullpath,"前輩有夠煩")
    print('-'*20)
