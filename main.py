# Project: AutoCM (nombre temporal)
# Autor: Kevin Miranda Luna
# Proyecto de practicas profesionales UTE
# Mayo - Agosto 2019
#
# Descripcion: programa automatizado para realizar peticiones de CM en las diferentes herramientas de la empresa CITI
# Software:
# 	- Python
# 	- Selenium
# 	- AutoHotkey
# 	- Git

import os
from selenium import webdriver

# High-level browser controller API with basic browser functions
class browser:
	class tab:
		def __init__(self, _url):
			self.url = _url

		@property
		def url(self):
			return self.url

		@url.setter
		def url(self, value):
			self.url = value

	def __init__(self):
		self.driver = None
		self.tabs = []
		self.activeTab = None
		self.start()

	# Go to homepage cospace.cloud
	def start(self):
		"""Starts an instance of a firefox Browser"""
		self.driver = webdriver.Firefox()

	def goTo(self, url):
		print("> loading homepage")
		self.driver.get(url)
		print('> done: ' + self.driver.current_url)

	def newTab(self):
		r = tab()
		self.tabs.append(r)

	def switchTab(self, _index):
		try:
			self.activeTab = _index
		except:
			print("tab not found")

	def switchNextTab(self):
		self.driver

br = browser()
user = os.environ.environ['MAILUSR']
psw = os.environ['MAILPSW']
