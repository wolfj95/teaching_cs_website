#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jacob Wolf'
SITENAME = 'Constructing Computer Science'
SITESUBTITLE = u'reflections on our first years as CS teachers'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Hong_Kong'

DEFAULT_LANG = 'en'

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

### Plugins

# PLUGIN_PATHS = [
#   'pelican-plugins'
# ]
#
# PLUGINS = [
#   'sitemap',
#   'neighbors',
#   'assets'
# ]

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

# Theme configurations

THEME = 'themes/attila'
HEADER_COLOR = '#414042'

COLOR_SCHEME_CSS = 'tomorrow.css'



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
LINKS = (('Constructing CS Repo', 'https://github.com/wolfj95/teaching_cs_website'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/myprofile'),
          ('github', 'https://github.com/jennylihan'))


AUTHORS_BIO = {
  "wolf": {
    "name": "Jacob Wolf",
    "cover": "white",
    "image": "https://avatars2.githubusercontent.com/u/36149703?s=460&v=4",
    "website": "https://github.com/wolfj95",
    "location": "Hong Kong",
    "bio": "a learner and a teacher, excited about education technology and passionate about education equity, one day hopes to start a school and/or a goat farm."
  }
}

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
