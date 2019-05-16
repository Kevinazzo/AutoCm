from main import br as browser
from main import user, psw
import _json


#region Mappings
def mapControls():
	switcher = {
		'':"",

	}
	def mapByID():
		pass
	def mapByCssSelector():
		pass
	def mapByXpath():
		pass
	def mapByCssRoute():
		pass
	pass
#endregion

# Log in
def login():
	print("> awaiting logIn credentials")
	usrTxTBox = browser.driver.find_element_by_id("io-ox-login-username")
	pswTxtBox = browser.find_element_by_id("io-ox-login-password")
	loginButton = browser.driver.find_element_by_id("io-ox-login-button")
	usrTxTBox.clear()
	pswTxtBox.clear()
	usrTxTBox.send_keys(user)
	pswTxtBox.send_keys(psw)
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


browser.goTo('https://mail.cospace.cloud/appsuite/ui#!!&app=io.ox/mail&folder=default0/INBOX')
login()
getUnreads()