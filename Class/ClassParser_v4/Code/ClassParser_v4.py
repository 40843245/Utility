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
        list1 : list
    ) -> bool :
        return list1 == None or len(list1) <= 0 
    @staticmethod
    def HasExactly2ElemsInTuple(
            list1 : list
    ) -> bool :
        if ListHandler.IsEmpty(list1) == True:
            return False
        eachElem = [ True if ( isinstance(x,tuple) == True and len(x) == 2 ) else False for x in list1 ]
        result = all(eachElem)
        return result
        
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
          raise Exception("Error!!! The val with specified className does NOT exists in availables!")
      return dicts[className]
    @staticmethod
    def GetMembers(
                class1 : list,
                availables , 
                searchMode : ClassModeEnum
    ):
        nestedClass = inspect.getmembers(class1[0][1])
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
    def GetChild(
            childPair ,
            funcName , 
            availables , 
            searchMode : ClassModeEnum
    ):
        if funcName == None:
            return childPair      
        if ListHandler.HasExactly2ElemsInTuple(childPair) == False:
            raise Exception("Error!!! The attr with specified childPair either is NOT a tuple, or is a tuple but at least one elem of them does NOT have exactly 2 elems.")          
        child = [k for (k,v) in childPair]
        if not funcName in child:
            raise Exception("Error!!! The attr with specified string does NOT exists in the class!")
        targetClass = [ (k,v) for (k,v) in childPair if ( k == funcName )]
        return targetClass
    @staticmethod
    def GetMember(
            class1 ,
            funcName , 
            availables ,
            searchMode : ClassModeEnum        
    ): 
        nestedClassPair = ClassFuncFinder.GetMembers(class1 = class1, availables=availables, searchMode=searchMode)
        return ClassFuncFinder.GetChild(childPair = nestedClassPair , funcName = funcName ,availables = availables, searchMode = searchMode)
    @staticmethod
    def GetNestedMember(
            className : list ,
            availables , 
            searchMode : ClassModeEnum
    ):
        
        if ListHandler.IsEmpty(className):
            raise Exception("Error!!! The attr with specified className is either Null or empty!")
        lastMember = ClassFuncFinder.GetClass(className=className[0], availables=availables)
        lastMember = [ ( lastMember.__name__ , lastMember ) ]
        for i in range(1,len(className) ,1):
            currentClassName = className[i]
            currentMember = ClassFuncFinder.GetMember(class1 = lastMember, funcName=currentClassName, availables = availables, searchMode = searchMode)
            lastMember = currentMember
        return currentMember
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
    ) -> list:
        if len(target) <= 0 :
            raise Exception("Error!!! The input string is Null or empty.")
        splittedS = target.split('.')
        currentMember = ClassFuncFinder.GetClass(className=splittedS[0],availables=availables)
        currentMember = [ ( currentMember.__name__ , currentMember ) ]
        currentMember = ClassFuncFinder.GetNestedMember(className=splittedS, availables=availables, searchMode=ClassModeEnum.OWNDEFINED_MEMBER)
        
        match searchMode:
            case RecursiveModeEnum.NONRECURSIVE_ALL:
                result = list()
                stack1 = list(currentMember)
                while True:
                    
                    # exit the loop
                    if len(stack1) <= 0 :
                        break
                    
                    x = list(stack1[0])
                    
                    # exit the loop
                    if ListHandler.IsEmpty(x) == True:
                        break

                    # Case 1: x is a builtin
                    # In this case, just simply skip the elem.
                    if inspect.isbuiltin(x[1]) == True:
                        stack1.pop(0)
                    # Case 2: x is a function or a method 
                    # (note that it returns True iff x is a method and is instantiate)
                    # In this case, just simply skip the elem.
                    elif inspect.isfunction(x[1]) == True or inspect.ismethod(x[1]) == True:
                        stack1.pop(0)
                    # Case 3: x is a class
                    # In this case, One has to append x to the resultant then change the extension the 2th arg of last elem by doing same way.
                    elif inspect.isclass(x[1]) == True:
                        result.append(x)
                        x = [ x ]
                        sublist = ClassFuncFinder.GetMembers(class1 = x,availables = availables ,searchMode = ClassModeEnum.OWNDEFINED_MEMBER)
                        stack1.pop(0)
                        l = list()
                        idx = 0
                        cnt = idx
                        # Access and change the value of last elem in last elem in resultant list.
                        for subelem in sublist:    
                            flag = True
                            if inspect.isbuiltin(subelem[1]) == True:
                                print("inspect.isbuiltin(subelem[1]) == True")
                                flag = False
                            if flag == True:
                                stack1.insert(cnt,subelem)
                                l.insert(cnt,subelem)
                                cnt += 1 
                            idx += 1
                        result[-1][-1] = l
                    # Case 4: nothing else
                    # In this case, just simply skip the elem.
                    else:
                        stack1.pop(0)
                return result
                result = list()
                stack1 = list(currentMember)
                while True:
                    
                    # exit the loop
                    if len(stack1) <= 0 :
                        break
                    
                    x = list(stack1[0])
                    
                    # exit the loop
                    if ListHandler.IsEmpty(x) == True:
                        break

                    # Case 1: x is a builtin
                    # In this case, just simply skip the elem.
                    if inspect.isbuiltin(x[1]) == True:
                        stack1.pop(0)
                    # Case 2: x is a function or a method 
                    # (note that it returns True iff x is a method and is instantiate)
                    # In this case, just simply skip the elem.
                    elif inspect.isfunction(x[1]) == True or inspect.ismethod(x[1]) == True:
                        stack1.pop(0)
                    # Case 3: x is a class
                    # In this case, One has to append x to the resultant then change the extension the 2th arg of last elem by doing same way.
                    elif inspect.isclass(x[1]) == True:
                        result.append(x)
                        x = [ x ]
                        sublist = ClassFuncFinder.GetMembers(class1 = x,availables = availables ,searchMode = ClassModeEnum.OWNDEFINED_MEMBER)
                        stack1.pop(0)
                        l = list()
                        idx = 0
                        cnt = idx
                        # Access and change the value of last elem in last elem in resultant list.
                        for subelem in sublist:    
                            flag = True
                            if inspect.isbuiltin(subelem[1]) == True:
                                print("inspect.isbuiltin(subelem[1]) == True")
                                flag = False
                            if flag == True:
                                stack1.insert(cnt,subelem)
                                l.insert(cnt,subelem)
                                cnt += 1 
                            idx += 1
                        # result[-1][-1] = l
                    # Case 4: nothing else
                    # In this case, just simply skip the elem.
                    else:
                        stack1.pop(0)
                return result
            case _ :
                raise Exception("ERROR!!! Invalid value of the arg searchMode")
                
