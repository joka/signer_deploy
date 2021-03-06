# Django settings for signer example project.

DEBUG = False
TEMPLATE_DEBUG =False

ADMINS = (
#    ('Nico', 'nico@open-projects.net'),
    ('Joscha', 'joka@jokasis.de'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'db/test.db'             # Or path to database file if using sqlite3. 
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Berlin'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
#MEDIA_URL = 'http://petitions.open-projects.net'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'jbvl66t)9=4bxd9-d%yi!qat^sl^k!)4=ulg!*=&0_y$&+jn+k'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_cachepurge.middleware.CachePurge',
)

ROOT_URLCONF = 'signer_project.signer_project.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django_cachepurge',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'signer',
    'signer_facebook',
)

# signer
EMAIL_HOST = 'localhost'
BASE_URL = 'petitions.open-projects.net'
DEFAULT_FROM_EMAIL = 'petitions-no-answer@open-projects.net'
NR_RECOMMEND_EMAIL_FIELDS = 5

# signer_facebook
FACEBOOK_API_KEY = '6a8cd986779e2733a59d865120cce8a6'
FACEBOOK_SECRET_KEY = 'fab4b9bb3eaa09bb208d9947ac3e607e'
FACEBOOK_APP_NAME = 'petitionen' 

# django cachepurge
CACHE_URLS = 'http://127.0.0.1:8010'

try:
    from localsettings import *
except ImportError:
    pass
