def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('about', '/about')
    config.add_route('authorization', '/authorization')
    config.add_route('test2', '/test2')
    config.add_route('test3', '/test3')
    config.add_route('Till_Lindemann', '/Till_Lindemann')
    config.add_route('Christian_Lorenz', '/Christian_Lorenz')
    config.add_route('Christoph_Doom_Schneider', '/Christoph_Doom_Schneider')
    config.add_route('Oliver_Riedel', '/Oliver_Riedel')
    config.add_route('Paul_Landers', '/Paul_Landers')
    config.add_route('Richard_Kruspe-Bernstein', '/Richard_Kruspe-Bernstein')
    config.add_route('Herzeleid', '/Herzeleid')
    config.add_route('Sehnsucht', '/Sehnsucht')
    config.add_route('Rosenrot', '/Rosenrot')
    config.add_route('LiebeIstFuerAlleDa', '/LiebeIstFuerAlleDa')
    config.add_route('Mutter', '/Mutter')
    config.add_route('ReiseReise', '/ReiseReise')
    #config.add_route('login1', '/login')
    #config.add_route('logout', '/logout')
    config.add_route('login1', '/login')
    config.add_route('logout', '/logout')

