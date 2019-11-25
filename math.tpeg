example Expr (1+2)*3
example Expr 1+2*3
Expr = { Prod '+' Prod #Add } / Prod
Prod = { Value '*' Value #Mul } / Value
Value = { DIGIT+ #Int } / '(' Expr ')' 
DIGIT = [0-9]