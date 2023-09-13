import inspect
from enum import Enum
                
class ClassModeEnum(Enum):
    OWNDEFINED_MEMBER = 1 ** 2 - 1
    BUILTIN__MEMBER = 2 ** 2 - 1
    ALL_MEMBER = 3 ** 2 - 1
class RecursiveModeEnum(Enum):
    VISIT_DEPTH_1  = 1 ** 2 - 1
    NONRECURSIVE_ALL = 2 ** 2 - 1

class ListHandler:
    @staticmethod
    def IsEmpty(
        list1:list
    ) -> bool :
        return list1 == None or len(list1) <= 0 
    
class StringHandler:
    @staticmethod
    def StartEnd(
        target : str  ,
        contains : str , 
        repetition : int
    ) -> bool :
        if repetition < 0:
            raise Exception("ERROR!!! The arg repetition should be a positive integer.")
        if repetition == 0:
            return True
        return target.startswith(contains*repetition) and target.endswith(contains*repetition)
    
class ClassFuncFinder:    
    @staticmethod
    def GetClass(
            className ,
            availables
    ):
      dicts = availables
      if not className in dicts :
          raise Exception("Error!!! The var with specified string does NOT exists!")
      return dicts[className]
    @staticmethod
    def GetMembers(
                className ,
                searchMode : ClassModeEnum
    ):
        nestedClass = inspect.getmembers(className)
        nestedClassPair = list()
        match searchMode:
            case ClassModeEnum.OWNDEFINED_MEMBER:
                nestedClassPair = [ (k,v) for (k,v) in nestedClass if ( StringHandler.StartEnd(target = k , contains = '_', repetition = 2) == False )]
            case ClassModeEnum.BUILTIN__MEMBER:
                nestedClassPair = [ (k,v) for (k,v) in nestedClass if ( StringHandler.StartEnd(target = k , contains = '_', repetition = 2) == True )]
            case ClassModeEnum.ALL_MEMBER:
                nestedClassPair = [ (k,v) for (k,v) in nestedClass]
            case _:
                raise Exception("ERROR!!! Invalid value of arg searchMode.")
        return nestedClassPair
    @staticmethod
    def GetMember(
            className ,
            funcName , 
            searchMode : ClassModeEnum        
    ): 
        nestedClassPair = ClassFuncFinder.GetMembers(className=className, searchMode=searchMode)
        nestedClassKeys = [k for (k,v) in nestedClassPair]
        if not funcName in nestedClassKeys:
            raise Exception("Error!!! The attr with specified string does NOT exists in the class!")
        targetClass = [ (k,v) for (k,v) in nestedClassPair if ( k == funcName )]
        return targetClass
    @staticmethod
    def GetVar(
            varName ,
            availables
    ):
        dicts = availables
        if not varName in dicts :
            raise Exception("Error!!! The var with specified string does NOT exists!")
        return dicts[varName]

class ClassFuncParser:
    @staticmethod
    def GetMemberTree(
            target : str,
            availables , 
            searchMode : RecursiveModeEnum ,
            result : list , 
            firstTime : bool
    ) -> list:
        if firstTime == True:
            result = list()
        if len(target) <= 0 :
            raise Exception("Error!!! The input string is Null or empty.")
        splittedS = target.split('.')
        c = ClassFuncFinder.GetClass(className=splittedS[0],availables=availables)
        currentClassPointer = c
        targetMembers = ClassFuncFinder.GetMembers(className=c, searchMode = ClassModeEnum.OWNDEFINED_MEMBER)
        match searchMode:
            case RecursiveModeEnum.NONRECURSIVE_ALL:
                result = list()
                stack1 = targetMembers
                while True:
                    if len(stack1) <= 0 :
                        break
                    x = stack1[0]
                    
                    if ListHandler.IsEmpty(x) == True:
                        break

                    # Case 1: x is a builtin
                    # In this case, just simply skip the elem.
                    if inspect.isbuiltin(x[1]) == True:
                        stack1.pop(0)
                    # Case 2: x is a function or a method 
                    # (note that it returns True iff x is a method and is instantiate)
                    # In this case, just simply append it to the resultant.
                    elif inspect.isfunction(x[1]) == True or inspect.ismethod(x[1]) == True:
                        tu = [ x[0],'function',list()]
                        result.append(tu)
                        stack1.pop(0)
                    # Case 3: x is a class
                    # In this case, One has to append x to the resultant then change the extension the 2th arg of last elem by doing same way.
                    elif inspect.isclass(x[1]) == True:
                        currentClassPointer = getattr(currentClassPointer,x[0])
                        tu = [ x[0],'class',list()]
                        result.append(tu)
                        y = currentClassPointer
                        sublist = ClassFuncFinder.GetMembers(className = y, searchMode = ClassModeEnum.OWNDEFINED_MEMBER)
                        # Access and change the value of last elem in last elem in resultant list.
                        result[-1][-1] = sublist
                        stack1.pop(0)
                        
                        idx = 0
                        for subelem in sublist:
                            stack1.insert(idx,subelem)
                            idx += 1
                    else:
                        stack1.pop(0)
                return result
            case _ :
                raise Exception("ERROR!!! Invalid value of the arg searchMode")
        
    

    
