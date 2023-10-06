class NumberSplitter2():
    def __init__(self):
        self.Clear()
    def Clear(self):
        self.dynamicTable = dict()
        self.result = None
    def Build(self,number : int):
        self.Clear()
        self.dynamicTable['1'] = 1
        self.dynamicTable['2'] = 1
        self.dynamicTable['3'] = 2
        self.dynamicTable['4'] = 4
        for i in range(5,number, 1):
            largestNumber = -1 
            counter = 2
            while counter < i :
                number1 = counter 
                number2 = i - counter 
                tempNumber = number1 * number2 
                if tempNumber > largestNumber:
                    largestNumber = tempNumber
                counter += 1
            self.dynamicTable[str(i)] = largestNumber
    def GetProduct(self,numbers : list [int] ):
        result = 1
        for i in range(0,len(numbers),1):
            result *= numbers [i]
        return result
    def GetMaxProductOfSplitSum(self,number:int):
        return self.dynamicTable[str(number)]
class NumberSplitter3():
    @staticmethod
    def GetMaxProductOfSplitSum(number:int):
        if number in [1]:
            return number
        return ( number // 2 ) * ( number // 2 + 1)
if __name__ == '__main__':
    
    number = 200
    numberSplitter2 = NumberSplitter2()
    numberSplitter2.Build(number)
    rList = [ numberSplitter2.GetMaxProductOfSplitSum(elem) for elem in range(1,number,1)  ] 
    print(rList)
    rList = [ NumberSplitter3.GetMaxProductOfSplitSum(elem) for elem in range(1,number,1)  ] 
    print(rList)
