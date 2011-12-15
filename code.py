# coding: utf-8
import web
from setting.url import urls

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()

#if __name__ == "__main__":
#    app.run()
