from NestedFlatterInhomogenous import NestedFlatterInhomogenous

"""
A class that handles elems in list.
"""
class ElemsFinder():
    """
    Intro:
        Get all elems in list with indices not in keyIndices.
    Parameter:
        1. l: given list.
        2. keyIndices: a list of integers which indices in will be removed.
    Returned Value:
        A list after removal of l with given keyIndices.     
    """
    @staticmethod
    def GetOtherElem(l : list , keyIndices : list[int] ) -> list :
        if keyIndices is None:
            raise Exception("Invalid given indices.")
        r = [ l[i] for i in range(0,len(l),1) if not i in keyIndices]
        return r
    
    """
    Intro:
        Get all elems in list with indices in keyIndices.
    Parameter:
        1. l: given list.
        2. keyIndices: a list of integers which indices in will be removed.
    Returned Value:
        A list whose elem in l is not removed with given keyIndices.     
    """
    @staticmethod
    def GetTheseElem(l : list , keyIndices : list[int] ) -> list :
        if keyIndices is None:
            raise Exception("Invalid given indices.")
        r = [ l[i] for i in range(0,len(l),1) if i in keyIndices]
        return r
    
    """
    Intro:
        Get the difference of nested list (from l1 to l2).
        Similar to the result of l1 - l2.
    Parameter:
        1. l1: a list as source.
        2. l2: a list as target.
    Returned Value:
        Get the difference of nested list (from l1 to l2).
        See intro section.
    """
    @staticmethod
    def Diff(l1 : list , l2 : list) -> (list | None):
        if l1 is None:
            raise Exception("The list is empty.")
        if len(l1) <= 0 :
            return []
        if l2 is None:
            raise Exception("The list is empty.")
        if len(l2) <= 0 :
            return l1
        
        difference = list()
        for i in range(0,len(l1),1):
            if not l1[i] in l2 :
                difference.append(l1[i])
        return difference
                    
    """
    Intro:
        Get all indices where l[index] are matched more than 1 time for all index in indices.
        Here, we define elem1 and elem2 are matched iff
        elem1[i] == elem2[i] for i in keyIndices.
    Parameter:
        1. l: a list as source.
        2. keyIndices: a list. indicates indices.
    Returned Value:
        See intro section.
    """
    @staticmethod
    def IndicesOfSameKeys(l : list , keyIndices : list[int] ) -> ( (  list[int] | None ) , bool ):
        if l is None :
            raise Exception("Invalid indices of keys to filter out the given list.")
        if len(l) <= 0:
            return list()
        if keyIndices is None:
            raise Exception("Invalid indices of keys to filter out the given list.")
        if len(keyIndices) <= 0 :
            return l
        
        if len(keyIndices) > len(l[0][0]) :
            raise Exception("Invalid indices of keys to filter out the given list.")

        if len(keyIndices) == len(l[0][0]) :
            return l      
        
        indiceList = list()
        indiceList_t1 = list()
        flag = True
        
        for i in range(0,len(l),1):
            currL = l[i]      
            indiceList_t1 = list()
            if any([elem for elem in indiceList if i in elem]) != True:
                for j in range(i+1,len(l),1):
                    compL = l[j]
                    if any([elem for elem in indiceList if j in elem]) != True:
                        flag = True
                        for k in range(0,len(keyIndices),1):
                            if currL[k] != compL[k]:
                                flag = False
                                break
                        if flag == True:
                            indiceList_t1.append(j)
            if indiceList_t1 != None and len(indiceList_t1) > 0 :
                indiceList.append( [i] + indiceList_t1 )
        isNonEmpty = not indiceList is None and len(indiceList) > 0 
        return ( indiceList , isNonEmpty )
    
    """
    Intro:
        Get all value corresponding to indices where l[index] are matched more than 1 time for all index in indices.
        Here, we define elem1 and elem2 are matched iff
        elem1[i] == elem2[i] for i in keyIndices.
        For more details, see ElemsFinder.IndicesOfSameKeys() method.
    Parameter:
        1. l: a list as source.
        2. keyIndices: a list. indicates indices.
    Returned Value:
        See intro section.
    """
    @staticmethod
    def NestedValuesOfSameKeys(l : list , keyIndices : list[int] ) -> ( ( list[int] | None ) , bool ):
        if keyIndices is None :
            raise Exception("The indices are None.")
            
        if len(keyIndices) <= 0 :
            return l
        
        if l is None:
            raise Exception("The input list are None.")
        
        if len(l) <= 0 :
            return list()
            
        keysForCheck = list()
        for i in range(0,len(keyIndices),1):
            if not isinstance(keyIndices[i], (list,tuple) ) :
                keysForCheck.append(keyIndices[i])
        
        sameKeys = keyIndices 
        
        if not keysForCheck is None and len(keysForCheck) > 0 :
            ( sameKeys , isNonEmpty ) = ElemsFinder.IndicesOfSameKeys(l, keysForCheck)
            if isNonEmpty == False:
                return ( sameKeys , isNonEmpty ) 
        
        differentKeys = ElemsFinder.Diff(keyIndices, keysForCheck)

        sameItems = list()
        for i in range(0,len(sameKeys),1):
            for j in range(0,len(sameKeys[i]),1):
                elem = l[sameKeys[i][j]]        
                sameItems.append(elem)
        
        if differentKeys is None or len(differentKeys) <= 0:
            isNonEmpty = not sameItems is None and len(sameItems) > 0 
            return ( sameItems , isNonEmpty )
        differentKeys = NestedFlatterInhomogenous.PartiallyFlat(differentKeys,1)
        return ElemsFinder.NestedValuesOfSameKeys(sameItems, differentKeys)
    
"""
Driver code to test.
"""
if __name__ == '__main__':

    l = [
            ('Func1', [['argv1', None], ['argv2', 'int']], 'pass\n        '), 
            ('Func2', [['argv1', None], ['argv2', None], ['', None]], 'pass\n   '),
            ('Func1', [['argv1', None], ['argv2', 'int']], 'return "Func1"\n        '), 
            ('Func1', [['argv1', None], ['argv2', 'int']], 'Nothing'), 
            ('Func2', [['argv1', None], ['argv2', None], ['', None]], 'return "Func2"'),
            ('Func1', [['argv1', None] ] , 'pass\n        '), 
            ('Func1', [['argv1', None] ] , 'return "Func1"'), 
            ('Func3', [['argv1', None] ] , 'pass\n        '), 
            ('Func3', [['argv1', None] , ['argv2',None]] , 'pass\n        '),        
        ]
    
    testData = [
        [0,1], # ElemsFinder.NestedIndicesOfSameKeys(l, keyIndices) will return all elem where both 0th and 1th are same (in order) for any two elem among l.
        [0,1,2], # it will return all elem where both 0th, 1th and 2th are same (in order) for any two elem among l.
        [0,[1,2]], # it will return all elem where 0th is same (in order) for any two elem among l, and for each elem of 1th among l, 0th and 1th are same.
        [0,[1]], # it will return all elem where 0th is same (in order) for any two elem among l, and for each elem of 1th among l,1th are same.
        [0,[]], # they get same result: calling ElemsFinder.NestedIndicesOfSameKeys(l, [0,[]]) and ElemsFinder.NestedIndicesOfSameKeys(l, [0])
        [[],[]], # they get same result: calling ElemsFinder.NestedIndicesOfSameKeys(l, [[],[]]) and ElemsFinder.NestedIndicesOfSameKeys(l, [] ). And it will return l
        [], # it will also return l 
        # None, # raise Exception
    ]
    for i in range(0,len(testData),1):
        keyIndices = testData[i]
        r1 = ElemsFinder.IndicesOfSameKeys(l, keyIndices)
        r2 = ElemsFinder.NestedValuesOfSameKeys(l, keyIndices)
        print("%sth test data:" %(str(i)))
        print("keyIndices:")
        print(keyIndices)
        print("result of method call ElemsFinder.IndicesOfSameKeys(l, keyIndices):")
        print(r1)
        print("result of method call ElemsFinder.NestedValuesOfSameKeys(l, keyIndices):")
        print(r2)
        print('-'*40)
    
