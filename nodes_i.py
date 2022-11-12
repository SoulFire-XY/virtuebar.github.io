###########################################
# NODES
###########################################

class NumberNode: # Float / Integer None
	def __init__(self, tok, _type=None):
		self.tok = tok
		self._type = _type

		self.pos_start = self.tok.pos_start
		self.pos_end = self.tok.pos_end

	def __repr__(self):
		return f'{self.tok}'

class VarAccessNode:
	def __init__(self, var_name_tok, _type=None):
		self.var_name_tok = var_name_tok
		self._type = _type

		self.pos_start = self.var_name_tok.pos_start
		self.pos_end = self.var_name_tok.pos_end

class VarAssignNode:
	def __init__(self, var_name_tok, value_node, _type=None):
		self.var_name_tok = var_name_tok
		self.value_node = value_node
		self._type = _type

		self.pos_start = self.var_name_tok.pos_start
		self.pos_end = self.value_node.pos_end

class BinOpNode: # Binary Operator None
	def __init__(self, left_node, op_tok, right_node, _type=None):
		self.left_node = left_node
		self.op_tok = op_tok
		self.right_node = right_node
		self._type = _type

		self.pos_start = self.left_node.pos_start
		self.pos_end = self.right_node.pos_end

	def __repr__(self):
		return f'({self.left_node}, {self.op_tok}, {self.right_node})'

class UnaryOpNode:
	def __init__(self, op_tok, node, _type=None):
		self.op_tok = op_tok
		self.node = node
		self._type = _type

		self.pos_start = self.op_tok.pos_start
		self.pos_end = self.node.pos_end

	def __repr__(self):
		return f'({self.op_tok}, {self.node})'