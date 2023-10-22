# REHandler.py (all version)
## Objective
1. A class that easier to handle a string through re (Regular expression).
# v1
## API
### class REHandler()
#### def WordRest()
Syntax :

     @staticmethod
        def WordRest(delim : str , s : str , rests : str ,ends : str ):        

Parameter :
1. delim : a string as delimiter that indicates the string to delimiter.
2. s : a string as source that indicates the string for handle.
3. rests : a string that indicates the expression just after delim (which occurs one or more times).
4. ends : a string that indicates the expression just after rests (which occurs zero, one or more times).

For more details, see the code.

Returned Value :
A tuple. 
    
    (expr, m, r, nolast )

where 
1. expr : the expression of the re (Regular expression).
2. m : the list after the string s is splitted by re.split.
3. r : m which not ends with delim.
4. nolast : copy all elem except the last in r.

NOTICE :
NOTICE that m contains elem that is delim or ends with delim.
Thus, I handle it with list comprehension (and store it in r).

### Code

Expression : (store it in expression)

    expr = r'(?<=('+delim+'))('+rests+'+'+ends+'*)'

Split : (store it in m)

    m = re.split(expr, s ,flags = re.NOFLAG)

Remove elem whose elem ends with delim : (store it in m)

    whitespace = ' '
    r = [ elem.removesuffix(whitespace) for elem in m if elem.endswith(delim) == False  ]

Remove the last : (store it in nolast)
    
    nolast = r[:-1]
    
## Examples
### Example 1
#### Code

    delim = '-'
    s = 'spam-egg bitch-shit'
    rests = '\w'
    ends = '\s'
    (expr, m , r , nolast) = REHandler.WordRest(delim,s,rests,ends)
    print('!'*40)
    print(expr)
    print(s)
    print('@'*40)
    print(m)
    print(r)
    print(nolast)

#### Output
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    (?<=(-))(\w+\s*)
    spam-egg bitch-shit
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    ['spam-', '-', 'egg ', 'bitch-', '-', 'shit', '']
    ['egg', 'shit', '']
    ['egg', 'shit']
### Example 2
#### Code
    delim = '-e'
    s = 'spam-egg bitch-shit'
    rests = '\w'
    ends = '\s'
    ( expr , m , r , nolast) = REHandler.WordRest(delim,s,rests,ends)
    print('!'*40)
    print(expr)
    print(s)
    print('@'*40)
    print(m)
    print(r)
    print(nolast)
#### Output
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    (?<=(-e))(\w+\s*)
    spam-egg bitch-shit
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    ['spam-e', '-e', 'gg ', 'bitch-shit']
    ['gg', 'bitch-shit']
    ['gg']
### Example 3
#### Code
    delim = '-s'
    s = 'spam-egg bitch-shit'
    rests = '\w'
    ends = '\s'
    ( expr, m , r , nolast) = REHandler.WordRest(delim,s,rests,ends)
    print('!'*40)
    print(expr)
    print(s)
    print('@'*40)
    print(m)
    print(r)
    print(nolast)
#### Output
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    (?<=(-s))(\w+\s*)
    spam-egg bitch-shit
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    ['spam-egg bitch-s', '-s', 'hit', '']
    ['hit', '']
    ['hit']

# v2
## Examples
Here are examples of REHandler.SplitParagraph.
### Input
     print('!'*40)
    
    keyword = 'class'
    s = 'class Response(): def Yes(): pass \n'
    rests = '\w'
    ends = '\s'
    r = REHandler.SplitParagraph(s,keyword)
    print('-'*40)
    print(r)
        
    print('!'*40)    
    
    keyword = 'class'
    s = 'class Response(): def No(): pass \n'
    rests = '\w'
    ends = '\s'
    r = REHandler.SplitParagraph(s,keyword)
    print('-'*40)
    print(r)
    

    print('!'*40)
    
    keyword = 'class'
    s = 'class Response(): def Unknown(): pass \n'
    rests = '\w'
    ends = '\s'
    r = REHandler.SplitParagraph(s,keyword)
    print('-'*40)
    print(r)
    

    print('!'*40)
    
    keyword = 'class'
    s = 'class Response(): def Unknown(): pass \nclass Animal(): def Dog(): pass'
    rests = '\w'
    ends = '\s'
    r = REHandler.SplitParagraph(s,keyword)
    print('-'*40)
    print(r)

### Output
     !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
     ----------------------------------------
     [' Response(): def Yes(): pass \n']
     !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
     ----------------------------------------
     [' Response(): def No(): pass \n']
     !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
     ----------------------------------------
     [' Response(): def Unknown(): pass \n']
     !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
     ----------------------------------------
     [' Response(): def Unknown(): pass \n', ' Animal(): def Dog(): pass']
## API
### class REHandler()
#### def WordRest()
See the v1 version.
#### def NextWord()
Syntax : 
     
     @staticmethod
     def NextWord(s : str , keyword:str):
     
Parameter :
1. s : target for search.
2. keyword : keyword to search.

Returned Value :

Returns next words after all ocuurences of the keyword (if keyword is matched successfully). Otherwise, returns the empty list.

#### def SplitParagraph()
Syntax :

    @staticmethod
    def SplitParagraph(s : str , keyword: str):

Parameter :
1. s : target for search.
2. keyword : keyword to search.

Returned Value :

A list that is splitted by the keyword with given s.

## Release Notes
### 2023/10/21 10:01
Initial Notes.
### 2023/10/22 11:22
Update the 2th version (upload codes in zip and add introduction)
