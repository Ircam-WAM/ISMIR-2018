#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

SITENAME = "ISMIR 2018" 
SITEURL = 'http://ismir2018.ircam.fr'
# AUTHOR = 'Guillaume Pellerin'
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#THEME = '/srv/lib/pelican-themes/flex'
THEME = '/srv/lib/pelican-themes/pelican-chameleon'
#THEME = '/Users/peeters/Dropbox/_work/_develop/_python/_pelican/pelican-themes/flex2'
#THEME = '/Users/peeters/Dropbox/_work/_develop/_python/_pelican/pelican-themes/pelican-bootstrap3'
#BOOTSTRAP_THEME = 'united'
BOOTSTRAP_THEME = 'yeti'

BS3_THEME = 'http://bootswatch.com/cosmo/bootstrap.min.css'

LOAD_CONTENT_CACHE = False

MAIN_MENU = True
LINKS = (('Portfolio', '//alexandrevicenzi.com'),)

SOCIAL = (('linkedin', 'https://br.linkedin.com/in/test'),
          ('github', 'https://github.com/test'),
          ('google', 'https://google.com/+Test'),
          ('rss', '//www.example.com/feeds/all.atom.xml'))

#MENUITEMS = (('Archives', '/archives.html'),
#             ('Categories', '/categories.html'),
#             ('Tags', '/tags.html'),)

#USE_LESS = True
#SITELOGO = '/images/ismir2018logo_black_short_L200.png'
#SITELOGOLONG = '/images/ismir2018logo_black_long.png'

BANNER = '/images/ismir2018logo_black_long_empty.png'
BANNER_SUBTITLE = 'September 23-27, Paris, France'
BANNER_ALL_PAGES = True
HIDE_SIDEBAR = False
DISPLAY_PAGES_ON_MENU = True
BOOTSTRAP_NAVBAR_INVERSE = False
DISPLAY_ARTICLE_INFO_ON_INDEX = False
USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
# CUSTOM_CSS = 'themes/bootswatch/slate/slate/bootstrap.css'

doLocal = False

if doLocal:
    PATH = '/Users/peeters/Dropbox/_work/_develop/_python/_pelican/var/in'
    OUTPUT_PATH = '/Users/peeters/Dropbox/_work/_develop/_python/_pelican/output/'
else:
    PATH = '/var/in'
    OUTPUT_PATH = '/var/out'

if not os.path.exists(PATH) and not os.path.exists(OUTPUT_PATH):
    PATH = '/var/in'
    OUTPUT_PATH = '/var/out'


STATIC_PATHS = ['doc', 'images', 'extra']

TIMEZONE = 'Europe/Paris'
#
DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'


SUMMARY_MAX_LENGTH = 127
SLUGIFY_SOURCE = 'title'
# DEFAULT_PAGINATION = 5

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

MENUITEMS = [
('Home', '/'),
('Important Dates', '/pages/important-dates.html'),
('Participants', [
    ('Venue', '/pages/participants-venue.html'),
    ('Registration', '/pages/participants-registration.html'),
    ]),
('Events-Main', [
    ('All events at a glance', '/pages/events-at-a-glance.html'),
    ('Call for Participation', '/pages/events-call.html'),
    ]),
('Events-Satelitte', [
    ]),
('Partners', [
    ('Become an Industry Partner', '/pages/partners-call.html'),
    ]),
('About', [
    ('About ISMIR', '/pages/about-ismir.html'),
    ('Organizing Committee', '/pages/about-organizing-committee.html'),
    ]),
]
FAVICON_TYPE = 'png'
FAVICON = '/images/ismir2018logo_black_long.png'

# Blogroll
LINKS =  (('Télécom ParisTech', 'https://www.telecom-paristech.fr/'),
            ('Ircam', 'http://www.ircam.fr'),
            ('ismir.net', 'http://www.ismir.net/'),
            ('WiMIR', 'https://wimir.wordpress.com/'),
          )

# Social widget
#SOCIAL = (('Twitter', 'https://twitter.com/Ircam/'),
#          ('GitHub', 'https://github.com/Ircam-RnD/'),
#          )
SOCIAL = ()

#DISQUS_SITENAME='ismir2018'
GITHUB_USER = 'ismir2018'
TWITTER_CARDS = False
TWITTER_USERNAME = 'ismir2018'
TWITTER_WIDGET_ID = '516222825451888640'

if doLocal:
    PLUGIN_PATHS = ['/Users/peeters/Dropbox/_work/_develop/_python/_pelican/pelican-plugins/']
else:
    PLUGIN_PATHS = ['/srv/lib/pelican-plugins']

PLUGINS = ['assets', 'jinja2content', 'sitemap', 'gallery',
            # 'i18n_subsites',
            'render_math',
            'neighbors',
        #    'liquid_tags.img', 'liquid_tags.video',
        #    'liquid_tags.youtube', 'liquid_tags.vimeo',
        #    'liquid_tags.include_code',
        #    'liquid_tags.notebook',
           ]

SITEMAP = {

    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Content licensing: CC-BY
CC_LICENSE = "CC-BY"

# GOOGLE_ANALYTICS = 'UA-6573030-16'

GALLERY_PATH = '/var/in/img/gallery/'

PELICANGIT_SOURCE_REPO=PATH
PELICANGIT_SOURCE_REMOTE="origin"
PELICANGIT_SOURCE_BRANCH="master"

PELICANGIT_DEPLOY_REPO=OUTPUT_PATH
PELICANGIT_DEPLOY_REMOTE="origin"
PELICANGIT_DEPLOY_BRANCH="master"
PELICANGIT_DEPLOY_IS_LOCAL_DIR = True

PELICANGIT_USER = "root"
PELICANGIT_WHITELISTED_FILES = [
    "README.md"
]

PELICANGIT_PORT=8888

MARKDOWN = {'extensions': ['markdown.extensions.meta',]}
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.tables':{},
    }
}

# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n',]}

# I18N_SUBSITES = {
#     'fr': {
#         'SITENAME': 'Musique et hacking',
#         }
#     }

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/custom.js': {'path': 'static/js/custom.js'}
}

SHOW_DATE_MODIFIED = False

FAVICON = ''
