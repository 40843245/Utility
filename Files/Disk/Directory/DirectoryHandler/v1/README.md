# DirectoryHandler (Handles a directory) (1th version)
## Objectives
1. List sub-directories and sub-files in specified string as the current directory.

## API
### class DirectoryHandler()
#### class FileLister()

##### GetFiles
In DirectoryHandler.FileLister.GetFiles( directory : str), it will 1 list with 4 elem containing 

    a list of sub-directories and sub-files ,
    a list of paths ( concatenation of directory and sub-directory and file ), 
    a list whose elem is a file, 
    and a list whose elem is a folder.

The syntax looks like this.

        @staticmethod
        def GetFiles(
                directory : str
        ):
            

## Used Modules
    os (built-in)
## Release Notes
### 2023/09/19 20:37 
initial notes
