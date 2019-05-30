import json
import os

class ScriptBase:
	"""
		Parent class for automated scripts
		contains mappings for DOM elements and
		user-defined UI controls
	"""
	def __init__(self):
		self.name = None
		self.mappings = {}

	def mapControls(self):
		dirpath = os.path.dirname(os.path.abspath(__file__))
		with open(dirpath, 'r') as file:
			data = file.read()
		obj = json.loads(data)

		for key,value in obj.items():
			pass