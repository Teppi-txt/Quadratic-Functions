import matplotlib
import sympy

#factorization function using sympy.
def factorize(string_eq):
    #converting stringed equation to equation.
    equation = sympy.parse_expr(string_eq)
    return sympy.factor(equation)

#expansion method.
def expansion(string_eq):
    #converting stringed equation to equation.
    equation = sympy.parse_expr(string_eq)
    #returns expanded equation
    return sympy.expand(equation)
