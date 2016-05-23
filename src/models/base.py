from sqlalchemy import create_engine, Column, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Date, DateTime, String

from ..local_settings import DATABASE


engine = create_engine('postgres://{0}:{1}@{2}/{3}'.format(
    DATABASE.get('user'),
    DATABASE.get('pass'),
    DATABASE.get('host'),
    DATABASE.get('name')
))

Session = sessionmaker(bind=engine)

Base = declarative_base()

books_authors = Table(
    'books_authors',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('book_id', Integer, ForeignKey('book.id')),
    Column('author_id', Integer, ForeignKey('author.id'))
)


class TimestampMixin:
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())


class Topic(TimestampMixin, Base):
    __tablename__ = 'topic'
    topic = Column(String(100), nullable=False, unique=True, index=True)


class Book(TimestampMixin, Base):
    __tablename__ = 'book'
    title = Column(String(300), index=True, unique=True, nullable=False)
    publication_date = Column(Date, nullable=False)
    topic_id = Column(Integer, ForeignKey('topic.id'), nullable=False)
    topic = relationship('Topic')


class Author(TimestampMixin, Base):
    __tablename__ = 'author'
    first_name = Column(String(30), index=True, nullable=False)
    last_name = Column(String(30), index=True, nullable=False)
    books = relationship('Book', secondary=books_authors)
