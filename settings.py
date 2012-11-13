# -*- coding: utf-8 -*- #
from hashlib import md5

AUTHOR = u"Murat Çorlu"
AUTHOR_SHORTBIO = '''
I'm web developer at sahibinden.com. I love Javascript and Python.
'''
SITENAME = u"web development notes"
SITEURL = 'http://muratcorlu.com'
SITE_TAGLINE = u'by Murat Çorlu'
TIMEZONE = 'Europe/Istanbul'

GITHUB_URL = 'http://github.com/muratcorlu'
GITHUB_USERNAME = 'muratcorlu'
GITHUB_BADGE = True
DISQUS_SITENAME = 'muratcorlu'
AUTHOR_EMAIL = 'muratcorlu@gmail.com'
AUTHOR_EMAIL_HASH = md5(AUTHOR_EMAIL).hexdigest()
PDF_GENERATOR = False
REVERSE_CAREGORY_ORDER = True
LOCALE = ('usa', 'en_US')
DEFAULT_LANG = 'tr'
DEFAULT_PAGINATION = 5

THEME = "neat"

OUTPUT_PATH = 'output'
PATH = 'src'

STATIC_PATHS = ["images", ]

ARTICLE_URL = "posts/{slug}/"
ARTICLE_SAVE_AS = "posts/{slug}/index.html"

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
