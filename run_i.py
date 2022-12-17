from context_i import Context
from lexer_i import *
from parser_i import *
from symbol_table_i import *
from Interpreter_i import *
from values_i import *

###########################################
# RUN
###########################################

global_symbol_table = SymbolTable()
global_symbol_table.set("NoC", [Number.null, 'Null'])
global_symbol_table.set("TRUE", [Number.true, 'True'])
global_symbol_table.set("FALSE", [Number.false, 'False'])
global_symbol_table.set("PI", Number.math_PI)
global_symbol_table.set("POUT", BuiltInFunction.printout)
global_symbol_table.set("PRET", BuiltInFunction.printreturn)
global_symbol_table.set("TIN", BuiltInFunction.typein)
global_symbol_table.set("TIN_INT", BuiltInFunction.typein_int)
global_symbol_table.set("CLEAR", BuiltInFunction.clear)
global_symbol_table.set("CLS", BuiltInFunction.clear)
global_symbol_table.set("IS_NUM", BuiltInFunction.is_number)
global_symbol_table.set("IS_STR", BuiltInFunction.is_string)
global_symbol_table.set("IS_LIST", BuiltInFunction.is_list)
global_symbol_table.set("IS_FUNC", BuiltInFunction.is_function)
global_symbol_table.set("APPEND", BuiltInFunction.append)
global_symbol_table.set("POP", BuiltInFunction.pop)
global_symbol_table.set("EXTEND", BuiltInFunction.extend)
global_symbol_table.set("FLOOR", BuiltInFunction.floor)
global_symbol_table.set("CEIL", BuiltInFunction.ceil)
global_symbol_table.set("SQRE", BuiltInFunction.square)
global_symbol_table.set("CUBE", BuiltInFunction.cube)
global_symbol_table.set("TESS", BuiltInFunction.tessaract)
global_symbol_table.set("ADD", BuiltInFunction.add)
global_symbol_table.set("SUB", BuiltInFunction.subt)
global_symbol_table.set("MUL", BuiltInFunction.mult)
global_symbol_table.set("DIV", BuiltInFunction.divi)
global_symbol_table.set("SQRT", BuiltInFunction.sqrt)
global_symbol_table.set("CBRT", BuiltInFunction.cbrt)
global_symbol_table.set("RANINT", BuiltInFunction.ranint)
global_symbol_table.set("RANGE", BuiltInFunction.range)
global_symbol_table.set("RUN", BuiltInFunction.run)
global_symbol_table.set("LEN", BuiltInFunction.len)
global_symbol_table.set("MAP", BuiltInFunction.map)
global_symbol_table.set("JOIN", BuiltInFunction.join)

def run(fn, text):

    #Generate tokens
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()

    if error: return None, error

    # Generate Abstract Syntax Tree
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error: return None, ast.error

    #Run program
    interpreter = Interpreter()
    context = Context('<shell>')
    context.symbol_table = global_symbol_table
    result = interpreter.visit(ast.node, context)

    if type(result.value) == List:
        if 'null' in result.value.elements:
            while 'null' in result.value.elements:
                result.value.remove('null')
    
    return result.value, result.error
