# coding: utf-8

import web

render = web.template.render('templates/',cache=False)
web.config.debug = True

config = web.storage(
			email ='dvy.zhang@gmail.com',
			site_name = 'kindle读书笔记',
			site_desc = '',
			static = '/static',
)

web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render