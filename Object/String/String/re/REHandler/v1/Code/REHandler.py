import re
class REHandler():
    @staticmethod
    def WordRest(delim : str , s : str , rests : str ,ends : str ):        
        expr = r'(?<=('+delim+'))('+rests+'+'+ends+'*)'
        print("expr:"+expr)
        m = re.split(expr, s ,flags = re.NOFLAG)
        whitespace = ' '
        r = [ elem.removesuffix(whitespace) for elem in m if elem.endswith(delim) == False  ]
        nolast = r[:-1]
        return ( m , r , nolast)
        
if __name__ == '__main__':
    delim = '-'
    s = 'spam-egg bitch-shit'
    rests = '\w'
    ends = '\s'
    ( m , r , nolast) = REHandler.WordRest(delim,s,rests,ends)
    print('!'*40)
    print(s)
    print('@'*40)
    print(m)
    print(r)
    print(nolast)
    
    
    delim = '-e'
    s = 'spam-egg bitch-shit'
    rests = '\w'
    ends = '\s'
    ( m , r , nolast) = REHandler.WordRest(delim,s,rests,ends)
    print('!'*40)
    print(s)
    print('@'*40)
    print(m)
    print(r)
    print(nolast)
    
    delim = '-s'
    s = 'spam-egg bitch-shit'
    rests = '\w'
    ends = '\s'
    ( m , r , nolast) = REHandler.WordRest(delim,s,rests,ends)
    print('!'*40)
    print(s)
    print('@'*40)
    print(m)
    print(r)
    print(nolast)
