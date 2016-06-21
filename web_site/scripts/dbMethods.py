import transaction
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    )
from ..models.mymodel import *


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,)
from sqlalchemy import create_engine
from pyramid.threadlocal import get_current_request

Base = declarative_base()
#DBSession = scoped_session(sessionmaker(), scopefunc=get_current_request)
engine = create_engine('sqlite:///web-site.sqlite')
#DBSession.configure(bind=engine)
Base.metadata.bind = engine
#Base.metadata.create_all(engine)

def getSongs(name):
    session_factory = get_session_factory(engine)
    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)
        albumId = dbsession.query(Albums.id).filter(Albums.name == name).first()[0]
        songs = dbsession.query(Songs.name, Songs.directPath).filter(Songs.albumId == albumId).all()  # поиск id альбома в бд по имени альбома
        #print(songs[0].directPath)
    return songs


def getUser(id_, request):
    #request for autorization, don't delete
    session_factory = get_session_factory(engine)
    #session = get_db_session()
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
    #session = get_db_session()
    dbsession = get_tm_session(session_factory, transaction.manager);
    query = dbsession.query(Users).filter(Users.login == login and Users.password == password)
    try:
        u = query.one()
        return u
    except NoResultFound:
        return None