from LocalModuleFinder import LocalModuleFinder

def TestFunc1():
    return "TestFunc1!!!"

def TestFunc2():
    return "TestFunc2!!!"
    
if __name__ == '__main__':
    print(LocalModuleFinder.GetLocalModules())
