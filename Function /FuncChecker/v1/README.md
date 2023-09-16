# FuncChecker (Check a var is a func ) (1th version)
## Objectives
    Check a var is either 
    1. a function which is implemented by C.
    2. a function which is implemented by Python.
    3. or both.
## Introduction 
A simple class implemented in Python which can check a var is a function.
## API

IsFunc : 
Check func is a function that is implemented by C or Python.

    @staticmethod
    def IsFunc( 
                func
        ) -> bool :

IsCFunc : 
Check func is a function that is implemented by Python.

    @staticmethod
    def IsCFunc( 
            func
    ) -> bool :
    
IsPythonFunc : 
Check func is a function that is implemented by Python.

    @staticmethod
    def IsPythonFunc( 
            func
    ) -> bool :
     



## NOTICE
    only available on >= Python 3.2
    For more details, see the reply answered by John Feminella
    https://stackoverflow.com/questions/624926/how-do-i-detect-whether-a-variable-is-a-function
## Examples
### Example 1
#### Code
    def TestFunc1():
            return 1
        def FuncInfo(
                func
            ):
            no = " NOT "
            msg = ( str(func) + " is "+ no +"a func." ) if FuncChecker.IsFunc(func) == False else ( str(func) + " is a func.")
            return msg
        
        x = 2
        y = TestFunc1()
        dir1 = dir(3)
        none = None
        list1 = list()
        tuple1 = tuple()
        dict1 = dict()
        callable1 = callable
        testList = [ 
            lambda a : a + 2 ,
            TestFunc1,
            x,
            y,
            dir1,
            none,
            list1,
            tuple1,
            dict1,
            callable1
        ]
     
        resultList = [ FuncInfo(arg) for arg in testList ]
        print(resultList)

#### Output
    ['<function <lambda> at 0x000001C44F2E9580> is a func.', '<function TestFunc1 at 0x000001C44F18C540> is a func.', '2 is  NOT a func.', '1 is  NOT a func.', "['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes'] is  NOT a func.", 'None is  NOT a func.', '[] is  NOT a func.', '() is  NOT a func.', '{} is  NOT a func.', '<built-in function callable> is a func.']

## Used Module
    types
    
## Release Notes
### 2023/09/16 17:04 
initial notes.
