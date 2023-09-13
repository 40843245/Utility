class ClassInheriter:
    @staticmethod
    def GetInheritedClass(
            class1
    ):
        return class1.__subclasses__()

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

class DerivedClass(TestClass):
    def DerivedFunc1():
        print("DerivedFunc1!!!")
    def DerivedFunc2():
        print("DerivedFunc2!!!")
    
if __name__ == '__main__':
    r = ClassInheriter.GetInheritedClass(TestClass)
    print(r)
    r = ClassInheriter.GetInheritedClass(DerivedClass)
    print(r)

