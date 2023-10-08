class ElemHandler():
    @staticmethod
    def HasSameElem( elems : (list|tuple)):
        if len(elems) <= 0 :
            return False
        set1 = set(elems)
        return len(set1) < len(elems)
        
if __name__ == '__main__':
    elems = [1,2,3,4,5]
    r = ElemHandler.HasSameElem(elems)
    print(r)
    
    elems = [1,2,3,4,4]
    r = ElemHandler.HasSameElem(elems)
    print(r)
    
    elems = [1,1,2]
    r = ElemHandler.HasSameElem(elems)
    print(r)
    
    elems = []
    r = ElemHandler.HasSameElem(elems)
    print(r)
    
    elems = (1,2)
    r = ElemHandler.HasSameElem(elems)
    print(r)
    
    elems = (2,2)
    r = ElemHandler.HasSameElem(elems)
    print(r)
    
    elems = tuple()
    r = ElemHandler.HasSameElem(elems)
    print(r)
    
