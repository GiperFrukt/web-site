# -*- coding: utf-8 -*-
import os
import sys

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.wsgi import wsgiapp

MIDDLEWARE_TOP = "<div class='top'>Middleware TOP</div>"
MIDDLEWARE_BOTTOM = "<div class='botton'>Middleware BOTTOM</div>"


class MyMiddleWare(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        response = self.app(environ, start_response)[0].decode()
        if response.find('<body>') == True:
            #разделяем документ на кусок до <Body> и после
            beforeBody,remainder = response.split('<body>')
            #оставшуюся часть делим на тело файла и концовку
            body,htmlend = remainder.split('</body>')
            #в тело документа вставляем мидлваровский код
            bodycontent = '<body>'+ MIDDLEWARE_TOP + body + MIDDLEWARE_BOTTOM+'</body>'
            return [beforeBody.encode() + bodycontent.encode() + htmlend.encode()]
        else: return [MIDDLEWARE_TOP + response.encode() + MIDDLEWARE_BOTTOM]

import codecs
@wsgiapp
def app(environ, start_response):
    res = environ['PATH_INFO']
    path = "." + res+".html"
    currentDirectory = "web_site/templates/";
    #if not os.path.isfile(path):
        #path = 'about.html' # добавить страничку 404. НИНАЙДЕНА!!!11!!
    #print('...path: ', path)
    file = open(currentDirectory+path, 'rb')
    fileContent = file.read()
    #file.close()
    #file = open(fileContent, 'r')
    #file = open(fileContent, 'r')
    #if fileContent.find('<body>') == True:
        # разделяем документ на кусок до <Body> и после
        #beforeBody, remainder = fileContent.split('<body>')
        # оставшуюся часть делим на тело файла и концовку
        #body, htmlend = remainder.split('</body>')
        # в тело документа вставляем мидлваровский код
        #bodycontent = '<body>' + MIDDLEWARE_TOP + body + MIDDLEWARE_BOTTOM + '</body>'
        #page = beforeBody + bodycontent + htmlend;
        #start_response('200 OK', [('Content-Type', 'text/html')])
        #return [page.encode()]
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [fileContent]



def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    #config.include('.models')
    config.include('pyramid_mako')
    config.add_mako_renderer('.html')
    config.add_mako_renderer('.shtml')
    config.include('.routes')
    config.add_route('about', '/about')
    config.add_route('artists1', '/Till_Lindemann')
    config.add_view(app, route_name='artists1')
    config.add_route('profile', '/profile')
    config.add_route('test2', '/test2')
    config.add_route('test3', '/test3   ')
    config.add_route('home', '/')

    config.add_route('artists2', '/Christian_Lorenz')
    config.add_route('artists3', '/Christoph_Doom_Schneider')
    config.add_route('artists4', '/Oliver_Riedel')
    config.add_route('artists5', '/Paul_Landers')
    config.add_route('artists6', '/Richard_Kruspe-Bernstein')


    config.scan()
    pyramid_app = config.make_wsgi_app()
    #answer = MyMiddleWare(pyramid_app)
    return pyramid_app
