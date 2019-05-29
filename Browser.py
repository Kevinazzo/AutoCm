""" Firefox browser module"""
from selenium import webdriver
from Scripts import Bitbucket,Cospace,Git,JIRA

# region VAR
browserDriver = None
tabs = []
activeTab = None
# endregion
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


def start():
	"""
	Browser initialization
	"""
	browserdriver = webdriver.Firefox()
	newTab()


def goTo(url):
	"""Go to website"""
	if activeTab is None:
		pass
	print('> going: ' + url)
	browserDriver.get(url)
	print('> done: ' + browserDriver.current_url)


def newTab():
	"""open new tab"""
	x = Tab()
	x.index = tabs.__len__() + 1
	x.script = ''
	x.url = ''
	tabs.append(x)
	activeTab = x


def switchTab(self, idx):
	"""switch active tab"""
	try:
		self.activeTab = idx
	except:
		print("tab not found")


def switchNextTab(self):
	pass


def closeTab(self):
	pass


def runScript(self):

	pass
