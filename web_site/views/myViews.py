from pyramid.response import Response
from pyramid.view import view_config
import os

from ..scripts.dbMethods import *
#@view_config(route_name='about', renderer='../templates/about.jinja2')

@view_config(route_name='LiebeIstFuerAlleDa', renderer='../templates/AlbumsVizualization.jinja2')
@view_config(route_name='Mutter', renderer='../templates/AlbumsVizualization.jinja2')
@view_config(route_name='ReiseReise', renderer='../templates/AlbumsVizualization.jinja2')
@view_config(route_name='Herzeleid', renderer='../templates/AlbumsVizualization.jinja2')
@view_config(route_name='Sehnsucht', renderer='../templates/AlbumsVizualization.jinja2')
@view_config(route_name='Rosenrot', renderer='../templates/AlbumsVizualization.jinja2')
def test(request):
    res = str(request).split('\n')[0].split(' ')[1]
    songpaths = getSongs(res[1:]) # название альбома без слэш
    return {"rows": songpaths}

@view_config(route_name='artists2', renderer='../templates/Christian_Lorenz.jinja2')
@view_config(route_name='about', renderer='../templates/about.jinja2')
@view_config(route_name='artists1', renderer='../templates/Till_Lindemann.jinja2')
@view_config(route_name='artists3', renderer='../templates/Christoph_Doom_Schneider.jinja2')
@view_config(route_name='artists4', renderer='../templates/Oliver_Riedel.jinja2')
@view_config(route_name='artists5', renderer='../templates/Paul_Landers.jinja2')
@view_config(route_name='artists6', renderer='../templates/Richard_Kruspe-Bernstein.jinja2')
@view_config(route_name='test2', renderer='../templates/test2.shtml')
@view_config(route_name='test3', renderer='../templates/test3.jinja2')
@view_config(route_name='home', renderer='../templates/home.jinja2')
def view_about(request):
    #file = open(os.getcwd(), 'r')
    return {'project': 'MyProject'}



from pyramid.security import remember, authenticated_userid, forget
from pyramid.httpexceptions import HTTPFound, HTTPForbidden

@view_config(route_name='authorization', renderer='templates/authorization.jinja2')
def my_view(request):
    print("azaza")
    #nxt = request.params.get('next') or request.route_url('profile')
    nxt = ""
    did_fail = False
    if 'login' in request.POST:
        user = login(
            request.POST["login"], request.POST["password"]
        )

        '''if user:
            nxt = True
            print(user)
        else:
            nxt = False'''

        if user:
            headers = remember(request, user.id)
            return HTTPFound(location=nxt, headers=headers)
        else:
            did_fail = True
    return {
        'login': "",
        'next': nxt,
        'failed_attempt': did_fail,
    }