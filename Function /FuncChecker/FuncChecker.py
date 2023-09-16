import types

class FuncChecker():
    """
    NOTE:
        only available on >= Python 3.2
        For more details, see the reply answered by John Feminella
        https://stackoverflow.com/questions/624926/how-do-i-detect-whether-a-variable-is-a-function
    """    
    @staticmethod
    def IsFunc( 
            func
    ) -> bool :
        return ( FuncChecker.IsCFunc(func = func) or
                 FuncChecker.IsPythonFunc(func = func)
               )
    @staticmethod
    def IsCFunc( 
            func
    ) -> bool :
        return isinstance(func, types.FunctionType)
    
    @staticmethod
    def IsPythonFunc( 
            func
    ) -> bool :
        return callable(func)
    

    
if __name__ == '__main__':
    def TestFunc1():
        return 1
    def FuncInfo(
            func
        ):
        no = " NOT "
        msg = ( str(func) + " is "+ no +"a func." ) if FuncChecker.IsFunc(func) == False else ( str(func) + " is a func.")
        return msg
    
    x = 2
    y = TestFunc1()
    dir1 = dir(3)
    none = None
    list1 = list()
    tuple1 = tuple()
    dict1 = dict()
    callable1 = callable
    testList = [ 
        lambda a : a + 2 ,
        TestFunc1,
        x,
        y,
        dir1,
        none,
        list1,
        tuple1,
        dict1,
        callable1
    ]
 
    resultList = [ FuncInfo(arg) for arg in testList ]
    print(resultList)
