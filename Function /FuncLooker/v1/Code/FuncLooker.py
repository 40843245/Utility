import inspect
from FuncChecker import FuncChecker
class FuncLooker():
    class ArgLooker():
        @staticmethod
        def GetArgs(
                        func
                   ):
            if callable(func) == False:
                return list()
            if FuncChecker.IsFunc(func) == False:
                return list()
            return inspect.signature(func).parameters
        @staticmethod
        def GetArgsName(
                        func
                       ):
            return list(FuncLooker.ArgLooker.GetArgs(func))
            
if __name__ == '__main__' :
    def Func1():
        return 2
    testList = [
        Func1,
        lambda x : x + 2 , 
        2,
        dir(4),
        callable
     ]
    resultList =[
        FuncLooker.ArgLooker.GetArgsName(func=elem) for elem in testList
    ]
    print(resultList)
