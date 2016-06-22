from sqlalchemy import (
    Column,
    Index,
    Integer,
    UnicodeText,
    String,
    Date,
    ForeignKey
)

from .meta import Base

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String(30), unique=True, nullable=False)
    password = Column(String(30), nullable=False)
    # с полом проблемы, не даёт создать бд с неопределённым полом
    age = Column(Date)
    aboutYourself = Column(UnicodeText(1000))

class Artists(Base):
    __tablename__ = 'artists'
    id = Column(Integer, primary_key=True)
    fullName = Column(String(100), unique=True, nullable=False)
    age = Column(Date)
    history = Column(UnicodeText(1000))
    photoPath = Column(UnicodeText(200))  # путь до картинки

class Albums(Base):
    __tablename__ = 'albums'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False) # название
    releaseDate = Column(Date) # дата выхода
    description = Column(UnicodeText(1000)) # описание альбома
    picturePath = Column(UnicodeText(200)) # путь до картинки

class Songs(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True)
    #name = Column(String(100), unique=True, nullable=False) # название
    name = Column(String(100), nullable=False) # название
    albumId = Column(Integer, ForeignKey("albums.id"), nullable = False)
    directPath = Column(UnicodeText(200)) # путь до песни

class Pictures(Base):
    __tablename__ = 'pictures'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False) # название
    directPath = Column(UnicodeText(200)) # путь до фото

class Videos(Base):
    __tablename__ = 'videos'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False) # название
    directPath = Column(UnicodeText(200)) # путь до фото

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    username = Column(Integer, ForeignKey("users.id"), nullable=False)
    songId = Column(Integer, ForeignKey("songs.id"), nullable=False)  # название