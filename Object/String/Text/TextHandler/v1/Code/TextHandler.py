from StringHandler import StringHandler
class TextHandler():
    @staticmethod
    def Search(content:str,searchText:str):
        delimList = [ ' ','\n' , '\t' ]
        r = StringHandler.Split(content, delimList)
        resultList = [ (elem1,elem2,elem3) for (elem1,elem2,elem3) in r if elem3 == searchText]
        return resultList
    @staticmethod
    def Replace( content:str, spellChecker : dict ):
        delimList = [' ','\n','\t']
        retVal = StringHandler.Split(content,delimList)
        spellCheckerKeysList = list( spellChecker.keys() )        
        s = ""
        for i in range(0,len(retVal),1):
            if retVal[i][2] in spellCheckerKeysList:
                s += spellChecker[retVal[i][2]] 
            else:
                s += retVal[i][2]
            if retVal[i][1] != StringHandler.NOTFOUND:
                s += delimList[retVal[i][1] ]
        return s

if __name__ == '__main__':
    content = "a1 b2 c3\n d4"
    searchText = "a1"
    spellChecker = {
        'a1' : 'k1',
        'a2' : 'k2',
        'b1' : 'c2'
    }
    r = TextHandler.Search(content,searchText)
    print('-'*20)
    print(r)
    print('-'*20)
    r = TextHandler.Replace(content,spellChecker)
    print('-'*20)
    print(r)
    print('-'*20)
    
