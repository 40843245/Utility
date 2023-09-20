# DirectoryHandler (Handles a directory) (2th version)
## Added
1. Iterate for all elem in specified directory recusively.

For more details, see the 1th version which is located in ../v2 .
   
## API
### class DirectoryHandler()
#### class FileLister()

##### GetFiles
In DirectoryHandler.FileLister.GetFiles( directory : (str,list) , mode , nthiteration : ( int , None ) = 1 ).

If directory is a string, then it will 1 list with 4 elem containing 

    a list of sub-directories and sub-files ,
    a list of paths ( concatenation of directory and sub-directory and file ), 
    a list whose elem is a file, 
    and a list whose elem is a folder.

If directory is a list, then it will return a list for all elem in specified directory. I implement it with list comprehension in Python.

If mode is set DirectoryHandler.RecursiveModeEnum.NONRECURSIVE, then it will visit for sub-directories and sub-files directly to the specified directory as current directory(i.e. visit 1 depth).

If mode is set DirectoryHandler.RecursiveModeEnum.RECURSIVE, then it will visit for all sub-directories and sub-files (i.e. visit all depth) through recursion.

The syntax looks like this.

        @staticmethod
        def GetFiles(
                directory : ( str , list ) , 
                mode , 
                nthiteration : ( int , None ) = 1
        ):
###### Parameter 
The argument mode should be a DirectoryHandler.RecursiveModeEnum object. It can be one of these:

    DirectoryHandler.RecursiveModeEnum.NONRECURSIVE
    DirectoryHandler.RecursiveModeEnum.RECURSIVE
###### Returned value
Represents like a signle linked node.

Return a list of tuple whose 0th elem is a string as current directory, 1th elem contains all four things which are listed above. 

You can consider a list of nodes. Each node containing keys where keys as current directory and values where values are listed above.

## Used Modules
    os (built-in)
    enum (built-in)
## Release Notes
### 2023/09/20 09:35
initial notes
