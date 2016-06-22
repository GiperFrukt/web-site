import transaction
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    )
from ..models.mymodel import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import insert

Base = declarative_base()
engine = create_engine('sqlite:///web-site.sqlite')
Base.metadata.bind = engine


def addSongFavorite(userid, song):
    with transaction.manager:
        insert_data = insert(Favorites).values(username=userid, songId = song)
        con = engine.connect()
        try:
            res = con.execute(insert_data)
            print(res)
        except:
            return False
    return True

def getFavoritesSong(name):
    session_factory = get_session_factory(engine)
    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)
        songs = dbsession.query(Favorites.songId).filter(Favorites.username == name).all()
        songlist = []
        for song in songs:
            songlist.append(dbsession.query(Songs.name, Songs.directPath, Songs.id).filter(Songs.id == song[0]).all())

        test = []
        for s in songlist:
            test.append(s[0])
    return test

def getSongs(name):
    session_factory = get_session_factory(engine)
    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)
        albumId = dbsession.query(Albums.id).filter(Albums.name == name).first()[0]
        songs = dbsession.query(Songs.name, Songs.directPath, Songs.id).filter(Songs.albumId == albumId).all()  # поиск id альбома в бд по имени альбома
    return songs

def getAlbum(name):
    session_factory = get_session_factory(engine)
    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)
        albumId = dbsession.query(Albums.picturePath).filter(Albums.name == name).first()[0]
    return albumId

def getUser(id_, request):
    session_factory = get_session_factory(engine)
    dbsession = get_tm_session(session_factory, transaction.manager);
    if not id_:
        return {}
    u = dbsession.query(Users).get(id_)
    if u:
        return dbsession.query(Users).get(id_)
    else:
        return{}


from sqlalchemy.orm.exc import NoResultFound

def login(login, password):
    session_factory = get_session_factory(engine)
    dbsession = get_tm_session(session_factory, transaction.manager);
    print(login+" " +password)
    query = dbsession.query(Users).filter((Users.login == login) & (Users.password == password))
    try:
        u = query.one()
        print(u.login+" "+u.password)
        return u
    except NoResultFound:
        return None