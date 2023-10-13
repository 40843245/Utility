import functools
def DoWhile(func,exprs,endExpr,list1 ,*args,**kwargs):
    lambdaFunc = functools.partial(func,list1,args,kwargs)
    while lambdaFunc() :
        lambdaExpr = functools.partial(exprs,list1,args,kwargs)
        list1 = lambdaExpr()
        lambdaFunc = functools.partial(func,list1,args,kwargs)
    list1 = endExpr()
    return list1
def Cond(obj,*args,**kwargs):
    print("obj:"+str(obj)) 
    list1 = [ elem < 10 for elem in obj]
    r = any(list1)
    print("obj<10?"+str(r))
    return  r
def Expr(obj,*args,**kwargs):
    print("obj:"+str(obj))
    list1 = [ elem + 1  for elem in obj]
    print("obj+1:"+str(list1))
    return list1
def EndExpr():
    print("EndExpr")
    
if __name__ == '__main__' :
    list1 = [1]
    args = []
    kwargs = []
    DoWhile(Cond,Expr,EndExpr,list1,args,kwargs)
