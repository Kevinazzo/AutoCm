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

# High-level browser controller API
class _browser:
	tabs = []
	activeTab = None

	# Go to homepage cospace.cloud
	def start(self):
		self.driver = webdriver.Firefox()

	def goto(self, url):
		print("> loading homepage")
		driver.get()
		print('> done: ' + self.driver.current_url)

	def newTab(self):
		anew = tab()
		self.tabs.append(anew)

	def switchTab(self, _index):
		try:
			self.activeTab = _index
		except:
			print("tab not found")

	def switchNextTab(self):
		self.driver

class tab:
	def __init__(self, _url):
		self.url = _url
	@property
	def url(self):
		return self.url

	@url.setter
	def url(self, value):
		self.url = value


# Log in
def login():
	print("> awaiting logIn credentials")
	usrTxT = driver.find_element_by_id("io-ox-login-username")
	usrPsw = driver.find_element_by_id("io-ox-login-password")
	loginButton = driver.find_element_by_id("io-ox-login-button")
	usrTxT.clear()
	usrPsw.clear()
	usrTxT.send_keys(os.environ['MAILUSR'])
	usrPsw.send_keys(os.environ['MAILPSW'])
	while True:
		try:
			loginButton.click()
			break
		except:
			pass

def getUnreads():
	unreads = []
	mailList = driver.find_elements_by_css_selector("li.list-item.selectable")
	for element in mailList:
		cssclass = element.get_attribute("class")
		if str(cssclass).__contains__('unread'):
			unreads.append(element)
	return unreads

browser = _browser()
browser.goto('https://mail.cospace.cloud/appsuite/ui#!!&app=io.ox/mail&folder=default0/INBOX')
login()
getUnreads()
