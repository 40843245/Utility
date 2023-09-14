from ClassParser import ClassFuncParser , ClassModeEnum , RecursiveModeEnum , ClassFuncFinder

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

if __name__ == '__main__':
    r = ClassFuncParser.GetMemberTree(target = "TestClass.a", availables = globals(), searchMode = RecursiveModeEnum.NONRECURSIVE_ALL)
    print("result:")
    print(r)
