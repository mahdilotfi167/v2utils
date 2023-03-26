# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$lg1ai-vvuxy@r7hieue&ky19nzo@!9*0c6a(1ca*^5=g@w)^0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ALLOWED_HOSTS = ['*']
