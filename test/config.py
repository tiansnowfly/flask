import os
from datetime import timedelta
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SEND_FILE_MAX_AGE_DEFAULT = timedelta(seconds=1)
    TEMPLATES_AUTO_RELOAD = True  # 静态文件自动刷新
    DEBUG=True
