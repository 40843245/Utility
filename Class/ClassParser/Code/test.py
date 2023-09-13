from ClassParser import ClassFuncParser , ClassModeEnum , RecursiveModeEnum

class TestClass:
    def Hello():
        print("Hello!!!")
    def Bark():
        print("Bark!!!")
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
    r = ClassFuncParser.GetMemberTree( 
                                    target = "TestClass" , 
                                    availables = globals(),
                                    searchMode = RecursiveModeEnum.NONRECURSIVE_ALL ,
                                    result = None , 
                                    firstTime = True
                                  )
    print("result:")
    print(r)
