class NumberSplitter():
    def __init__(self):
        self.Clear()
    """
    Intro:
    Given a positive integer n, get the maximum among these product numbers which sum of each element is equal to n.
    Examples:
    Example 1:
    Input:
        5
    Output:
        6
    """
    def Build(self,number:int):
        if number <= 0 :
            raise Exception("It must be a positive integer in method call GetMaxProductOfSumDigit.")
        self.Clear()
        # fill out dummy index 0
        self.dynamicTable.append(1)
        self.resultTable.append(1)
        # fill the result directly.
        self.dynamicTable.append(1)
        self.resultTable.append(1)
        
        self.dynamicTable.append(2)
        self.resultTable.append(1)
        
        self.dynamicTable.append(3)
        self.resultTable.append(2)
        
        # calculating ...
        for n in range(4,number,1):
            tempProduct = 1
            maxProduct = -1
            for j in range(1,n,1):
                tempProduct = self.dynamicTable[j] * self.dynamicTable[n-j]
                # Update max product number
                if tempProduct > maxProduct :
                    maxProduct = tempProduct
            maxProduct = max(maxProduct,n)
            self.dynamicTable.append(maxProduct)        
            self.resultTable.append(maxProduct)
    """
    Clear all attrs.
    """
    def Clear(self):
        # Just a table to store the result while processing. DO NOT access it to get answer.
        self.dynamicTable = list()
        # Resultant table. Use it to get answer. 
        self.resultTable = list()

if __name__ == '__main__':
    MAX_NUMBER = 100
    
    handler = NumberSplitter()    
    handler.Build(MAX_NUMBER)
    
    for i in range(1,MAX_NUMBER,1):      
        r = handler.resultTable[i]
        print("The max product of elem whose sum of elem is equal to "+str(i)+" is " + str(r))
    
