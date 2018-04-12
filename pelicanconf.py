#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'NMehdi'
SITENAME = u'Datascience, what else'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'
DEFAULT_DATE_FORMAT = '%d %b %Y'

DEFAULT_LANG = u'en'

LOAD_CONTENT_CACHE = False
DELETE_OUTPUT_DIRECTORY = False
MENUITEMS = [('Machine Learning','/category/machine-learning'), ('Deep Learning','/category/deep-learning'), 
							('Natural Languge Processing','/category/nlp'), ('Recommandation Systems','/category/recommandation-systems')]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# Pagination
DEFAULT_PAGINATION = 3
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['assets']

EXTRA_PATH_METADATA = {
    'assets/robots.txt': {'path': 'robots.txt'},
    'assets/favicon.ico': {'path': 'favicon.ico'},
    'assets/CNAME': {'path': 'CNAME'}
}

# Post and Pages path 
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Archive path
ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path 
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'catgegories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'

# Theme
THEME = 'pelican-themes/attila-master'

### Plugins
PLUGIN_PATHS = [
  'pelican-plugins'
]

PLUGINS = [
  'sitemap', 
  'neighbors', 
  'assets'
]

# Sitemap
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

# Comments
DISQUS_SITENAME = "datascience-whatelse"

### Theme specific settings

COLOR_SCHEME_CSS = 'github.css'

CSS_OVERRIDE = ['assets/css/myblog.css']

AUTHORS_BIO = {
  "NMehdi": {
    "name": "NMehdi",
    "cover": "assets/images/avatar.png",
	"image": "assets/images/avatar.png",
    "website": "https://nmehdi.github.io/blog",
    "location": "Paris",
    "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
	 #"linkedin": "https://www.linkedin.com/in/johnsobanski/",
    #"github": "https://github.com/hatdropper1977",
  }
 }
