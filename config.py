import os

class Config(object):
    USER = os.environ.get('POSTGRES_USER', 'egor')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', '123')
    HOST = os.environ.get('POSTGRES_HOST', '127.0.0.1')
    PORT = os.environ.get('POSTGRES_PORT', '1488')
    DB = os.environ.get('POSTGRES_DB', 'main')
    
    SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    SECRET_KEY = '1gh2452ljk346h1234ljk6h134jk'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    