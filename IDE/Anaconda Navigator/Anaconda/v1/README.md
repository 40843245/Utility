# AnacondaHandler (1th version)
## Objective
1. Get info about Anaconda Navigator with Python.
## API
### AnacondaHandler
#### Spyder
A class that gets Spyder info.
##### SetUser()

Set the username.

Syntax : 
    
    SetUser(self,username : str) 

Parameter :

1. username : username

Returned Value :

None

##### GetHistory()

Set the username.

Syntax : 
    
    GetHistory(self)

Parameter :

None

Returned Value :

A string.

It lists execution of file with Spyder Kernel.

##### GetHistoryInternal()

Set the username.

Syntax : 
    
    GetHistoryInternal(self):

Parameter :

None

Returned Value :

A string.

It lists Spyder Python Console History Log.

##### GetTemplate()

Set the username.

Syntax : 
    
    GetTemplate(self):

Parameter :

None

Returned Value :

A string.

It will return a template of Spyder. 

The template is loaded once you created a new file in Spyder.

##### GetLang()

Set the username.

Syntax : 
    
    GetLang(self):

Parameter :

None

Returned Value :

A string.

It will return the current used language in Spyder.

##### AutoSave
A class that handles about autosaves in Spyder.

NOTICE that

It is necessary to instantiate AnacondaHandler.Spyder().AutoSave() object and call method Reset() at the first time and once after changing the full path.

(it can be changed through calling method AnacondaHandler.Spyder().SetUser() )

###### Reset()

Reset the full path for autosave directory.

Syntax : 
    
    Reset(self):

Parameter :

None

Returned Value :

None

###### ListFiles()

List all directories and files of autosaves.

Syntax : 
    
    Reset(self):

Parameter :

None

Returned Value :

None

## Release Notes
### 2023/10/05 16:28
Initial Notes
