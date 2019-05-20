"""
Proyecto: AutoCM (nombre temporal)
Autor: Kevin Miranda Luna
Proyecto de practicas profesionales UTE
Mayo - Agosto 2019

Descripcion: programa automatizado para realizar peticiones de CM en las diferentes herramientas de la empresa CITI
Software:
	- Python
	- Selenium
	- AutoHotkey
	- Git
"""
import os
from selenium import webdriver
from Scripts import Bitbucket,Cospace,Git,JIRA

#region var
user = os.environ['MAILUSR']
psw = os.environ['MAILPSW']
#endregion


class Browser:
	"""High-level browser controller API with basic browser functions"""
	# region Tab
	class Tab:
		""" instance of tab """
		def __init__(self, _url):
			self.url = _url
			self.script = None
			self.index = None

		@property
		def url(self):
			return self.url

		@url.setter
		def url(self, value):
			self.url = value
	# endregion

	def __init__(self):
		"""Constructor"""
		self.driver = None
		self.tabs = []
		self.activeTab = None

	def goTo(self, url):
		"""Go to website"""
		print('> going: ' + url)
		self.driver.get(url)
		print('> done: ' + self.driver.current_url)

	def newTab(self):
		"""open new tab"""
		r = browser.tab()
		self.tabs.append(r)

	def switchTab(self, _index):
		"""switch active tab"""
		try:
			self.activeTab = _index
		except:
			print("tab not found")

	def switchNextTab(self):
		pass

	def runScript():


br = Browser()
br.start()
br.driver = webdriver.Firefox()
