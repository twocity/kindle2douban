# coding: utf-8

pre_fix = 'controllers.'

urls = (
    '/',                       pre_fix + 'index.Index',
	'/login',                  pre_fix + 'index.Login',
	'/logout',                 pre_fix + 'index.Logout',
    '/oauthdouban',            pre_fix + 'index.OAuthDouban',
    '/home/*',          	   pre_fix + 'index.Home',
#   '/todo/(\d+)/edit',     pre_fix + 'todo.Edit',
#    '/todo/(\d+)/delete',   pre_fix + 'todo.Delete',
#    '/todo/(\d+)/finish',   pre_fix + 'todo.Finish',

)
