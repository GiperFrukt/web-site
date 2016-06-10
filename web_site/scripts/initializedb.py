import os
import sys
import transaction

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
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

def fillAlbums():
    from ..models.mymodel import Albums

def fillSongs():
    from ..models.mymodel import Songs

def fillArtists():
    from ..models.mymodel import Artists

def fillUsers(dbsession):
    from ..models.mymodel import Users
    from datetime import date
    list = []
    list.append(Users(login='admin', password='admin', age=date(1995, 1, 11), aboutYourself='Я есть админ'))
    list.append(Users(login='user', password='user', age=date(1997, 6, 5), aboutYourself='Я подопытный'))
    dbsession.add_all(list)

def fillPictures():
    from ..models.mymodel import Pictures

def fillVideos():
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

        fillUsers(dbsession)
        model = MyModel(name='one', value=1)
        dbsession.add(model)
