from modulefinder import ModuleFinder

class ModuleLister: 
    @staticmethod
    def GetLoadedModules(
            fileName : str
    ):
        finder = ModuleFinder()
        finder.run_script(fileName)

        result = list()
        for ( name, mod ) in finder.modules.items():
            result.append( [ name  , ','.join(list(mod.globalnames.keys())[:3] )  ] )
        return result
    @staticmethod 
    def IsLoadedModule(
            fileName : str,
            moduleName : str
    ) -> bool :
        result = ModuleLister.GetLoadedModules(fileName=fileName)
        keys = [ k for (k,v) in result ]
        if moduleName in keys :
            return True
        return False

if __name__ == '__main__' :
    print('Loaded modules:')
    r = ModuleLister.GetLoadedModules("ModuleLister.py")
    print(r)
    print("-"*20)
    r = ModuleLister.IsLoadedModule("ModuleLister.py","modulefinder")
    print(r)
    
