from pyramid.response import Response
from pyramid.view import view_config
import os

from ..scripts.dbMethods import *
#@view_config(route_name='about', renderer='../templates/about.jinja2')

@view_config(route_name='Herzeleid', renderer='../templates/AlbumsVizualization.jinja2')
@view_config(route_name='Sehnsucht', renderer='../templates/AlbumsVizualization.jinja2')
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
def my_view_about(request):
    #return {'project': 'MyProject'}
    #result = []
    #path = 'test2.shtml';
    #file = open(os.getcwd(), 'r')
    #if not os.path.isfile(path):
        #path = os.getcwd();
        #file = open(path, 'r')
        #for x in file:
            #result.append(x)
    #return result
    return {'project': 'MyProject'}
    #return Response(result)


@view_config(route_name='test3', renderer='../templates/test3.jinja2')
@view_config(route_name='home', renderer='../templates/home.jinja2')
def view_about(request):
    #file = open(os.getcwd(), 'r')
    return {'project': 'MyProject'}