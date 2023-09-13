import sys
import inspect
import types

def OtherTestFunc1():
    return 1

def OtherTestFunc2():
    return 2

class LocalModuleFinder:
    @staticmethod
    def IsFunctionLocal(object):
        return isinstance(object, types.FunctionType) and object.__module__ == __name__
    @staticmethod
    def IsClassLocal(object):
        return isinstance(object, types.ClassMethodDescriptorType) and object.__module__ == __name__
    @staticmethod
    def GetLocalModules():
        return inspect.getmembers(sys.modules[__name__], predicate=LocalModuleFinder.IsFunctionLocal)
