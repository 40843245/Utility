from StringHandler import StringHandler
class TextHandler():
    @staticmethod
    def Search(content:str,searchText):
        delimList = [ ' ','\n' , '\t' ]
        r = StringHandler.Split(content, delimList)
        return r
    @staticmethod
    def Replace( content:str, spellChecker : dict ):
        delimList = [' ','\n','\t']
        retVal = TextHandler.Search(content,delimList)
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
    content = 'a1 b2 c3\n d4'
    spellChecker = {
        'a1' : 'k1',
        'a2' : 'k2',
        'b1' : 'c2'
    }
    r = TextHandler.Replace(content,spellChecker)
    print(r)
