# coding=utf-8
__author__ = 'stclaus'
import os

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

MAIL_SERVER = 'localhost'
MAIL_PORT = 10025
MAIL_USERNAME = None
MAIL_PASSWORD = None

ADMINS = ['voitenko@qarea.com']


POSTS_PER_PAGE = 2

WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULT = 50

LANGUAGES = {
    'en': 'English',
    'ru': 'Русский'
}