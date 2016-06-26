from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

from .local_settings import DATABASE

engine = create_engine('postgres://{0}:{1}@{2}/{3}'.format(
    DATABASE.get('user'),
    DATABASE.get('pass'),
    DATABASE.get('host'),
    DATABASE.get('name')
))

Session = sessionmaker(bind=engine)
