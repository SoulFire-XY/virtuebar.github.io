###########################################
# RUNTIME RESULT
###########################################

class RTResult:
	def __init__(self):
		self.reset()
	
	def reset(self):
		self.value = None
		self.error = None
		self.func_value_return = None
		self.loop_break = False
		self.loop_skip = False

	def register(self, res):
		self.error = res.error
		self.func_value_return = res.func_value_return
		self.loop_break = res.loop_break
		self.loop_skip = res.loop_skip
		return res.value

	def success(self, value):
		self.reset()
		self.value = value
		return self

	def success_return(self, value):
		self.reset()
		self.func_value_return = value
		return self

	def success_skip(self):
		self.reset()
		self.loop_skip = True
		return self
		
	def success_break(self):
		self.reset()
		self.loop_break = True
		return self
		
	def failure(self, error):
		self.reset()
		self.error = error
		return self

	def should_return(self):
		return (
			self.error or
			self.func_value_return or 
			self.loop_skip or
			self.loop_break
		)