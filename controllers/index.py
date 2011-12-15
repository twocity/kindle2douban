# coding: utf-8

import web
from douban.client import OAuthClient
from douban.service import DoubanService
from setting import setting

render = setting.render
API_KEY = '0516527552aeabd50f42f75ff80c037f'
SECRET = '438ad54fabc47fea'

#request_tokens = {}
#access_tokens = {}

class Login:
	def GET(self):
		return render.index()
class OAuthDouban:
	def GET(self):
		douban_svc = DoubanService(API_KEY, SECRET)
		req_token, req_secret = douban_svc.client.get_request_token()
		url = douban_svc.client.get_authorization_url(req_token,req_secret)
		raise web.seeother(url)