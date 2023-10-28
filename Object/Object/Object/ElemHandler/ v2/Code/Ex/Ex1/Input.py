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
