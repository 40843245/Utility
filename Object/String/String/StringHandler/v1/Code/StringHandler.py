class StringHandler():
    NOTFOUND = -1
    @staticmethod
    def Split( content:str,delimList : list[str] ):
        resultList = list()
        counter = 0
        while content != None and len(content) > 0 :
            counter = counter + 1           
            notFound = True
            smallestFoundIndexCorr = StringHandler.NOTFOUND
            tempList = list()
            smallestFoundIndex = len(content)         
            for i in range(0,len(delimList),1):   
                foundIndex  = content.find(delimList[i])    
                if foundIndex != StringHandler.NOTFOUND :
                    if foundIndex < smallestFoundIndex : 
                        smallestFoundIndex = foundIndex
                        smallestFoundIndexCorr = i 
                    notFound = False
                    
            if notFound == False:
                tempList = content[ 0 : smallestFoundIndex]
                content = content[ smallestFoundIndex + 1 : ]
                resultList.append( (  counter , smallestFoundIndexCorr , tempList  ) )
            else: 
                tempList = content[ : ]
                content = None
                resultList.append( (  counter , smallestFoundIndexCorr , tempList  ) )
            
        retVal = resultList
        return retVa
