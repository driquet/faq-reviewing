#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'The Publisher'
SITENAME = 'Foire aux Questions - Reviewing'
SITEURL = ''
THEME = 'nest'

PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('Twitter', 'https://www.twitter.com/driquet'),
          ('Github', 'https://github.com/driquet/'),
          ('Google Plus', 'https://plus.google.com/106515306465580046991/posts'))

DEFAULT_PAGINATION = 10
TWITTER_USERNAME = 'driquet'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# NEST Template
NEST_CSS_MINIFY = False
# Add items to top menu before pages
MENUITEMS = [('Accueil', '/'),('Sommaire','/pages/sommaire.html'),('À propos', '/pages/a-propos.html')]
NEST_HEADER_IMAGES = ''
NEST_HEADER_LOGO = '/images/logo.gif'
# Footer
NEST_SITEMAP_COLUMN_TITLE = u'Sitemap'
NEST_SITEMAP_MENU = [('Archives', '/archives.html'),('Catégories', '/categories.html'), ('Tags','/tags.html'), ('Auteurs','/authors.html')]
NEST_SITEMAP_ATOM_LINK = u'Atom Feed'
NEST_SITEMAP_RSS_LINK = u'RSS Feed'
NEST_SOCIAL_COLUMN_TITLE = u'Social'
NEST_LINKS_COLUMN_TITLE = u'Links'
NEST_COPYRIGHT = u'&copy; The Publisher / driquet 2016'
# Footer optional
NEST_FOOTER_HTML = ''
# index.html
NEST_INDEX_HEAD_TITLE = u'Accueil'
NEST_INDEX_HEADER_TITLE = u'Reviewing Geocaching - Questions/Réponses'
NEST_INDEX_HEADER_SUBTITLE = u"""Bienvenue sur ce site, qui a pour ambition de proposer des éléments de réponses pour un certain nombre de questions récurrentes liées à la publication de caches.
L'ensemble des éléments de réponse sont présentés sur la page <a href=\"/pages/sommaire.html\">Sommaire</a>.<br/>
Pour en savoir plus sur cette initiative, rendez-vous sur la page <a href=\"/pages/a-propos.html\">À propos</a>."""
NEST_INDEX_CONTENT_TITLE = u'Dernières publications'
# archives.html
NEST_ARCHIVES_HEAD_TITLE = u'Archives'
NEST_ARCHIVES_HEAD_DESCRIPTION = u'Posts Archives'
NEST_ARCHIVES_HEADER_TITLE = u'Archives'
NEST_ARCHIVES_HEADER_SUBTITLE = u'Archives de tous les articles'
NEST_ARCHIVES_CONTENT_TITLE = u'Archives'
# article.html
NEST_ARTICLE_HEADER_BY = u'Par'
NEST_ARTICLE_HEADER_MODIFIED = u'mis à jour le'
NEST_ARTICLE_HEADER_IN = u'dans la catégorie'
# author.html
NEST_AUTHOR_HEAD_TITLE = u'Articles de'
NEST_AUTHOR_HEAD_DESCRIPTION = u'Articles de'
NEST_AUTHOR_HEADER_SUBTITLE = u'Archive de publications'
NEST_AUTHOR_CONTENT_TITLE = u'Publications'
# authors.html
NEST_AUTHORS_HEAD_TITLE = u'Liste des auteurs'
NEST_AUTHORS_HEAD_DESCRIPTION = u'Liste des auteurs'
NEST_AUTHORS_HEADER_TITLE = u'Liste des auteurs'
NEST_AUTHORS_HEADER_SUBTITLE = u'Archives des publications par auteur'
# categories.html
NEST_CATEGORIES_HEAD_TITLE = u'Catégories'
NEST_CATEGORIES_HEAD_DESCRIPTION = u'Archives par catégorie'
NEST_CATEGORIES_HEADER_TITLE = u'Catégories'
NEST_CATEGORIES_HEADER_SUBTITLE = u'Archives par catégorie'
# category.html
NEST_CATEGORY_HEAD_TITLE = u'Catégorie'
NEST_CATEGORY_HEAD_DESCRIPTION = u'Catégorie'
NEST_CATEGORY_HEADER_TITLE = u'Catégorie'
NEST_CATEGORY_HEADER_SUBTITLE = u'Archive de la catégorie'
# pagination.html
NEST_PAGINATION_PREVIOUS = u'Précédent'
NEST_PAGINATION_NEXT = u'Suivant'
# period_archives.html
NEST_PERIOD_ARCHIVES_HEAD_TITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_HEAD_DESCRIPTION = u'Archives for'
NEST_PERIOD_ARCHIVES_HEADER_TITLE = u'Archives'
NEST_PERIOD_ARCHIVES_HEADER_SUBTITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_CONTENT_TITLE = u'Archives for'
# tag.html
NEST_TAG_HEAD_TITLE = u'Archives du tag'
NEST_TAG_HEAD_DESCRIPTION = u'Archive du tag'
NEST_TAG_HEADER_TITLE = u'Tag'
NEST_TAG_HEADER_SUBTITLE = u'Archives du tag'
# tags.html
NEST_TAGS_HEAD_TITLE = u'Tags'
NEST_TAGS_HEAD_DESCRIPTION = u'Liste des tags'
NEST_TAGS_HEADER_TITLE = u'Tags'
NEST_TAGS_HEADER_SUBTITLE = u'Liste des tags'
NEST_TAGS_CONTENT_TITLE = u'Liste des tags'
NEST_TAGS_CONTENT_LIST = u'tagged'
