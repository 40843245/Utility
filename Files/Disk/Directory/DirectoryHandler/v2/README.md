# DirectoryHandler (Handles a directory) (2th version)
## Objectives
1. List sub-directories and sub-files in specified string as the current directory.
2. 

## API
### class DirectoryHandler()
#### class FileLister()

##### GetFiles
In DirectoryHandler.FileLister.GetFiles( directory : (str,list) ), if directory is a string, then it will 1 list with 4 elem containing 

    a list of sub-directories and sub-files ,
    a list of paths ( concatenation of directory and sub-directory and file ), 
    a list whose elem is a file, 
    and a list whose elem is a folder.

If directory is a list, then it will return a list for all elem in specified directory. I implement it with list comprehension in Python.

The syntax looks like this.

        @staticmethod
        def GetFiles(
                directory : ( str , list )
        ):
            

## Used Modules
    os (built-in)
## Release Notes
### 2023/09/19 20:37 
initial notes
