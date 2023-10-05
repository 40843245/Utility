import os

class AnacondaHandler():
    class Spyder():
        class AutoSave():
            def __init__(self,spyder):
                self.spyder = spyder
            def Reset(self):
                self.autosave_fullpath = os.path.join( self.spyder.userPath , self.spyder.autosave_path) 
            def ListFiles(self):
                files = os.listdir(self.autosave_fullpath)
                files = [ os.path.join(self.autosave_fullpath,elem) for elem in files ]
                return files
            
        def __init__(self):
            self.drive = "C:"
            self.slash = "\\"
            self.users = "Users"
            self.spyderPath = ".spyder-py3"
            self.history = "history.py"
            self.historyinternal = "history_internal.py"
            self.template = "template.py"
            self.autosave_path = "autosave"
            self.langconfig = "langconfig"
            
        def SetUser(self,username : str) :
            self.username = username 
            self.userPath = os.path.join( self.drive + self.slash , self.users , self.username , self.spyderPath  )
           
        def GetHistory(self):       
            path = os.path.join( self.userPath , self.history ) 
            if os.path.exists(path) != True:
                raise Exception("path does not exist.")
            file = open(path,'r')
            content = file.read()
            file.close()
            return content
        
        def GetHistoryInternal(self):
            path = os.path.join( self.userPath , self.historyinternal ) 
            if os.path.exists(path) != True:
                raise Exception("path does not exist.")
            file = open(path,'r')
            content = file.read()
            file.close()
            return content
        
        def GetTemplate(self):
            path = os.path.join( self.userPath , self.template ) 
            if os.path.exists(path) != True:
                raise Exception("path does not exist.")
            file = open(path,'r')
            content = file.read()
            file.close()
            return content
        
        def GetLang(self):
            path = os.path.join( self.userPath , self.langconfig ) 
            if os.path.exists(path) != True:
                raise Exception("path does not exist.")
            file = open(path,'r')
            content = file.read()
            file.close()
            return content
            
        
        
            
if __name__ == '__main__' :
    spyder = AnacondaHandler.Spyder() 
    spyder.SetUser("40843")
    
    r = spyder.GetHistory()
    print(r)
    
    r = spyder.GetHistoryInternal()
    print(r)
    
    r = spyder.GetTemplate()
    print(r)
    
    r = spyder.GetLang()
    print(r)
    
    autosave = spyder.AutoSave(spyder)
    autosave.Reset()
    r = autosave.ListFiles()
    print(r)
