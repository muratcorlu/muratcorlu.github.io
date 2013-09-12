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
TWITTER_USERNAME = 'muratcorlu'
AUTHOR_EMAIL = 'muratcorlu@gmail.com'
AUTHOR_EMAIL_HASH = md5(AUTHOR_EMAIL).hexdigest()
PDF_GENERATOR = False
REVERSE_CAREGORY_ORDER = True
LOCALE = ('usa', 'en_US')
DEFAULT_LANG = 'tr'
DEFAULT_PAGINATION = 5
SITE_SOURCE = 'https://github.com/muratcorlu/muratcorlu.github.com/tree/source'

GOOGLE_ANALYTICS = 'UA-790007-1'

MD_EXTENSIONS = ['codehilite','extra','headerid']

THEME = "theme"

OUTPUT_PATH = 'output'
PATH = 'src'

STATIC_PATHS = ["images", ]

RELATIVE_URLS = False

ARTICLE_EXCLUDES = ('pages','drafts',)
ARTICLE_URL = "post/{slug}/"
ARTICLE_SAVE_AS = "post/{slug}/index.html"

<<<<<<< HEAD
=======
DISPLAY_PAGES_ON_MENU = True
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
PAGE_LANG_URL = "{lang}/{slug}/"
PAGE_LANG_SAVE_AS = "{lang}/{slug}/index.html"

>>>>>>> 3f0cb63bf982ce8e0b953398422086e1c2869f35
DEFAULT_PAGINATION = 10

FILES_TO_COPY = (('CNAME','',),)