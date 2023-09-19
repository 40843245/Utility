import os

class DirectoryHandler():
    class FileLister():
        @staticmethod
        def GetFiles(
                directory : str
        ):
            fileList  = os.listdir(directory)
            
            print(fileList)
            
            paths = [ os.path.join(directory,elem) for elem in fileList  ]
            
            files = [ elem for elem in paths if os.path.isfile(elem) == True ]
            
            dirs = [ elem for elem in paths if os.path.isdir(elem) == True ]
            
            return [ files , paths , files , dirs ]
        
        
if __name__ == '__main__':
    directory = "C:\\"
    r = DirectoryHandler.FileLister.GetFiles(directory = directory)
    print(r)
    
