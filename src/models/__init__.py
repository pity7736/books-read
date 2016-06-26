from sqlalchemy import create_engine, Column, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, mapper
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import ForeignKey, MetaData
from sqlalchemy.sql.sqltypes import Integer, Date, DateTime, String

from .topic import TopicModel
from .author import AuthorModel
from .book import BookModel


# Base = declarative_base()
metadata = MetaData()

books_authors = Table(
    'books_authors',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('book_id', Integer, ForeignKey('book.id')),
    Column('author_id', Integer, ForeignKey('author.id'))
)

topic = Table(
    'topic',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('created', DateTime, default=func.now()),
    Column('modified', DateTime, onupdate=func.now()),
    Column('name', String(100), nullable=False, unique=True, index=True)
)

author = Table(
    'author',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('created', DateTime, default=func.now()),
    Column('modified', DateTime, onupdate=func.now()),
    Column('first_name', String(40), index=True, nullable=False),
    Column('last_name', String(40), index=True, nullable=False)
)

book = Table(
    'book',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('created', DateTime, default=func.now()),
    Column('modified', DateTime, onupdate=func.now()),
    Column('title', String(300), index=True, unique=True, nullable=False),
    Column('publication_date', Integer, nullable=False),
    Column('read_date', Date, nullable=True),
    Column('topic_id', Integer, ForeignKey('topic.id'), nullable=False)
)

mapper(TopicModel, topic)
mapper(AuthorModel, author, properties={
    'books': relationship(BookModel, backref='book', secondary=books_authors)
})
mapper(BookModel, book, properties={
    'topic': relationship(TopicModel),
    'authors': relationship(AuthorModel, secondary=books_authors)
})
