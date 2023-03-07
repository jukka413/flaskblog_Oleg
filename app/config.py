class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/for_flask'
    SECRET_KEY = 'Very Secret'

    SECURITY_PASSWORD_SALT = 'refd;sla'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'