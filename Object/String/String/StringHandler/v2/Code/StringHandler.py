class StringHandler():
    """
    Intro:
        Get the how many occurences of prefix (which is given in ) in given string (which given in s).
    Parameter:
        s: given string as target.
        keyword: keyword for counting the occurences.
    Returned Value:
        Returns a nonnegative integer that indicates how many occurences of prefix (which is given in ) in given string (which given in s).
    """
    @staticmethod
    def GetPrefixCount(s:str,keyword:str):
        removedS = s.lstrip(keyword)
        count = ( len(s) - len(removedS) ) // len(keyword)
        return count
    
    """
    Intro:
        Get the how many occurences of suffix (which is given in ) in given string (which given in s).
    Parameter:
        s: given string as target.
        keyword: keyword for counting the occurences.
    Returned Value:
        Returns a nonnegative integer that indicates how many occurences of suffix (which is given in ) in given string (which given in s).
    """
    @staticmethod
    def GetSuffixCount(s:str,keyword:str):
        removedS = s.rstrip(keyword)
        count = ( len(s) - len(removedS) ) // len(keyword)
        return count
if __name__ == '__main__':
    s = """  class DemoClass():
        def Func1():
            pass
    """
    keyword = ' '
    r = StringHandler.GetPrefixCount(s, keyword)
    print("How many occurences are there of '%s' in '%s' at beginning?" % (keyword,s) )
    print(r)
    
    s = """  class DemoClass():
        def Func1():
            pass
    """
    keyword = ' '
    r = StringHandler.GetSuffixCount(s, keyword)
    print("How many occurences are there of '%s' in '%s' at end?" % (keyword,s) )
    print(r)
