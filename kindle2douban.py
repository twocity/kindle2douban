# coding: utf-8
import web
from setting import setting
#from setting.url import urls

#app = web.application(urls, globals())
app = setting.app
session = setting.session

def getSession():
	if '_session' not in web.config:
		web.config._session = session
	

if __name__ == "__main__":
	getSession()
	app.run()

#if __name__ == "__main__":
#    app.run()
