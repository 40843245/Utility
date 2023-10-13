# DoWhile.py (1th version)
## Objective
1. Emulate do-while loop.

## API
I don't wrap it into class. Instead, I just write a function.
### def DoWhile()

I emulate it with while loop.
Syntax :
    
    DoWhile(func,exprs,endExpr,list1 ,*args,**kwargs):
    
Parameter :
1. Cond : A condition to determine the loop will exit or not. 
2. Expr : An expression that is executed every time the loop will continue. 
3. EndExpr : An expression that is executed only after the loop exits.
4. list1 : A list that each elem is executed for execution of Expr.
5. args :   A tuple that each elem is executed for execution of Expr.
6. kwargs :  A dict that each elem in keys of the dict is executed for execution of Expr.
   
Returned Value :

list1

####
