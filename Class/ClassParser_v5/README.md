# ClassParser_v5 (5th version of ClassParser)
## Preface
The code of classParser_v5 is very similar to ../ClassParser_v4/Code/ClassParser_v4.py .

For more details, see the Fixed section.

## Examples 
### Example 1
#### Statement
    r = ClassFuncParser.GetMemberTree(target = "TestClass", availables = globals(), searchMode = RecursiveModeEnum.VISIT_DEPTH_1)
#### Output
    [['TestClass', <class '__main__.TestClass'>], ['a', <class '__main__.TestClass.a'>], ['a1_1', <class '__main__.TestClass.a.a1_1'>]]
### Example 2
#### Statement
        r = ClassFuncParser.GetMemberTree(target = "TestClass", availables = globals(), searchMode = RecursiveModeEnum.NONRECURSIVE_ALL)
#### Output
    [['TestClass', [('Hello', <function TestClass.Hello at 0x0000018700681260>), ('Sound', <function TestClass.Sound at 0x0000018700681620>), ('a', <class '__main__.TestClass.a'>)]], ['a', [('a1_1', <class '__main__.TestClass.a.a1_1'>), ('a1_func1', <function TestClass.a.a1_func1 at 0x0000018700681F80>)]], ['a1_1', [('a1_1_func1', <function TestClass.a.a1_1.a1_1_func1 at 0x00000187006820C0>), ('a1_1_func2', <function TestClass.a.a1_1.a1_1_func2 at 0x0000018700682160>)]]]
### Example 3
#### Statement 
    r = ClassFuncParser.GetMemberTree(target = "TestClass.Sound", availables = globals(), searchMode = RecursiveModeEnum.NONRECURSIVE_ALL)
#### Expected Output
I expect that it return all members of TestClass.Sound .
#### Output
    []
## Change
### Fixed
1. Solve the runtime error of top-level class ( for example, getting expected output when running the code of Example 1 in ../ClassParser_v4/README.md .) .

At first, I just so careless. I just forgot to one following statement and the runtime error solved.

    I just add one following statement in ../ClassParser_v4/Code/ClassParser_v4.py

At first, a runtime error occured -- UnboundedLocalError.

For more details, see Example 1 section in Examples section of the file ../ClassParser_v4/README.md .

## Known issues
1. Return an empty list when try to list all members which its type is a function or a method.
   It also occurs at 4th version, or exactly to say, I have NOT finished these parts -- for the method or function.
   
   See Example 3. 
## Release Notes
### 2023/09/14 15:17 
Initial Notes
### 2023/09/14 15:27
#### Added
1. Known issue section

I have found a known issue which also occurs at 4th version.

So I add it to known issue.

