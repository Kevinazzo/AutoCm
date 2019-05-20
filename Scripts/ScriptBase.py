class ScriptBase:
	"""
		Parent class for automated scripts
		contains mappings for DOM elements and
		user-defined UI controls
	"""
	def __init__(self):
		self.name = None
		self.description = None
		self.version = None
		self.targetVersion = None
		self.mappings = None
		self.dateLastModified = None
		self.dateCreated = None

	def mapControls(self):

