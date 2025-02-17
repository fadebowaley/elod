import os


class Config(object):
    """
    Common configurations
    """
    SECRET_KEY = os.urandom(16)
    ASSETS_DEBUG = True
    CSRF_ENABLED = True

class DoleAppConfig(Config):
    """
    Configurations
    """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_ECHO = True
    test_directory_path = os.path.dirname(os.path.realpath(__file__))
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(test_directory_path, 'dole_app_db.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dole_app_db.db'

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_BINDS = {
        "test": 'sqlite:///' + os.path.join(test_directory_path, 'dole_app_db.db')
    }

app_config = {
    'config': DoleAppConfig
}
