import os

class DirectoryHandler():
    class FileLister():
        @staticmethod
        def GetFiles(
                directory : ( str , list )
        ):
            if isinstance( directory ,  str ) == True:
                fileList  = os.listdir(directory)
                paths = [ os.path.join(directory,elem) for elem in fileList  ]
                files = [ elem for elem in paths if os.path.isfile(elem) == True ]
                dirs = [ elem for elem in paths if os.path.isdir(elem) == True ]
                return [ files , paths , files , dirs ]
            elif isinstance( directory ,  list ) == True:
                return [  DirectoryHandler.FileLister.GetFiles(directory = elem) for elem in directory]
            
            
        
if __name__ == '__main__':
    directory = "C:\\"
    r = DirectoryHandler.FileLister.GetFiles(directory = directory)
    print(r)
    
    directoryList = [ "C:\\Qt" , "C:\\Users"]
    r = DirectoryHandler.FileLister.GetFiles(directory = directoryList)
    print(r)
    
