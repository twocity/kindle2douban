# coding: utf-8

import web
import urllib
from douban.client import OAuthClient
from douban.service import DoubanService
from setting import setting
import xml.etree.ElementTree as etree

render = setting.render
API_KEY = setting.API_KEY
SECRET = setting.SECRET

request_tokens = {}
access_tokens = {}

douban_client = DoubanService(API_KEY, SECRET)
#web.ctx.session = web.config._session
session = setting.session

def login_required(func):
	def Function(*args):
		if session.isLogin == 0:
			raise web.seeother('/login')
		else:
			return func(*args)
	return Function
	
class Index:
	@login_required
	def GET(self):
#		if session.isLogin == 0:
#			return render.login()
#		else:
#			raise web.seeother('/home')
		raise web.seeother('/home')	
		
class Login:
	def GET(self):
		return render.login()
	
	def POST(self):
		print 'login post'
		user, passwd = web.input().form_email, web.input().form_password
		if user and passwd:
			# do something check
			if user == 'dvy.zhang@gmail.com' and passwd == '123':
				print 'login!!!'
				session.isLogin = 1
				raise web.seeother('/home')
		else:
			return render.login()
			
class Logout:
	def GET(self):
		session.kill()
		raise web.seeother('/login')

class OAuthDouban:
	def GET(self):

		req_token, req_secret = douban_client.client.get_request_token()
		url = douban_client.GetAuthorizationURL(req_token,req_secret)
		
		access_token, access_secret, douban_uid = \
                     douban_client.client.get_access_token(req_token, req_secret)
		#douban_client.client.login(access_token,access_secret)
		
		raise web.seeother(url)
		#render(callback_url)

class Home:
	@login_required
	def GET(self):
		reading = douban_client.GetCollectionFeed('http://api.douban.com/people/twocity/collection?cat=book&status=reading')
		#print reading
		#tree = etree.parse(reading)
		print 'reading'
		print '==================='
		for entry in reading.entry:
			print 'title:' + entry.title.text
			print 'updated:' + entry.updated.text
			print 'status:' + entry.status.text
			print 'id:' + entry.id.text
			print '************'
			for attr in entry.subject.attribute:
				print attr.name + ": " + attr.text
				content = attr.text
			print entry.subject.title.text
			print '---------------'
#			print 'author:'
#			for author in entry.author:
#				print entry.author.name.text
		return render.home(content)

def escape(s):
	return urllib.quote(s,safe='~')