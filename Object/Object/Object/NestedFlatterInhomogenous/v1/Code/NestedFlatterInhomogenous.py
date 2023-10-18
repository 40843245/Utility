class NestedFlatterInhomogenous():
    """
    Intro :
        A function that flats a nested array-like object to 1D array-like object. 
        For more details of returned value and returned type, see the following sections.
    Parameter :
        items : nested array-like object that be flatted.
    Returned Value:
        It returns an array-like object after flattening. 
    Returned Type:
        The type of returned value is same as type of input nested array-like object.
        i.e.
        1D list if input is nested list.
        1D tuple if input is nested tuple.
    NOTICE :
        NOTICE that 
        The input nested array-like object can be inhomogenous (i.e. with different shape.)
        (rather than NestedFlatter class in NestedFlatter.py file, which can only handle homogenous (i.e. with same shape) of nested array-like object.)
        For more details, see the following examples.
    Example : 
        Example 1 :
            ( (1,2,3) ,('a','b','c' ) )
        Example 2 :
            ( ( (1,2,3) ,('a','b','c' ) ) , ('q','w','e'))
    """
    @staticmethod
    def Flat(items : ( list | tuple ) ) -> ( list | tuple ) :
        result = NestedFlatterInhomogenous.Flat_SubUtility(items)
        if isinstance(items, tuple) == True:
            result = tuple(result)
        return result
     
    @staticmethod
    def Flat_SubUtility(items : ( list | tuple ) ) -> ( list | tuple ) :
        temp = list()
        for i in range(0,len(items),1):
            item = items[i]
            if item != None:
                if isinstance(item, (tuple,list)) == True:
                    elem = NestedFlatterInhomogenous.Flat_SubUtility(item)
                    temp = elem + temp
                else:
                    temp.append(item)
        return temp
if __name__ == '__main__':
    items = ( (1,2,3) ,('a','b','c' ) )
    r = NestedFlatterInhomogenous.Flat(items)
    print(r)
    
    items = ( ( (1,2,3) ,('a','b','c' ) ) , ('q','w','e'))
    r = NestedFlatterInhomogenous.Flat(items)
    print(r)
