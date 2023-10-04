# DocumentHandler (1th versiom)
## Objective 

## API
### DocumentHandler
#### SetInputFile

Set the full path and name of the input file.

Syntax :
      
        SetInputFile(self,inputFile:str)

Parameter :

1. self : Of course, is the instance itself.
2. inputFile : full path and name of the input file.

Returned Value :

None

#### Load

Load the file with attr self.inputFile. 
Syntax :
      
        Load(self)

Parameter :

1. self : Of course, is the instance itself

Returned Value :

None

#### SetSpellChecker

Set the spell checker.

Syntax :
      
        SetSpellChecker(self,spellChecker:dict):

Parameter :

1. self : Of course, is the instance itself
2. spellChecker : It should be a dict. When each word exactly matches one of keys of spellChecker. Then the word will be replaced into its value.

Returned Value :

None

#### SetSaveFullName

Set the full path and name for output file.
     
Syntax :
      
       SetSaveFullName(self,saveFullName:str)

Parameter :

1. self : Of course, is the instance itself
2. saveFullName : The full path and name for output file.

Returned Value :

None

#### Save

Save the file with the member self.saveFullName.

Syntax :

    Save(self)

Parameter :

1. self : Of course, is the instance itself

Returned Value :

None

### ReplaceAll

Replace all content of the loaded file with spellChecker.

First, for all content of the loaded file, it will be splitted into words with one of delimiter ' ','\n', and '\t'

Second, for each word, it will be replaced with spellChecker. It will be replaced into its correspodning value iff it matches with one of keys in spellChecker/

(If it does not match, it will do nothing.)

Lastly, join each words. And get the result.

Syntax :

    ReplaceAll(self)

Parameter : 

    None

Returned Value:

    None

Used attr:

    spellChecker : self.spellChecker

## Used Module

My own Developement Module:

    StringHandler
## Release Notes
### 2023/10/05 6:49
Initial Notes
