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
import Browser
import os

# region var
user = os.environ['MAILUSR']
psw = os.environ['MAILPSW']
# endregion


Browser.start()
Browser.driver = Browser.webdriver.Firefox()
