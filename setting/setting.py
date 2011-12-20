# coding: utf-8

import web
from url import urls

render = web.template.render('templates/',cache=False)
web.config.debug = False

API_KEY = '0516527552aeabd50f42f75ff80c037f'
SECRET = '438ad54fabc47fea'

config = web.storage(
			email ='dvy.zhang@gmail.com',
			site_name = 'kindle读书笔记',
			site_desc = '',
			static = '/static',
)
app = web.application(urls, globals())

session = web.session.Session(
		app,web.session.DiskStore('sessions'),
		initializer={'isLogin':0})
		
web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render