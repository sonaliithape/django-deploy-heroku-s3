from settings import PROJECT_ROOT, SITE_ROOT
import os

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
	'default': {
	    'ENGINE': 'django.db.backends.mysql',
	    'NAME': 'django-db',
	    'USER': 'root',
	    'PASSWORD': 'password',
	}

}

