class Configuration(object):
    DATABASE = {
        'name': 'datacache.db',
        'engine': 'peewee.SqliteDatabase',
        'check_same_thread': False,
    }
    DEBUG = True
    SECRET_KEY = '9uiahsdf98haw904ijfoishjdgf98ahyaew'
    SECURITY_PASSWORD_SALT = 'j923f'
    SECURITY_USER_IDENTITY_ATTRIBUTES = 'username'
