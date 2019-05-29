class Switch(object):

	def __init__(self):
		self.value = None
		self.fall = False

	def __iter__(self):
		"""return the match method once, then stop"""
		yield self.match
		raise StopIteration

	def match(self,*args):
		"""indicate wether or not to enter a case suite"""
		if self.fall or not args:
			return True
		elif self.value in args:
			self.fall = True
			return True
		else:
			return False