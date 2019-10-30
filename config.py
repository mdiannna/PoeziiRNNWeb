import os

# # Configure database
# basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	pass
#     # ...
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#         'sqlite:///' + os.path.join(basedir, 'app.db')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configure secret key
SECRET_KEY = '48cefb4d36a7f5f7e42ec2cd'