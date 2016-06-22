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
Заполнение таблицы с альбомами
'''
def fillAlbums(dbsession):
    from ..models.mymodel import Albums
    from datetime import date
    currentDirectory = os.getcwd();  # абсолютный путь текущей директории
    path = '\static\Musics\\'
    dPath = '\web_site\static\Musics\\'
    fullPath = currentDirectory + dPath  # абсолютный путь до папки с музыкой
    dirList = os.listdir(path=fullPath)  # список альбомов в папке с музыкой
    for dir in dirList:
        #directPath = fullPath.replace(currentDirectory, "")  # относительный путь до альбома
        directPath = path
        #int(dir[0:4])
        dbsession.add(Albums(name=dir, releaseDate=date(2000, 1, 1), description="Запилить файлик с описанием", picturePath=directPath+dir+"\\Cover\\picture.jpg"))

'''
Заполнение таблицы с песнями
'''
def fillSongs(dbsession, engine):
    from ..models.mymodel import Songs
    from ..models.mymodel import Albums
    currentDirectory = os.getcwd(); # абсолютный путь текущей директории
    path = '\static\Musics\\'
    dPath = '\web_site\static\Musics\\'
    fullPath = currentDirectory + dPath # абсолютный путь до папки с музыкой
    dirList = os.listdir(path=fullPath) # список альбомов в папке с музыкой
    for dir in dirList:
        albumId = dbsession.query(Albums.id).filter(Albums.name == dir).first() # поиск id альбома в бд по имени альбома
        songsNames = os.listdir(path=fullPath+dir)
        for c in songsNames:
            if (c.find(".mp3")!=-1):
                #directPath = fullPath.replace(currentDirectory, "")  # относительный путь до песни
                directPath = path
                dbsession.add(Songs(name=c, albumId=albumId[0], directPath=directPath+dir+"\\"+c))


'''
Заполнение таблицы с пользовтелями
'''
def fillUsers(dbsession):
    from ..models.mymodel import Users
    from datetime import date
    list = []
    list.append(Users(login='admin', password='admin', age=date(1995, 1, 11), aboutYourself='Я есть админ'))
    list.append(Users(login='user', password='user', age=date(1997, 6, 5), aboutYourself='Я подопытный'))
    dbsession.add_all(list)

'''
Заполнение таблицы с картинками
'''
def fillPictures(dbsession):
    from ..models.mymodel import Pictures

'''
Заполнение таблицы с видео
'''
def fillVideos(dbsession):
    from ..models.mymodel import Videos

def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
    Base.metadata.create_all(engine)

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)

        fillAlbums(dbsession)
        fillSongs(dbsession, engine)
        fillUsers(dbsession)
