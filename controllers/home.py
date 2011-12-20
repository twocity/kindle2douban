# coding: utf-8

import web
from douban.service import DoubanService
from setting import setting

render = setting.render
API_KEY = '0516527552aeabd50f42f75ff80c037f'
SECRET = '438ad54fabc47fea'

client = DoubanService(API_KEY,SECRET)

class Main:
	def GET(self):
		return render.home('hello')