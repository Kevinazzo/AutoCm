from main import br as browser
from main import user, psw
from Scripts import ScriptBase

import _json

class CospaceController(ScriptBase):
	"""function-container class for each script"""
	def mapControls(self):
		super() we need to call super here... find HOW now


	# Log in
	def login(self):
		print("> awaiting logIn credentials")
		# usrTxTBox.clear()
		# pswTxtBox.clear()
		# usrTxTBox.send_keys(user)
		# pswTxtBox.send_keys(psw)
		# while True:
		# 	try:
		# 		loginButton.click()
		# 		break
		# 	except:
		# 		pass

	def getUnread(self):
		unread = []
		# mailList = driver.find_elements_by_css_selector("li.list-item.selectable")
		# for element in mailList:
		# 	cssclass = element.get_attribute("class")
		# 	if str(cssclass).__contains__('unread'):
		# 		unread.append(element)
		# return unread

	# Controller running process and method calling function
	def worker(self):
		browser.goTo('https://mail.cospace.cloud/appsuite/ui#!!&app=io.ox/mail&folder=default0/INBOX')
		login()
		getUnread()
