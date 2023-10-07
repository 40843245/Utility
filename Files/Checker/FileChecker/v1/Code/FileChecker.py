import ListHandler 
class FileHandler():
    class FileChecker():
        class ProgLang():
            class Python():
                @staticmethod
                def IsPython(src):
                    r = ListHandler.ListHandler.String.EndsWith(src, [".py",".pym"])
                    return r 
        class Microsoft():
            class Office():
                class Word():
                    @staticmethod
                    def IsWord(src):
                        r = ListHandler.ListHandler.String.EndsWith(src, [".doc",".docx"])
                        return r 
                class PowerPoint():
                    @staticmethod
                    def IsPowerPoint(src):
                        r = ListHandler.ListHandler.String.EndsWith(src, [".ppt",".pptx"])
                        return r 
                class Excel():
                    @staticmethod
                    def IsExcel(src):
                        r = ListHandler.ListHandler.String.EndsWith(src, [".xls",".xlsx"])
                        return r 
                    
if __name__ == '__main__':
    r = FileHandler.FileChecker.Microsoft.Office.Word.IsWord("test1.docx")
    print(r)
