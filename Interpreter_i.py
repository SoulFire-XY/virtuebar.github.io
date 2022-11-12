from runtime_result_i import RTResult
from token_i import *
from values_i import *
from context_i import *

###########################################
# Interpreter
###########################################

class Interpreter:
	def visit(self, node, context, type_Var_decle):
		self.type_Var_decle = type_Var_decle
		method_name = f'visit_{type(node).__name__}'
		method = getattr(self, method_name, self.no_visit_method) 
		return method(node, context)

	def no_visit_method(self, node):
		raise Exception(f'No visit_{type(node).__name__} method defined')

	################################################################
	
	def visit_NumberNode(self, node, context):
		return RTResult().success(
			Number(node.tok.value).set_context(context).set_pos(node.pos_start, node.pos_end)
		)

	def visit_VarAccessNode(self, node, context):
		res = RTResult()
		var_name = node.var_name_tok.value
		value = context.symbol_table.get(var_name)

		if not value:
			return res.failure(RunTimeError(
				node.pos_start, node.pos_end,
				f"'{var_name}' is not defined!",
				context
			))
		
		value = value[0]
		value = value.copy().set_pos(node.pos_start, node.pos_end)
		return res.success(value)

	def visit_VarAssignNode(self, node, context):
		res = RTResult()
		var_name = node.var_name_tok.value
		value = res.register(self.visit(node.value_node, context, self.type_Var_decle))

		if res.error: return res

		if self.type_Var_decle in ['VAL', 'CONST']:
			if self.type_Var_decle == 'CONST':
				if var_name in context.symbol_table.symbols.keys():
					var_value = context.symbol_table.get(var_name)
					var_type = var_value[1]
					return res.failure(DefinedTypeError(
						node.pos_start, node.pos_end,
						f"'{var_name}' is already as {var_type}!"
					))
				context.symbol_table.set(var_name, (value, self.type_Var_decle))
				return res.success(value)

			context.symbol_table.set(var_name, (value, self.type_Var_decle))
			return res.success(value)

	def visit_BinOpNode(self, node, context):
		res = RTResult()
		left = res.register(self.visit(node.left_node, context, self.type_Var_decle))
		if res.error: return res
		right = res.register(self.visit(node.right_node, context, self.type_Var_decle))
		if res.error: return res

		if node.op_tok.type == TT_PLUS:
			result, error = left.added_to(right)

		elif node.op_tok.type == TT_MINUS:
			result, error = left.subbed_by(right)  

		elif node.op_tok.type == TT_MUL:
			result, error = left.multed_by(right)

		elif node.op_tok.type == TT_DIV:
			result, error = left.dived_by(right)

		elif node.op_tok.type == TT_POWER:
			result, error = left.powed_by(right)

		elif node.op_tok.type == TT_EE:
			result, error = left.get_comparison_eq(right)

		elif node.op_tok.type == TT_NE:
			result, error = left.get_comparison_ne(right)

		elif node.op_tok.type == TT_LT:
			result, error = left.get_comparison_lt(right)

		elif node.op_tok.type == TT_GT:
			result, error = left.get_comparison_gt(right)

		elif node.op_tok.type == TT_LTE:
			result, error = left.get_comparison_lte(right)

		elif node.op_tok.type == TT_GTE:
			result, error = left.get_comparison_gte(right)

		elif node.op_tok.matches(TT_KEYWORD, 'WITH'):
			result, error = left.withed_by(right)
			
		elif node.op_tok.matches(TT_KEYWORD, 'OR'):
			result, error = left.ored_by(right)

		if error: return res.failure(error)
		else: return res.success(result.set_pos(node.pos_start, node.pos_end))

	def visit_UnaryOpNode(self, node, context):
		res = RTResult()
		number = res.register(self.visit(node.node, context, self.type_Var_decle))
		if res.error: return res

		error = None

		if node.op_tok.type == TT_MINUS:
			number, error = number.multiplied_by(Number(-1))
		
		elif node.op_tok.matches(TT_KEYWORD, 'INVER'):
			number, error = number.inverted()

		if error: return res.failure(error)
		else: return res.success(number.set_pos(node.pos_start, node.pos_end))