from context_i import Context
from lexer_i import *
from parser_i import *
from symbol_table_i import *
from Interpreter_i import *
import values_i 

###########################################
# RUN
###########################################

global_symbol_table = SymbolTable()
global_symbol_table.set("NoC", [Number.null, 'Null'])
global_symbol_table.set("None", [Number.none, 'None'])
global_symbol_table.set("TRUE", [Number.true, 'True'])
global_symbol_table.set("FALSE", [Number.false, 'False'])
global_symbol_table.set("PI", Number.math_PI)
global_symbol_table.set("OUT", BuiltInFunction.printout)
global_symbol_table.set("RUT", BuiltInFunction.printreturn)
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
global_symbol_table.set("CLEAN", BuiltInFunction.clean)
global_symbol_table.set("GLOB_ATTR", BuiltInFunction.global_attributes)

def run(fn, text):

    #Generate tokens

    lexer = Lexer(fn, text)
    tokens, ProgData, error = lexer.make_tokens()
    # print(tokens)
    if error: return None, error

    # Generate Abstract Syntax Tree
    parser = Parser(tokens)
    ast = parser.parse()
    #print(ast.node)
    
    if ast.error: return None, ast.error

    #Run program
    interpreter = Interpreter(tokens, ProgData, global_symbol_table)
    context = Context('<shell>')
    context.symbol_table = global_symbol_table
    result = interpreter.visit(ast.node, context)

    #print(dir(result))

    try:
        if type(result.value) == values_i.List:
            #print(result, result.value, result.value.elements)
            #print(type(result.value.elements), result.value.elements)
            for i in result.value.elements:
                #print(i, 1)
                if str(i) == "null":
                    a = [1, 2]
                    #print(1, i, type(i))
                    ind = result.value.elements.index(i)
                    #print(ind)
                    del result.value.elements[ind]
    except:
        pass
    
    return result.value, result.error
