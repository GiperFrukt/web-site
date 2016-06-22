from pyramid.view import view_config
from ..scripts.dbMethods import *
from pyramid.security import remember, authenticated_userid, forget
from pyramid.httpexceptions import HTTPFound

@view_config(route_name='LiebeIstFuerAlleDa', renderer='../templates/AlbumsVizualization.jinja2')
@view_config(route_name='Mutter', renderer='../templates/AlbumsVizualization.jinja2')
@view_config(route_name='ReiseReise', renderer='../templates/AlbumsVizualization.jinja2')
@view_config(route_name='Herzeleid', renderer='../templates/AlbumsVizualization.jinja2')
@view_config(route_name='Sehnsucht', renderer='../templates/AlbumsVizualization.jinja2')
@view_config(route_name='Rosenrot', renderer='../templates/AlbumsVizualization.jinja2')
def almub_view(request):
    print(request)
    username = request.authenticated_userid
    res = str(request).split('\n')[0].split(' ')[1]
    res1 = res[1:]
    picture = getAlbum(res[1:])
    songpaths = getSongs(res[1:]) # название альбома без слэш
    added = 0
    if 'addFavorite' in request.POST:
        added = addSongFavorite(username, request.POST["addFavorite"])
    hideIt = "hidden"
    if username:
        human = username
        hideIt = "visible"
    else:
        human = "Гость"
    return {"rows": songpaths,
            'came_from': res1,
            'photo': picture,
            'human': human,
            'hideIt': hideIt,
            }


@view_config(route_name='favorites', renderer='../templates/FavoriteVizualization.jinja2')
def favorite_view(request):
    print(request)
    username = request.authenticated_userid
    res = str(request).split('\n')[0].split(' ')[1]
    res1 = res[1:]

    hideIt = "hidden"
    if username:
        songpaths = getFavoritesSong(username)  # название альбома без слэш
        human = username
        hideIt = "visible"
    else:
        return HTTPFound(location=request.route_url("about"))
        human = "Гость"
    return {"rows": songpaths,
            'came_from': res1,
            'photo': "",
            'human': human,
            'hideIt': hideIt,
            }


@view_config(route_name='Christian_Lorenz', renderer='../templates/Christian_Lorenz.jinja2')
@view_config(route_name='about', renderer='../templates/about.jinja2')
@view_config(route_name='Till_Lindemann', renderer='../templates/Till_Lindemann.jinja2')
@view_config(route_name='Christoph_Doom_Schneider', renderer='../templates/Christoph_Doom_Schneider.jinja2')
@view_config(route_name='Oliver_Riedel', renderer='../templates/Oliver_Riedel.jinja2')
@view_config(route_name='Paul_Landers', renderer='../templates/Paul_Landers.jinja2')
@view_config(route_name='Richard_Kruspe-Bernstein', renderer='../templates/Richard_Kruspe-Bernstein.jinja2')
@view_config(route_name='contacts', renderer='../templates/contacts.jinja2')
@view_config(route_name='home', renderer='../templates/about.jinja2')
def view_about(request):
    username = request.authenticated_userid
    #file = open(os.getcwd(), 'r')
    res = str(request).split('\n')[0].split(' ')[1]
    res1 = res[1:]
    hideIt = "hidden"
    if username:
        human = username
        hideIt = "visible"
    else: human = "Гость"
    return {'came_from': res1,
            'human':human,
            'hideIt': hideIt,
            }


@view_config(route_name='login1', renderer='../templates/authorization.jinja2')
@view_config(route_name='logout', renderer='../templates/authorization.jinja2')
@view_config(route_name='authorization', renderer='../templates/authorization.jinja2')
def test(request):
    res = str(request).split('\n')[0].split(' ')[1]
    came_from = res[1:]
    print(request.authenticated_userid)
    print(request.POST)
    if 'login' in request.POST and 'password' in request.POST:
        user = login(
            request.POST["login"], request.POST["password"]
        )
        if user:
            headers = remember(request, user.login)
            # reques.route_name
            return HTTPFound(location=request.route_url(request.POST["came_from"], name=user.login),
                         headers=headers)

        print(request.POST["login"], request.POST["password"])
    if 'form.submitted' in request.POST and request.POST["form.submitted"] == "LogOut":
        print (request.POST["form.submitted"])
        headers = forget(request)
        return HTTPFound(location=request.route_url('about', name='log out!!!'),
                         headers=headers)

    return HTTPFound(location=request.route_url(request.POST["came_from"]))


def get_current_user(request):
    id_ = authenticated_userid(request)
    print("in views ", id_)
    user = getUser(id_, request)
    return user