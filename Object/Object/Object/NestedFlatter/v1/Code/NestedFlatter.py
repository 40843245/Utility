import numpy as np
class NestedFlatter():
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
        The input nested array-like object should be satisfy all requirements:
            1. all subarray should have homogeneous shape (i.e. have same length).
        Otherwise, the error will be raised.
        For more details, see the following examples.
    Example : 
        Okay Examples (Examples without errors).
        Example 1 :
            [ [1,2,3] ,['a','b','c']]
        Erroreous Examples (Examples with errors).
        Example 2 (Due to inhomogeneous shape):
            [ [1,2,3] ,['a','b','c'] , ['q','w','e']]
    """
    @staticmethod
    def Flat(items : ( list | tuple ) ) -> ( list | tuple ) :
        arr = np.array(items)
        flatted = np.reshape(arr, -1)
        return flatted
    
if __name__ == '__main__':
    items = [ [1,2,3] ,['a','b','c']]
    r = NestedFlatter.Flat(items)
    print(r)
