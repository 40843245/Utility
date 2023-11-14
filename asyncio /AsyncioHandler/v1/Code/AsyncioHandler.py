import asyncio

class AsyncioHandler():
    @staticmethod
    def IsAsyncFunction(func):
        return asyncio.iscoroutinefunction(func)

async def Func1():
    return 1

def Func2():
    return 0

class DemoClass1():
    async def Func1_1():
        return -1
    def Func1_2():
        return -1
    
class DemoClass2():
    async def Func2_1():
        return -1
    def Func2_2():
        return -1
    def Func2_3():
        def Func2_3_1():
            return -1
        return Func2_3_1
    def Func2_4():
        async def Func2_4_1():
            return -1
        return Func2_4_1
    async def Func2_5():
        def Func2_5_1():
            return -1
        return Func2_5_1
    
    async def Func2_6():
        def Func2_6_1():
            return -1
        return Func2_6_1
    
if __name__ == '__main__':
    testDatas = [
        Func1,
        Func2,
        DemoClass1.Func1_1,
        DemoClass1.Func1_2,
        DemoClass2.Func2_1,
        DemoClass2.Func2_2,
        DemoClass2.Func2_3,
        DemoClass2.Func2_4,
        DemoClass2.Func2_5,
        DemoClass2.Func2_6,
    ]
    for ith in range(0,len(testDatas)):
        testData = testDatas[ith]
        r = AsyncioHandler.IsAsyncFunction(testData)
        print("ith:%d" % (ith) )
        print("r:")
        print(r)
    
