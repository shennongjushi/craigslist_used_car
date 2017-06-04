import os
SECRET_KEY = 'you-will-never-guess'
DEBUG = True
DB_USERNAME = 'shennongjushi'
DB_PASSWORD = ''
CAR_DATABASE_NAME = 'usedcar'
DB_HOST = os.getenv('IP', '0.0.0.0')
DB_URI = 'mysql+pymysql://%s:%s@%s/%s' % (DB_USERNAME, DB_PASSWORD, DB_HOST, CAR_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True