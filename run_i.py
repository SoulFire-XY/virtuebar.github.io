from context_i import Context
from lexer_i import *
from parser_i import *
from symbol_table_i import *
from Interpreter_i import *

###########################################
# RUN
###########################################

global_symbol_table = SymbolTable()
global_symbol_table.set("NoC", (Number(0), 'Null'))

def run(fn, text):

    #Generate tokens
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()

    if error: return None, error

    # Generate Abstract Syntax Tree
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error: return None, ast.error
    print(ast._type)

    #Run program
    interpreter = Interpreter()
    context = Context('<shell>')
    context.symbol_table = global_symbol_table
    result = interpreter.visit(ast.node, context, ast._type)

    return result.value, result.error