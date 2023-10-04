# TextHandler (1th version)
## Objective
1. Handles plain text.
( such as search and replace etc)
## API
### class TextHandler()
#### Search
Search all occurences of the specified paragraph (which splitted by one of ' ', '\n', and '\t')

Syntax :

    @staticmethod
    def Search(content:str,searchText:str)

Parameter :
1. content : The plain text that will be searched for.
2. searchText : The text that will search to.

Returned Value :

Returns a list of tuple. Looks like:

    [   (  counter , smallestFoundIndexCorr , tempList  ) ] 

### class TextHandler()
#### Replace
Replace all occurences of the specified paragraph named content with the given dict named spellChecker.

The content will be splitted into many words with one of ' ', '\n', and '\t'. It uses StringHandler.Split(content,delimList).

    delimList = [ ' ','\n','\t']

Then, each word will be replaced, if it is in keys of spellChecker, into the corresponding value.

If it is not in keys of spellChecker, nothing will be performed.

Lastly, each word will be joined with the 1th elem of returned value -- StringHandler.Split(content,delimList) .

Syntax :

    @staticmethod
    def Search(content:str,searchText:str)

Parameter :
1. content : The plain text that will be replaced for.
2. spellChecker : A dict that contains pairs which each word will be replaced to its corresponding value if it is one of the keys of spellChecker.

Returned Value :

Returns a list of tuple. Looks like:

    [   (  counter , smallestFoundIndexCorr , tempList  ) ] 

## Example
### Example 1
#### Code

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

#### Expected Output

     --------------------
    [(1, 0, 'a1')]
    --------------------
    --------------------
    k1 b2 c3
     d4
    --------------------
#### Output

    --------------------
    [(1, 0, 'a1')]
    --------------------
    --------------------
    k1 b2 c3
     d4
    --------------------

#### Explanation

For 1th part, it will search all occurences of "a1" ( case-sensitive and matching only whole word )

For 2th part, 

'a1' will be replaced into 'k1'.

'a2' will be replaced into 'k2'.

'b1' will be replaced into 'c2'.

## Used Module
My Developed Module

    StringHandler

which avaialables at Github.

https://github.com/40843245/Utility/blob/main/Object/String/String/StringHandler/v1/Code/StringHandler.py

## Release Notes
### 2023/10/04 16:27
Initial Notes.
