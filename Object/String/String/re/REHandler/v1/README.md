# REHandler.py (all version)
## Objective
1. A class that easier to handle a string through re (Regular expression).
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

## Release Notes
### 2023/10/21 10:01
Initial Notes.
