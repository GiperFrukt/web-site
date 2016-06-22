# -*- coding: utf-8 -*-
from pyramid.authentication import SessionAuthenticationPolicy
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from .scripts.dbMethods import getUser

class HelloFactory(object):
    def __init__(self, request):
        self.__acl__ = [
            (Allow, 'vasya', 'view'),
            (Allow, 'group:editors', 'add'),
            (Allow, 'group:editors', 'edit'),
        ]

from pyramid.security import Allow, forget, remember

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    '''config = Configurator(settings=settings)

    authn_policy = AuthTktAuthenticationPolicy(
        'sosecret', callback=getUser, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)'''

    authn_policy = AuthTktAuthenticationPolicy('seekrit', hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()

    config = Configurator(root_factory=HelloFactory)
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    config.include('pyramid_jinja2')
    #config.include('.models')
    config.include('pyramid_mako')
    config.add_mako_renderer('.html')
    config.add_mako_renderer('.shtml')
    config.include('.routes')

    config.scan()
    pyramid_app = config.make_wsgi_app()
    #answer = MyMiddleWare(pyramid_app)
    return pyramid_app
