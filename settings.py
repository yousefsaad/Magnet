import os

SECRET_KEY = "b'\xf9\x07K\xc2\x11\x9ee\xd4\x8a\xe3\x91\xd9\x88\xca\xba\x1d\xb2\x9d\xb5\xdb\x82;\xd6\xd4'"
DEBUG = True

####################################################################
DB_USERNAME = 'root'
DB_PASSWORD = 'AGmysql--'

BLOG_DATABASE_NAME = 'magnet'
DB_HOST = os.getenv('IP','127.0.0.1')
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True



################################################################

#for aws db settings 
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)
# QLALCHEMY_DATABASE_URI = 'mysql+pymysql://magnet:Magnet123--@magnethms.cqrzi7laicv7.us-west-2.rds.amazonaws.com:3306.amazonaws.com:3306/magnet'

# SQLALCHEMY_TRACK_MODIFICATIONS = True

# SQLALCHEMY_POOL_RECYCLE = 3600

# WTF_CSRF_ENABLED = True



