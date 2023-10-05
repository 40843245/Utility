# AnacondaHandler (2th version)
## Added
1. Jupyter Notebook ( in this version, only it is implemented , accessing info about Jupyter Notebook. I want to implement more functions in the future. )

## API
### AnacondaHandler
#### JupyterNotebook
##### SetUser()
Set username and update its full path of directory. 

Syntax :

    SetUser(self,username : str)

Parameter :

1. username : username

Returned Value :

None

##### GetConfig()
Set username and update its full path of directory. 

Syntax :

    GetConfig(self)

Parameter :

None

Returned Value :

A string that contains all configuration about Jupyter Notebook in Anaconda Navigator.

The directory about Jupyter Notebook in Anaconda Navigator is stored at:

    {jupyterPath} C:\Users\{username}\.jupyter

where

    # {username} refers username.

While its configuration file is stored at:

    {jupyterConfig} := {jupyterPath}\\{jypter_notebook_config}

where 

    {jypter_notebook_config} := "jypter_notebook_config.py"

NOTICE that in RE ( regular expression ) 

1. \ can escape the next character. \\ refers the literal '\'.
2. There are no whitespace between '\' in path.
    
## Release Notes
### 2023/10/05 21:39
Initial Notes of 2th version.

## Ref

From the figure of the reply on stackoverflow.

![image](https://github.com/40843245/Utility/assets/75050655/73209a08-440a-411b-bc71-b413f40edeed)

https://stackoverflow.com/questions/47772157/how-to-change-the-default-browser-used-by-jupyter-notebook-in-windows
