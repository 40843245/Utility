import os
from enum import Enum


class DirectoryHandler():
    class RecursiveModeEnum(Enum):
        NONRECURSIVE = 1
        RECURSIVE = 2
    
    class FileLister():
        result = list()
        temp = list()
        @staticmethod
        def GetFiles(
                directory : ( str , list ) , 
                mode , 
                nthiteration : ( int , None ) = 1
        ):
            match mode:
                case DirectoryHandler.RecursiveModeEnum.NONRECURSIVE :
                    if isinstance( directory ,  str ) == True:
                        fileList  = os.listdir(directory)
                        paths = [ os.path.join(directory,elem) for elem in fileList  ]
                        files = [ elem for elem in paths if os.path.isfile(elem) == True ]
                        dirs = [ elem for elem in paths if os.path.isdir(elem) == True ]
                        return [ files , paths , files , dirs ]
                    elif isinstance( directory ,  list ) == True:
                        return [  DirectoryHandler.FileLister.GetFiles(directory = elem , mode = mode ) for elem in directory]
                case DirectoryHandler.RecursiveModeEnum.RECURSIVE:
                    files = DirectoryHandler.FileLister.GetFiles(directory = directory , mode = DirectoryHandler.RecursiveModeEnum.NONRECURSIVE , nthiteration = nthiteration + 1 )
                    files = ( directory , files )  
                    if len(files[1][3]) <= 0 :
                        DirectoryHandler.FileLister.result.append( files )
                        return None
                    for elem in files[1][3]:
                        if len(elem) <= 0 :
                            continue
                        temp = DirectoryHandler.FileLister.GetFiles(directory = elem , mode = DirectoryHandler.RecursiveModeEnum.NONRECURSIVE , nthiteration = nthiteration + 1)         
                        temp = ( elem , temp)
                        DirectoryHandler.FileLister.result.append( temp )
                        if temp[1] != None and len(temp[1]) >= 3 and len(temp[1][3]) > 0 :
                            temp = DirectoryHandler.FileLister.GetFiles(directory = elem , mode = DirectoryHandler.RecursiveModeEnum.RECURSIVE , nthiteration = nthiteration + 1)                                     
                    return  DirectoryHandler.FileLister.result
                case _ :
                    raise Exception("ERROR!!! Invalid value of arg mode!")
            
        
if __name__ == '__main__':
    directory =  "C:\\Test"
    r = DirectoryHandler.FileLister.GetFiles(directory = directory , mode = DirectoryHandler.RecursiveModeEnum.NONRECURSIVE )
    print(r)
    
    directory =  "C:\\Test"
    r = DirectoryHandler.FileLister.GetFiles(directory = directory , mode = DirectoryHandler.RecursiveModeEnum.RECURSIVE , nthiteration = 1)
    print(r)
    
