from similarity import local_config


def create_db_url(db_config):
    return f"postgresql://{db_config['user']}:{db_config['pass']}@{db_config['host']}:{db_config['port']}/{db_config['db']}"


def get_env_db_url(selected_environment):
    if local_config.PSQL_LOCAL_SETTINGS[selected_environment]:
        return create_db_url(local_config.PSQL_LOCAL_SETTINGS[selected_environment])

    return None


# DB URLS for each Environment.
DEV_DB_URL = get_env_db_url('development')
TESTING_DB_URL = get_env_db_url('testing')
PROD_DB_URL = get_env_db_url('production')


class Config(object):
    # SQLAlchemy settings.
    SQLALCHEMY_DATABASE_URI = DEV_DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask Settings.
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = TESTING_DB_URL
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = PROD_DB_URL
    DEBUG = False
    TESTING = False
