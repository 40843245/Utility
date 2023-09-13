# ClassInheriter (Find Inherited class for the class) (1th version)
## Objectives
    1. Find Inherited class for the class
## Examples
### Example 1
#### Class
Base Class:
    
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

Derived Class:
    
    class DerivedClass(TestClass):
        def DerivedFunc1():
            print("DerivedFunc1!!!")
        def DerivedFunc2():
            print("DerivedFunc2!!!")
#### Input
    r = ClassInheriter.GetInheritedClass(TestClass)
    print(r)
    r = ClassInheriter.GetInheritedClass(DerivedClass)
    print(r)
#### Output
    [<class '__main__.DerivedClass'>]
    []
## Ref
https://stackoverflow.com/questions/3048337/python-subclasses-not-listing-subclasses

## Release Notes
### 2023/09/14 7:18 
Initial Notes

