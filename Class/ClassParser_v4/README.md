# ClassParser_v4 (4th version of ClassParser)
## Examples
### Example 1 (for top-level class)
#### Agrument
The test block is shown in 
         
         the block __name__ == '__main__' in the file ./test.py .
         
Sorry for put it in the gray block. I would NOT like to do so, but it will NOT display the text as expected when 
I combine a whitespace, the double dash and then a whitespace in other place than gray block. I am a little forced to do so.

#### Expected Output

#### Output
A runtime error occured.
         
         UnboundLocalError: cannot access local variable 'currentMember' where it is not associated with a value
         
## Change
### Fixed
1. In ClassFuncParser.GetMemberTree method.
   Instead of listing all members of the specified class which are defined at top (for convenience, we call it as top-level class of the module.) .
   It can list all members of specified class (including nested class).

   I have tried <b>nested class</b> which is defined as a child in class, ensuring that they are NO bugs.

## Known issues
1. Get unexpected result on top-level class
   For more details, see Examples section.
