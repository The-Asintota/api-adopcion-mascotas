import dj_database_url
from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = [
    config("CLIENT_HOST", cast=str),
    config("TEST_HOST", cast=str),
    config("SERVER_HOST", cast=str),
]

CSRF_TRUSTED_ORIGINS = [
    f"https://{config('SERVER_HOST', cast=str)}",
    f"https://{config('TEST_HOST', cast=str)}",
    f"https://{config('CLIENT_HOST', cast=str)}",
]

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True


# CORS settings
CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = [
    f"https://{config('CLIENT_HOST', cast=str)}",
    f"https://{config('TEST_HOST', cast=str)}",
]


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    "default": dj_database_url.config(
        default=config("POSTGRE_DB_URL", cast=str),
        engine="django.db.backends.postgresql",
    ),
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_ROOT = Path.joinpath(BASE_DIR, "staticfiles")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
