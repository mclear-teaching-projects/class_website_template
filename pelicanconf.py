#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Colin McLear'
SITENAME = u'Philosophy 101'
SITEURL = ''
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'
PATH = 'content'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# CACHE SETTINGS ########
# CACHE_CONTENT = True
# CACHE_PATH = '/Users/Roambot/Dropbox/Personal/bin/phil101/cache'
# AUTORELOAD_IGNORE_CACHE = True
# LOAD_CONTENT_CACHE = True
# CHECK_MODIFIED_METHOD = 'mtime'


# THEME SETTINGS ########
THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME='simplex'
BOOTSTRAP_NAVBAR_INVERSE = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('Resources', '/.html'),
    ('Schedule', '/.html'),
    ('Syllabus', '/syllabus.html'),
    ('Contact', '/.html'),
    # ('Tags', '/tags.html'),
    # ('Home', '/'),
    # ('Category1', 'category/category1.html'),
    # ('Category2', 'category/category2.html'),
)

CC_LICENSE = "CC-BY-NC-SA"
GOOGLE_ANALYTICS = 'UA-30497236-1'
CUSTOM_CSS = 'static/custom.css'

# Tell Pelican to add 'extra/custom.css' to the output dir
STATIC_PATHS = ['images', 'extra/custom.css']
# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'}
}


# Plugins ##########
PLUGIN_PATHS = ['/Users/Roambot/Dropbox/Personal/bin/pelican-plugins']
PLUGINS = ['org_pandoc_reader', 'assets', 'tipue_search', 'tag_cloud', 'neighbors', 'extract_toc']

ORG_PANDOC_ARGS = [
    '--filter=/usr/local/bin/pandoc-citeproc',
    '--base-header-level=2',
    '--bibliography=/Users/Roambot/Dropbox/Work/Master.bib',
    '--mathjax',
    '--toc',
    '--toc-depth=5',
  ]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Tags

TAG_CLOUD = True
DISPLAY_TAGS_ON_SIDEBAR= True
DISPLAY_TAGS_INLINE = True
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100
# TAG_CLOUD_SORTING = 'random'


# Blogroll
LINKS = (
        ('Blackboard', 'https://my.unl.edu/webapps/portal/frameset.jsp'),
        ('UNL Philosophy', 'http://www.unl.edu/philosophy/'))

# Social widget
# SOCIAL = (
#           ('twitter', 'http://twitter.com/mclearc'),
#           ('github', 'https://github.com/mclearc'),
#           ('facebook', 'https://www.facebook.com/?_rdr=p'),
#           )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
