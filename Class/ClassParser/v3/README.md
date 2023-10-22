# ClassParser.py ( 3th version of ClassParser )
## Examples
### Example1 
#### Input Class

    class TestClass:
        def Hello():
            def HelloWorld():
                print("HelloWorld!!!")
            print("Hello!!!")
        def Sound():
            class Animal:
                class Dog:
                    def Bark():
                        print("Bark!!!")
                class Cat:
                    def Mow():
                        print("Mow!!!")
            print("Sound!!!")
        class a:
            def a1_func1():
                print("a1_func1!!!")
            class a1_1:
                def a1_1_func1():
                    print("a1_1_func1!!!")
                @staticmethod
                def a1_1_func2():
                    print("a1_1_func2!!!")

### Arguemt

        r = ClassFuncParser.GetMemberTree( 
                                    target = "TestClass" , 
                                    availables = globals(),
                                    searchMode = RecursiveModeEnum.VISIT_DEPTH_1
                                  )
### Output
It looks like this.

      [['Hello', 'function', []], ['Sound', 'function', []], ['a', 'class', []], ['a1_1', 'class', []], ['a1_1_func1', 'function', []], ['a1_1_func2', 'function', []], ['a1_func1', 'function', []]]

## Change
### Fix 
1. The searchMode = RecursiveModeEnum.VISIT_DEPTH_1 ( it is shown in the 2th point in known issues list in file ../ClassParser/README.md ).

## Release Notes
### 2023/09/13 12:11 
