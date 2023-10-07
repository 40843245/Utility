class ObjectHandler():
    class Filler():
        @staticmethod
        def Fill(
                src : ( None | list | tuple ),
                expectedType : str ,
                expectedLength : int ,
                defaultElem
        ):
            if expectedLength <= 0 :
                raise Exception("The expected number of element ( named expectedLength ) must be a positive integer.")
            if not expectedType in ["list","tuple"]:
                raise Exception("The expected type ( named expectedType ) must be either following type:\n" +
                                "list,"+"tuple")
            expectedTypeMap = { 
                "list" : list ,
                "tuple" : tuple 
            }
            expectedType = expectedTypeMap[expectedType]
            
            timesToFilled = 0
            prefix = None
            if src == None:
                timesToFilled = expectedLength
                prefix = expectedType() 
            else:
                timesToFilled =  expectedLength - len(src)
                prefix = src
            ret = [ defaultElem for elem in range(0,timesToFilled ,1) ]
            ret = expectedType(ret)
            retVal = prefix + ret           
            return retVal 
                
            
def Demo():
    r = ObjectHandler.Filler.Fill(
        None,
        "list",
        2,
        4
    )
    print(r)
    
    r = ObjectHandler.Filler.Fill(
        [ 1 ] ,
        "list",
        2,
        4
    )
    print(r)
    
    r = ObjectHandler.Filler.Fill(
        [ 1 , 5 ],
        "list",
        2,
        4
    )
    print(r)
    
    r = ObjectHandler.Filler.Fill(
        [ ] ,
        "list",
        2,
        4
    )
    print(r)
    
    r = ObjectHandler.Filler.Fill(
        [ 1 , 3 , 4] ,
        "list",
        2,
        4
    )
    print(r)
    
    r = ObjectHandler.Filler.Fill(
        [ [1,2,3] ] ,
        "list",
        2,
        4
    )
    print(r)
    
    r = ObjectHandler.Filler.Fill(
        ( 1 , ) ,
        "tuple",
        2,
        4
    )
    print(r)
    
    r = ObjectHandler.Filler.Fill(
        tuple() ,
        "tuple",
        2,
        4
    )
    
    r = ObjectHandler.Filler.Fill(
        ( 1 , 2 , 3) ,
        "tuple",
        2,
        4
    )
    print(r)
    
    
if __name__ == '__main__':
    Demo()
