import os


class Configuration(object):
      APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
      #DEBUG = True
      DEBUG = False
      SECRET_KEY = 'udZQM3mUB3AqX6dbeaAw3r4KD'
      STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')
