# -*- coding: utf-8 -*-
from pyramid.authentication import SessionAuthenticationPolicy
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from .scripts.dbMethods import getUser

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    authn_policy = AuthTktAuthenticationPolicy(
        'sosecret', callback=getUser, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
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
