import urllib.request

class MacroMicro():
    class Data():
        @staticmethod
        def GetResponse(website:str) :
            if website != None and len(website) > 0 :
                with urllib.request.urlopen(website) as response:
                    html = response.read()
                    return (response,html)
                
if __name__ == '__main__':
    website = 'http://python.org/'
    (response,html) = MacroMicro.Data.GetResponse(website)
    print("response:")
    print(response)
    print("html:")
    print(html)
                
