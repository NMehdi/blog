#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mehdi NOUI'
SITENAME = u'Datascience, what else'
SITESUBTITLE = u'(N)EVER (S)TOP LEARNING'
#SITEURL = 'http://www.nmehdiblog.com'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'
DEFAULT_DATE_FORMAT = '%d %b %Y'

DEFAULT_LANG = u'en'

DISPLAY_CATEGORIES_ON_MENU = False
FAVICON_FILENAME = "favicon.ico"
LOAD_CONTENT_CACHE = False
DELETE_OUTPUT_DIRECTORY = False

MENUITEMS = [('Machine Learning','/category/machine-learning'), ('Deep Learning','/category/deep-learning'), 
							('Natural Languge Processing','/category/nlp'), ('Recommandation Systems','/category/recommandation-systems')]

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'authors', 'archives', 'search'))

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
SOCIAL = (('github', 'https://github.com/NMehdi'),
                  ('linkedin', 'https://www.linkedin.com/in/mehdi-noui'),)

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
    'assets/CNAME': {'path': 'CNAME'},
	'assets/css/better_responsive_images.css': {'path': 'css/better_responsive_images.css'}
}

# Post and Pages path 
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'

PAGE_PATHS = ['pages']
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Archive path
ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path 
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
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
  'assets',
  'series',
   'tag_cloud',
   'liquid_tags.youtube',
   'liquid_tags.notebook',
   'liquid_tags.include_code',
   'render_math',
   'pelican-ipynb.markup',
   'related_posts', 
   'post_stats',
   'tipue_search'
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
DISQUS_SITENAME = "nmehdiblog"

#Github
GITHUB_URL = 'https://github.com/NMehdi/blog'

# Google Analytics
GOOGLE_ANALYTICS = "UA-118465736-1"

### Theme specific settings
# Copied from https://github.com/mingp/pelican-clean-blog-theme/blob/master/static/css/clean-blog.css
COLOR_SCHEME_CSS = 'github.css'
CSS_OVERRIDE = ['css/better_responsive_images.css']

AUTHORS_BIO = {
  "mehdi": {
    "name": "Mehdi N.",
    "cover": "assets/images/home-bg.jpg",
    "image": "assets/images/avatar.png",
    "website": "http://www.nmehdiblog.com",
    "location": "Paris",
    "bio": "• Data Scientist • Machine Learning • Python • R • NLP •",
    "github": "NMehdi",
    "linkedin": "mehdi-noui"
  }
}