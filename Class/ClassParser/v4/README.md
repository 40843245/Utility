# ClassParser_v4 (4th version of ClassParser)
## Examples
### Example 1 (for top-level class) (bug example)
#### Statement
The test block is shown as
         
        r = ClassFuncParser.GetMemberTree(target = "TestClass", availables = globals(), searchMode = RecursiveModeEnum.NONRECURSIVE_ALL)
         
Sorry for put it in the gray block. I would NOT like to do so, but it will NOT display the text as expected when 
I combine a whitespace, the double dash and then a whitespace in other place than gray block. I am a little forced to do so.

#### Expected Output
It should like this. The format of output may be different. I also omit some item with the symbol ... . 

                  [ [('TestClass', <class '__main__.TestClass'>),[ [('Hello',<function TestClass.Hello at 0x0000000000>)],[('Sound',<function TestClass.Sound at 0x000000000000>), ...] ,['a', [('a1_1', <class '__main__.TestClass.a.a1_1'>), ('a1_func1', <function TestClass.a.a1_func1 at 0x0000021FB45420C0>)]], ['a1_1', [('a1_1_func1', <function TestClass.a.a1_1.a1_1_func1 at 0x0000021FB4542200>), ('a1_1_func2', <function TestClass.a.a1_1.a1_1_func2 at 0x0000021FB45422A0>)]]]]]
                  
#### Output
A runtime error occured.
         
         UnboundLocalError: cannot access local variable 'currentMember' where it is not associated with a value
### Example 2
#### Statement
The test block is shown as
         
         r = ClassFuncParser.GetMemberTree(target = "TestClass.a", availables = globals(), searchMode = RecursiveModeEnum.NONRECURSIVE_ALL)
         
#### Output

         [['a', [('a1_1', <class '__main__.TestClass.a.a1_1'>), ('a1_func1', <function TestClass.a.a1_func1 at 0x000002650F92DF80>)]], ['a1_1', [('a1_1_func1', <function TestClass.a.a1_1.a1_1_func1 at 0x000002650F92E0C0>), ('a1_1_func2', <function TestClass.a.a1_1.a1_1_func2 at 0x000002650F92E160>)]]]

### Example 3
#### Statement
The test block is shown as

             r = ClassFuncParser.GetMemberTree(target = "TestClass.a", availables = globals(), searchMode = RecursiveModeEnum.VISIT_DEPTH_1)

#### Output

         [['a', <class '__main__.TestClass.a'>], ['a1_1', <class '__main__.TestClass.a.a1_1'>]]
## Change
### Fixed
1. In ClassFuncParser.GetMemberTree method.
   Instead of listing all members of the specified class which are defined at top (for convenience, we call it as top-level class of the module.) .
   It can list all members of specified class (including nested class).

   I have tried <b>nested class</b> which is defined as a child in class, ensuring that they are NO bugs.

## Known issues
1. Get unexpected result on top-level class
   For more details, see Examples section.

## Release Notes
### 2023/09/14 14:52 
Initial Notes
### 2023/09/15 15:01
#### Add 
1. Example 2 and Example 3 to Notes.
2. Fix the code of the file ClassParser_v4.py and update it. I forgot to all the case-statement inside match block. It's so ridculous.


