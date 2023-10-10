class ObjectHandler():
    @staticmethod
    def flatten(x):
        result = []
        for el in x:
            if hasattr(el, "__iter__") and isinstance(el, (list,tuple)):
                result.extend(ObjectHandler.flatten(el))
            else:
                result.append(el)
        return result
if __name__ == '__main__':
    array1 = [ 1,8,9,[2,4] ]
    array2 = ObjectHandler.flatten(array1)
    print(array2)
    r = sum(array2)
    print(r)
    
    array1 = ( 1,8,9,(2,4) )
    array2 = ObjectHandler.flatten(array1)
    print(array2)
    r = sum(array2)
    print(r)
    
    array1 = [ 1,8,9,(2,4) ] 
    array2 = ObjectHandler.flatten(array1)
    print(array2)
    r = sum(array2)
    print(r)
    
    array1 = ( 1,8,9,[2,4] )
    array2 = ObjectHandler.flatten(array1)
    print(array2)
    r = sum(array2)
    print(r)
