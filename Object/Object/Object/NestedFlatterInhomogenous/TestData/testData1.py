from NestedFlatter import NestedFlatter

from NestedFlatterInhomogenous import NestedFlatterInhomogenous

import time

def Demo():
    NUMEBR = 1000
    
    print("For a 1D array-like object.")    
    print("The test data:")
    cnt = 0 
    for idx in range(NUMEBR - 1,NUMEBR,1):
        print("%dth data:" % (cnt) )
        testData = [ elem for elem in range(0,idx,1) ]
        print(testData)
        
    for idx in range(NUMEBR - 1,NUMEBR,1):
        testData = [ elem for elem in range(0,idx,1) ]
        
        print("With NestedFlatter.Flat method.")
        startTime = time.time_ns()
        NestedFlatter.Flat(testData)
        endTime = time.time_ns()
        interval = round(endTime - startTime,17)
        print("It took %.17f nanoseconds to flat the nested array-like object." % (interval) )
        
        print("With NestedFlatterInhomogenous.Flat method.")
        startTime = time.time_ns()
        NestedFlatterInhomogenous.Flat(testData)
        endTime = time.time_ns()
        interval = round(endTime - startTime,17)
        print("It took %.17f nanoseconds to flat the nested array-like object." % (interval) )
        
    #
    print("For a nested array-like object.")
    print("The test data:")
    cnt = 0 
    for idx in range(NUMEBR - 1,NUMEBR,1):
        print("%dth data:" % (cnt) )
        testData = [ [ elem for elem in range(0,idx,1) ] , [ elem for elem in range(idx,idx*2,1) ] ] 
        print(testData)
        
    for idx in range(NUMEBR - 1,NUMEBR,1):
        testData = [ [ elem for elem in range(0,idx,1) ] , [ elem for elem in range(idx,idx*2,1) ] ] 
        
        print("With NestedFlatter.Flat method.")
        startTime = time.time_ns()
        NestedFlatter.Flat(testData)
        endTime = time.time_ns()
        interval = round(endTime - startTime,17)
        print("It took %.17f nanoseconds to flat the nested array-like object." % (interval) )
        
        print("With NestedFlatterInhomogenous.Flat method.")
        startTime = time.time_ns()
        NestedFlatterInhomogenous.Flat(testData)
        endTime = time.time_ns()
        interval = round(endTime - startTime,17)
        print("It took %.17f nanoseconds to flat the nested array-like object." % (interval) )
        
        
        
if __name__ == '__main__':
    Demo()    
