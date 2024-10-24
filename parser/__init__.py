import ply.yacc as yacc
import readline

# Get the token map from the lexer.  This is required.
from tokenizer import tokens

class Node:
    def __init__(self, type, value, children=[]):
        self.type = type
        self.value = value
        self.children = children

def p_expression_or_float_exp(p):
    """x_expression : f_exp
                 | expression"""
    p[0] = Node('x_expression', '', [p[1]])

def p_float_exp_plus(p):
    """f_exp : f_exp PLUS f_term"""
    p[0] = Node('f_exp', '+', [p[1], p[3]])

def p_float_exp_minus(p):
    'f_exp : f_exp MINUS f_term'
    p[0] = Node('f_exp', '-', [p[1], p[3]])

def p_float_exp_term(p):
    'f_exp : f_term'
    p[0] = Node('f_exp', '', [p[1]])

def p_float_term_times(p):
    'f_term : f_term TIMES f_factor'
    p[0] = Node('f_term', '*', [p[1], p[3]])

def p_float_term_div(p):
    'f_term : f_term DIVIDE f_factor'
    p[0] = Node('f_term', '/', [p[1], p[3]])

def p_float_term_float_factor(p):
    'f_term : f_factor'
    p[0] = Node('f_term', '', [p[1]])

def p_factor_float(p):
    'f_factor : FLOAT'
    p[0] = Node('f_factor', p[1], [])

def p_factor_f_expr(p):
    'f_factor : LPAREN f_exp RPAREN'
    p[0] = Node('f_factor', '', [p[2]])

def p_expression_plus(p):
    """expression : expression PLUS term"""
    p[0] = Node('expression', '+', [p[1], p[3]])

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = Node('expression', '-', [p[1], p[3]])

def p_expression_term(p):
    'expression : term'
    p[0] = Node('expression', '', [p[1]])

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = Node('term', '*', [p[1], p[3]])

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = Node('term', '/', [p[1], p[3]])

def p_term_factor(p):
    'term : factor'
    p[0] = Node('term', '', [p[1]])

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = Node('factor', p[1], [])

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = Node('factor', '', [p[2]])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

def pretty_print(node, indent=0):
    print('  '* indent + node.type + ':'+ str(node.value))
    for child in node.children:
        pretty_print(child, indent+1)


while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   pretty_print(parser.parse(s))
