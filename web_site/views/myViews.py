from pyramid.response import Response
from pyramid.view import view_config
import os

#@view_config(route_name='about', renderer='../templates/about.jinja2')
@view_config(route_name='test', renderer='../templates/test.html')
@view_config(route_name='test2', renderer='../templates/test2.shtml')
def my_view_about(request):
    #return {'project': 'MyProject'}
    result = []
    path = 'test2.shtml';
    if not os.path.isfile(path):
        file = open(path, 'r')
        for x in file:
            result.append(x)
    #return result
    return {'project': 'MyProject'}
    return Response(result)


@view_config(route_name='about', renderer='templates/about.jinja2')
@view_config(route_name='profile', renderer='templates/profile.jinja2')
@view_config(route_name='home', renderer='../templates/home.jinja2')
def view_about(request):
    return {'project': 'MyProject'}