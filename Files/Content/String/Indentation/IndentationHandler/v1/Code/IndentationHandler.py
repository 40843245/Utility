from StringHandler import StringHandler

class IndentationHandler():
    class Indentation():
        class String():
            """
            Intro:
                A method that get number of indentation for each line in given string.
            Parameter:
                s: given string.
            Returned Value:
                A dict that indicates :
                    1. which line is None or empty string.
                    2. If the line neither None or empty string, the number of indentation.
            """
            @staticmethod
            def GetIndentations(s:str):
                newline = '\n'
                tab = '\t'
                whitespace = ' '
                
                indentation = dict()
                lines = s.split(newline)
                numOfLines = len(lines)
                for i in range(0,numOfLines,1):
                    line = lines[i]
                    if line != None and len(line) > 0 :
                        currCnt = 0
                        whitespaceMap = list()
                        tabMap = list()
                        table = dict()
                        text = line[:]
                        while len(text) > 0 :
                            if text[0] == whitespace :
                                prefixCount = StringHandler.GetPrefixCount(text, whitespace)
                                whitespaceMap.append([currCnt,currCnt+prefixCount])
                                currCnt += prefixCount
                                text = text[prefixCount+1:]
                            elif text[0] == tab:
                                prefixCount = StringHandler.GetPrefixCount(text, tab)
                                tabMap.append([currCnt,currCnt+prefixCount])
                                currCnt += prefixCount
                                text = text[prefixCount+1:]
                            else :
                                break
                                
                            
                        table.update( {'whitespace': whitespaceMap} )
                        table.update( {'tab': tabMap} )
                        
                        indentation.update( { i : table} )
                    else :
                        indentation.update({i:None})
                return indentation
                
if __name__ == '__main__':
    s = """
    class DemoClass():
        def Func1():
            pass
    

    class DemoClass():
        class InnerClass():
            pass
        def Func2():
            pass
    
        def Func1():
            return "Method Func1 of DemoClass in demo_2.py file."
    """
    r = IndentationHandler.Indentation.String.GetIndentations(s)
    print(s)
    print(r)
                
