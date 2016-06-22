# -*- coding: utf-8 -*-
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from pyramid.config import Configurator
from .scripts.dbMethods import getUser

def main(global_config, **settings):
    authn_policy = AuthTktAuthenticationPolicy('seekrit', hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()

    config = Configurator(settings=settings)
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    config.include('pyramid_jinja2')
    config.include('pyramid_mako')
    config.add_mako_renderer('.html')
    config.include('.routes')

    config.scan()
    pyramid_app = config.make_wsgi_app()
    return pyramid_app
