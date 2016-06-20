import os
import sys
import transaction

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    )
from ..models.mymodel import *

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)

'''
Заполнение таблицы с песнями
'''
def fillSongs(dbsession, engine):
    from ..models.mymodel import Songs
    from ..models.mymodel import Albums
    currentDirectory = os.getcwd(); # абсолютный путь текущей директории
    dPath = '\web_site\static\Musics\\'
    fullPath = currentDirectory + dPath # абсолютный путь до папки с музыкой
    dirList = os.listdir(path=fullPath) # список альбомов в папке с музыкой
    for dir in dirList:
        albumId = dbsession.query(Albums.id).filter(Albums.name == dir[7:]).first() # поиск id альбома в бд по имени альбома
        songsNames = os.listdir(path=fullPath+dir)
        for c in songsNames:
            if (c.find(".mp3")!=-1):
                directPath = fullPath.replace(currentDirectory, "")  # относительный путь до песни
                dbsession.add(Songs(name=c, albumId=albumId[0], directPath=directPath+dir+"\\"+c))

def getSongs(albim_name):


    return 1

def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)

        fillSongs(dbsession, engine)



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
        print(songs[0].directPath)
    return songs