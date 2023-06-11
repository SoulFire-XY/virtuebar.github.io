###########################################
# VALUES
###########################################

import math
from runtime_result_i import *
from Interpreter_i import *
from context_i import *
from symbol_table_i import *
import os
from error_i import *
import random

class Value:
	def __init__(self):
		self.set_pos()
		self.set_context()

	def set_pos(self, pos_start=None, pos_end=None):
		self.pos_start = pos_start
		self.pos_end = pos_end
		return self

	def set_context(self, context=None):
		self.context = context
		return self

	def added_to(self, other):
		return None, self.illegal_operation(other)

	def subbed_by(self, other):
		return None, self.illegal_operation(other)

	def multed_by(self, other):
		return None, self.illegal_operation(other)

	def dived_by(self, other):
		return None, self.illegal_operation(other)

	def powed_by(self, other):
		return None, self.illegal_operation(other)

	def get_comparison_eq(self, other):
		return None, self.illegal_operation(other)

	def get_comparison_ne(self, other):
		return None, self.illegal_operation(other)

	def get_comparison_lt(self, other):
		return None, self.illegal_operation(other)

	def get_comparison_gt(self, other):
		return None, self.illegal_operation(other)

	def get_comparison_lte(self, other):
		return None, self.illegal_operation(other)

	def get_comparison_gte(self, other):
		return None, self.illegal_operation(other)

	def withed_by(self, other):
		return None, self.illegal_operation(other)

	def ored_by(self, other):
		return None, self.illegal_operation(other)

	def inverted(self, other):
		return None, self.illegal_operation(other)

	def execute(self, args, no_value):
		return RTResult().failure(self.illegal_operation())

	def copy(self):
		raise Exception('No copy method defined')

	def is_true(self):
		return False

	def illegal_operation(self, other=None):
		if not other: other = self
		return RunTimeError(
			self.pos_start, other.pos_end,
			'Illegal operation',
			self.context
		)

class Number(Value):
	def __init__(self, value):
		super().__init__()
		self.value = value

	def added_to(self, other):
		if isinstance(other, Number):
			return Number(self.value + other.value).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def subbed_by(self, other):
		if isinstance(other, Number):
			return Number(self.value - other.value).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def multed_by(self, other):
		if isinstance(other, Number):
			return Number(self.value * other.value).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def dived_by(self, other):
		if isinstance(other, Number):
			if other.value == 0:
				return None, RunTimeError(
					other.pos_start, other.pos_end,
					'Division by zero',
					self.context
				)

			return Number(self.value / other.value).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def powed_by(self, other):
		if isinstance(other, Number):
			return Number(self.value ** other.value).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def get_comparison_eq(self, other):
		if isinstance(other, Number):
			return Number(int(self.value == other.value)).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def get_comparison_ne(self, other):
		if isinstance(other, Number):
			return Number(int(self.value != other.value)).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def get_comparison_lt(self, other):
		if isinstance(other, Number):
			return Number(int(self.value < other.value)).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def get_comparison_gt(self, other):
		if isinstance(other, Number):
			return Number(int(self.value > other.value)).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def get_comparison_lte(self, other):
		if isinstance(other, Number):
			return Number(int(self.value <= other.value)).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def get_comparison_gte(self, other):
		if isinstance(other, Number):
			return Number(int(self.value >= other.value)).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def withed_by(self, other):
		if isinstance(other, Number):
			return Number(int(self.value and other.value)).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def ored_by(self, other):
		if isinstance(other, Number):
			return Number(int(self.value or other.value)).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def inverted(self):
		return Number(1 if self.value == 0 else 0).set_context(self.context), None

	def copy(self):
		copy = Number(self.value)
		copy.set_pos(self.pos_start, self.pos_end)
		copy.set_context(self.context)
		return copy
	
	def get_value(self):
		return self.value

	def is_true(self):
		return self.value != 0

	def __str__(self):
		return str(self.value)

	def __repr__(self):
		return str(self.value)

class List(Value):
	'''List Value Type'''
	def __init__(self, elements):
		super().__init__()
		self.elements = elements

	def added_to(self, other):
		new_list = self.copy()
		new_list.elements.append(other)
		return new_list, None

	def subbed_by(self, other):
		if isinstance(other, Number):
			new_list = self.copy()
			try:
				new_list.elements.pop(other.value)
				return new_list, None
			except:
				return None, RunTimeError(
				other.pos_start, other.pos_end,
				'Element at this index could not be removed from list because index is out of bounds',
				self.context
				)
		else:
			return None, Value.illegal_operation(self, other)

	def multed_by(self, other):
		if isinstance(other, List):
			new_list = self.copy()
			new_list.elements.extend(other.elements)
			return new_list, None
		else:
			return None, Value.illegal_operation(self, other)

	def get_item(self, other):
		if isinstance(other, Number):
			try:
				return self.elements[other.value], None
			except:
				return None, RunTimeError(
				other.pos_start, other.pos_end,
				'Element at this index could not be retrieved from list because index is out of bounds',
				self.context
			)
		else:
			return None, Value.illegal_operation(self, other)
  
	def copy(self):
		copy = List(self.elements)
		copy.set_pos(self.pos_start, self.pos_end)
		copy.set_context(self.context)
		return copy

	def __str__(self):
		return ", ".join([str(x) for x in self.elements])
	
	def __repr__(self):
		return f'[{", ".join([repr(x) for x in self.elements])}]'

class BaseFunction(Value):
	'''Base Function Value Type'''
	def __init__(self, name):
		super().__init__()
		self.name = name or "<anonymous>"

	def generate_new_context(self):
		new_context = Context(self.name, self.context, self.pos_start)
		new_context.symbol_table = SymbolTable(new_context.parent.symbol_table)
		return new_context

	def check_args(self, arg_names, args):
		res = RTResult()

		if len(args) > len(arg_names):
			return res.failure(RunTimeError(
			self.pos_start, self.pos_end,
        f"{len(args) - len(arg_names)} too many args passed into {self}",
        self.context
      	))
    
		if len(args) < len(arg_names):
			return res.failure(RunTimeError(
			self.pos_start, self.pos_end,
			f"{len(arg_names) - len(args)} too few args passed into {self}",self.context ))

		return res.success(None)

	def populate_args(self, arg_names, args, exec_ctx):
		for i in range(len(args)):
			arg_name = arg_names[i]
			arg_value = args[i]
			arg_value.set_context(exec_ctx)
			exec_ctx.symbol_table.set(arg_name, arg_value)

	def check_and_populate_args(self, arg_names, args, exec_ctx):
		res = RTResult()
		res.register(self.check_args(arg_names, args))
		if res.should_return(): return res
		self.populate_args(arg_names, args, exec_ctx)
		return res.success(None)

class Function(BaseFunction):
	'''Function Value Type'''
	def __init__(self, name, body_node, arg_names, auto_return):
		super().__init__(name)
		self.body_node = body_node
		self.arg_names = arg_names
		self.auto_return = auto_return

	def execute(self, args, Interpreter):
		res = RTResult()
		interpreter = Interpreter()
		exec_ctx = self.generate_new_context()

		res.register(self.check_and_populate_args(self.arg_names, args, exec_ctx))
		if res.should_return(): return res

		value = res.register(interpreter.visit(self.body_node, exec_ctx))
		if res.should_return() and res.func_value_return == None: return res

		return_value = (value if self.auto_return else None) or res.func_value_return or Number.null
		return res.success(return_value)

	def copy(self):
		copy = Function(self.name, self.body_node, self.arg_names, self.auto_return)
		copy.set_context(self.context)
		copy.set_pos(self.pos_start, self.pos_end)
		return copy

	def __repr__(self):
		return f"<function {self.name}>"

class String(Value):
	def __init__(self, value):
		super().__init__()
		self.value = value

	def added_to(self, other):
		if isinstance(other, String):
			return String(self.value + other.value).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def multed_by(self, other):
		if isinstance(other, Number):
			return String(self.value * other.value).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def is_true(self):
		return len(self.value) > 0

	def len_str(self):
		return len(self.value)

	def copy(self):
		copy = String(self.value)
		copy.set_pos(self.pos_start, self.pos_end)
		copy.set_context(self.context)
		return copy

	def __str__(self):
		return self.value

	def __repr__(self):
		return f'"{self.value}"'

###################################################################################
# GLOBAL CONSTANTS
###################################################################################
Number.null = String("null")
Number.none = String(None)
Number.false = Number(0)
Number.true = Number(1)
Number.math_PI = Number(math.pi)
###################################################################################s

class BuiltInFunction(BaseFunction):
	def __init__(self, name):
		super().__init__(name)

	def execute(self, args, no_value):
		res = RTResult()
		exec_ctx = self.generate_new_context()

		method_name = f'execute_{self.name}'
		method = getattr(self, method_name, self.no_visit_method)

		res.register(self.check_and_populate_args(method.arg_names, args, exec_ctx))
		if res.should_return(): return res

		return_value = res.register(method(exec_ctx))
		if res.should_return(): return res
		return res.success(return_value)

	def no_visit_method(self, node, context):
		raise Exception(f'No execute_{self.name} method defined')

	def copy(self):
		copy = BuiltInFunction(self.name)
		copy.set_context(self.context)
		copy.set_pos(self.pos_start, self.pos_end)
		return copy

	def __repr__(self):
		return f"<built-in function {self.name}>"

	#################################################################################################

############################### I/O SYSTEM ###############################
	def execute_printout(self, exec_ctx):
		print(str(exec_ctx.symbol_table.get('value')))
		return RTResult().success(Number.none)
	execute_printout.arg_names = ["value"]

	def execute_printreturn(self, exec_ctx):
		statement = String(str(exec_ctx.symbol_table.get('value')))
		return RTResult().success(statement)
	execute_printreturn.arg_names = ["value"]

	def execute_typein(self, exec_ctx):
		text = input()
		return RTResult().success(String(text))
	execute_typein.arg_names = []

	def execute_typein_int(self, exec_ctx):
		while True:
			text = input()
			try:
				number = int(text)
				break
			except ValueError:
				print(f"'{text}' must be an integer. Try again!")
		return RTResult().success(Number(number))
	execute_typein_int.arg_names = []

	def execute_clear(self, exec_ctx):
		os.system('cls' if os.name == 'nt' else 'clear')
		return RTResult().success(Number.none)
	execute_clear.arg_names = []

	def execute_is_number(self, exec_ctx):
		is_number = isinstance(exec_ctx.symbol_table.get("value"), Number)
		return RTResult().success(Number.true if is_number else Number.false)
	execute_is_number.arg_names = ['value']
		
	def execute_is_string(self, exec_ctx):
		is_string = isinstance(exec_ctx.symbol_table.get("value"), String)
		return RTResult().success(Number.true if is_string else Number.false)
	execute_is_string.arg_names = ['value']
		
	def execute_is_list(self, exec_ctx):
		is_list = isinstance(exec_ctx.symbol_table.get("value"), List)
		return RTResult().success(Number.true if is_list else Number.false)
	execute_is_list.arg_names = ['value']
		
	def execute_is_function(self, exec_ctx):
		is_function = isinstance(exec_ctx.symbol_table.get("value"), BaseFunction)
		return RTResult().success(Number.true if is_function else Number.false)
	execute_is_function.arg_names = ['value']

	def execute_clean(self, exec_ctx):
		item = exec_ctx.symbol_table.get("item")
		exec_ctx.symbol_table.remove(item)
		del item
		return RTResult().success(Number.none)
	
	execute_clean.arg_names = ['item']

############################### List Operations ###############################

	def execute_len(self, exec_ctx):
		value = exec_ctx.symbol_table.get("list")
		
		if not (isinstance(value, List) or isinstance(value, String)):
			return RTResult().failure(RunTimeError(
				self.pos_start, self.pos_end,
				"Argument must be a list or string",
				exec_ctx
			))
		if isinstance(value, List):
			return RTResult().success(Number(len(value.elements)))
		elif isinstance(value, String):
			return RTResult().success(Number(len(str(value))))
	execute_len.arg_names = ['list']

	def execute_append(self, exec_ctx):
		list_ = exec_ctx.symbol_table.get("list")
		value = exec_ctx.symbol_table.get("value")

		if not isinstance(list_, List):
			return RTResult().failure(RunTimeError(
				self.pos_start, self.pos_end,
				"First argument must be a list",
				exec_ctx
			))

		list_.elements.append(value)
		return RTResult().success(Number.none)
	execute_append.arg_names = ['list', 'value']

	def execute_pop(self, exec_ctx):
		list_ = exec_ctx.symbol_table.get("list")
		index = exec_ctx.symbol_table.get("index")

		if not isinstance(list_, List):
			return RTResult().failure(RunTimeError(
        		self.pos_start, self.pos_end,
        		"First argument must be list",
        		exec_ctx
      	))

		if not isinstance(index, Number):
			return RTResult().failure(RunTimeError(
				self.pos_start, self.pos_end,
				"Second argument must be number",
				exec_ctx
			))

		try:
			element = list_.elements.pop(index.value)
		except:
			return RTResult().failure(RunTimeError(
			self.pos_start, self.pos_end,
			'Element at this index could not be removed from list because index is out of bounds',
			exec_ctx
		))

		return RTResult().success(element)
	execute_pop.arg_names = ['list', 'index']

	def execute_extend(self, exec_ctx):
		listA = exec_ctx.symbol_table.get("listA")
		listB = exec_ctx.symbol_table.get("listB")

		if not isinstance(listA, List):
			return RTResult().failure(RunTimeError(
			self.pos_start, self.pos_end,
			"First argument must be list",
			exec_ctx
		))

		if not isinstance(listB, List):
			return RTResult().failure(RunTimeError(
			self.pos_start, self.pos_end,
			"Second argument must be list",
			exec_ctx
		))

		listA.elements.extend(listB.elements)
		return RTResult().success(Number.none)
	execute_extend.arg_names = ['listA', 'listB']

	def execute_map(self, exec_ctx):
		elements = exec_ctx.symbol_table.get("elements")
		func = exec_ctx.symbol_table.get("func")

		new_elements = []

		for i in range(0, len(elements)):
			new_elements.append(func(elements[i]))

		return RTResult().success(List(new_elements))
	execute_map.arg_names = ["elements", "func"]

	def execute_join(self, exec_ctx):
		elements = exec_ctx.symbol_table.get("elements")
		if i != len - 1: separator = exec_ctx.symbol_table.get("separator")

		result = ""
		length = len(elements)

		for i in range(0, length):
			result += elements[i]
			result += separator

		return RTResult().success(String(result))
	execute_join.arg_names = ["elements", "separator"]

############################### MATH FUNCTIONS ###############################

	def execute_floor(self, exec_ctx):
		num = exec_ctx.symbol_table.get("float")
		try:
			num = float(num.value)
		except:
			print(f'{num} cannot be floored. Try with a float or integer value.')
		
		num = math.floor(num)
		return RTResult().success(Number(num))
	execute_floor.arg_names = ['float']

	def execute_ceil(self, exec_ctx):
		num = exec_ctx.symbol_table.get("float")
		try:
			num = float(num.value)
		except:
			print(f'{num} cannot be ceiled. Try with a float or integer value.')
		
		num = math.ceil(num)
		return RTResult().success(Number(num))
	execute_ceil.arg_names = ['float']

	def execute_square(self, exec_ctx):
		value = exec_ctx.symbol_table.get("value")
		value = value.value
		try:
			number = int(value)
		except ValueError:
			try: 
				number = float(value)
			except:
				return RTResult(IncorrectValueTypeError(
					self.pos_start, self.pos_end,
					f"'{value}' must be an float or an integer. Try again!",
					exec_ctx
					))

		number = number ** 2
		return RTResult().success(Number(number))
	execute_square.arg_names = ['value']

	def execute_cube(self, exec_ctx):
		value = exec_ctx.symbol_table.get("value")
		value = value.value
		try:
			number = int(value)
		except ValueError:
			try: 
				number = float(value)
			except:
				return RTResult(IncorrectValueTypeError(
					self.pos_start, self.pos_end,
					f"'{value}' must be an float or an integer. Try again!",
					exec_ctx
					))

		number = number ** 3
		return RTResult().success(Number(number))
	execute_cube.arg_names = ['value']

	def execute_tessaract(self, exec_ctx):
		value = exec_ctx.symbol_table.get("value")
		value = value.value
		try:
			number = int(value)
		except ValueError:
			try: 
				number = float(value)
			except:
				return RTResult(IncorrectValueTypeError(
					self.pos_start, self.pos_end,
					f"'{value}' must be an float or an integer. Try again!"
					))

		number = number ** 4
		return RTResult().success(Number(number))
	execute_tessaract.arg_names = ['value']

	def execute_add(self, exec_ctx):
		numA = exec_ctx.symbol_table.get("NumberA")
		numb = exec_ctx.symbol_table.get("NumberB")
		numa = numA.value
		numb = numb.value

		result = numa + numb

		return RTResult().success(Number(result)) 
	execute_add.arg_names = ['NumberA', 'NumberB']

	def execute_subt(self, exec_ctx):
		numA = exec_ctx.symbol_table.get("NumberA")
		numb = exec_ctx.symbol_table.get("NumberB")
		numa = numA.value
		numb = numb.value

		result = numa - numb
		return RTResult().success(Number(result)) 
	execute_subt.arg_names = ['NumberA', 'NumberB']

	def execute_mult(self, exec_ctx):
		numA = exec_ctx.symbol_table.get("NumberA")
		numb = exec_ctx.symbol_table.get("NumberB")
		numa = numA.value
		numb = numb.value

		result = numa * numb
		return RTResult().success(Number(result)) 
	execute_mult.arg_names = ['NumberA', 'NumberB']

	def execute_divi(self, exec_ctx):
		numA = exec_ctx.symbol_table.get("NumberA")
		numb = exec_ctx.symbol_table.get("NumberB")
		numa = numA.value
		numb = numb.value

		result = numb / numa
		return RTResult().success(Number(result)) 
	execute_divi.arg_names = ['NumberA', 'NumberB']

	def execute_sqrt(self, exec_ctx):
		value = exec_ctx.symbol_table.get("value")
		value = value.value

		result = math.sqrt(value)

		return RTResult().success(Number(result))
	execute_sqrt.arg_names = ['value']

	def execute_cbrt(self, exec_ctx):
		value = exec_ctx.symbol_table.get("value")
		value = value.value

		result = math.cbrt(value)

		return RTResult().success(Number(result))
	execute_cbrt.arg_names = ['value']

	def execute_ranint(self, exec_ctx):
		maxint = int(exec_ctx.symbol_table.get("maxint"))
		minint = int(exec_ctx.symbol_table.get("minint"))

		result = random.randint(maxint, minint)
		return RTResult().success(Number(result))
	execute_ranint.arg_names = ['maxint', 'minint']

	def execute_range(self, exec_ctx):
		min_int = int(exec_ctx.symbol_table.get("min"))
		max_int = int(exec_ctx.symbol_table.get("max"))
		for i in range(min_int, max_int):
			return RTResult().success(Number(i))
	execute_range.arg_names = ["min", "max"]

############################### Language Embeded Functions ###############################

	def execute_run(self, exec_ctx):
		fn = exec_ctx.symbol_table.get("fn")

		if not isinstance(fn, String):
			return RTResult().failure(RunTimeError(
				self.pos_start, self.pos_end,
				"Filename must be string data type!",
				exec_ctx
			))

		fn = fn.value

		try:
			with open(fn, "r") as file:
				script = file.read()
		except Exception as e:
			return RTResult().failure(RunTimeError(
				self.pos_start, self.pos_end,
				f"Failed to load script \"{fn}\"\n" + str(e),
				exec_ctx
			))

		from run_i import run
		_, error = run(fn, script)

		if error: return RTResult().failure(RunTimeError(
			self.pos_start, self.pos_end,
			f"Failed to finish executing script \"{fn}\"\n" + 
			error.as_string(),
			exec_ctx
			))

		return RTResult().success(Number.none)
	execute_run.arg_names = ["fn"] # File name

	def execute_global_attributes(self, exec_ctx):
		Attributes = exec_ctx.symbol_table.getTable()
		AttrList = List([])
		for i in Attributes:
			for items in i.items():
				AttrList.elements.append(items)
		return RTResult().success(AttrList)
	execute_global_attributes.arg_names = []


############################### Assignments ###############################

BuiltInFunction.printout    = BuiltInFunction("printout")
BuiltInFunction.printreturn = BuiltInFunction("printreturn")
BuiltInFunction.typein      = BuiltInFunction("typein")
BuiltInFunction.typein_int  = BuiltInFunction("typein_int")
BuiltInFunction.clear       = BuiltInFunction("clear")
BuiltInFunction.is_number   = BuiltInFunction("is_number")
BuiltInFunction.is_string   = BuiltInFunction("is_string")
BuiltInFunction.is_list     = BuiltInFunction("is_list")
BuiltInFunction.is_function = BuiltInFunction("is_function")
BuiltInFunction.append      = BuiltInFunction("append")
BuiltInFunction.pop         = BuiltInFunction("pop")
BuiltInFunction.extend      = BuiltInFunction("extend")
BuiltInFunction.floor 		= BuiltInFunction("floor")
BuiltInFunction.ceil      	= BuiltInFunction("ceil")
BuiltInFunction.square  	= BuiltInFunction("square")
BuiltInFunction.cube		= BuiltInFunction("cube")
BuiltInFunction.tessaract	= BuiltInFunction("tessaract")
BuiltInFunction.add 		= BuiltInFunction("add")
BuiltInFunction.subt		= BuiltInFunction("subt")
BuiltInFunction.mult		= BuiltInFunction("mult")
BuiltInFunction.divi		= BuiltInFunction("divi")
BuiltInFunction.sqrt		= BuiltInFunction("sqrt")
BuiltInFunction.cbrt		= BuiltInFunction("cbrt")
BuiltInFunction.ranint		= BuiltInFunction("ranint")
BuiltInFunction.range       = BuiltInFunction("range")
BuiltInFunction.run 		= BuiltInFunction("run")
BuiltInFunction.len 		= BuiltInFunction("len")
BuiltInFunction.map			= BuiltInFunction("map")
BuiltInFunction.join 		= BuiltInFunction("join")
BuiltInFunction.clean		= BuiltInFunction("clean")
BuiltInFunction.global_attributes = BuiltInFunction("global_attributes")