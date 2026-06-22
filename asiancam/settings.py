"""
Django settings for AsianCam Website.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY

# For production, set DJANGO_SECRET_KEY in the server environment.

SECRET_KEY = os.getenv(
"DJANGO_SECRET_KEY",
"django-insecure-asiancam-local-development-key-change-later",
)

# Automatically True on Windows local PC and False on Linux server.

DEBUG = os.getenv(
"DJANGO_DEBUG",
"True" if os.name == "nt" else "False",
).lower() in ("1", "true", "yes")

ALLOWED_HOSTS = [
"5.223.90.183",
"127.0.0.1",
"localhost",
]

CSRF_TRUSTED_ORIGINS = [
"http://5.223.90.183:8004",
"http://127.0.0.1:8000",
"http://localhost:8000",
]

# APPLICATIONS

INSTALLED_APPS = [
"django.contrib.admin",
"django.contrib.auth",
"django.contrib.contenttypes",
"django.contrib.sessions",
"django.contrib.messages",
"django.contrib.staticfiles",


# Custom application
"company_news",


]

# MIDDLEWARE

MIDDLEWARE = [
"django.middleware.security.SecurityMiddleware",
"django.contrib.sessions.middleware.SessionMiddleware",
"django.middleware.common.CommonMiddleware",
"django.middleware.csrf.CsrfViewMiddleware",
"django.contrib.auth.middleware.AuthenticationMiddleware",
"django.contrib.messages.middleware.MessageMiddleware",
"django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "asiancam.urls"

# TEMPLATES

TEMPLATES = [
{
"BACKEND": "django.template.backends.django.DjangoTemplates",
"DIRS": [
BASE_DIR / "templates",
],
"APP_DIRS": True,
"OPTIONS": {
"context_processors": [
"django.template.context_processors.request",
"django.contrib.auth.context_processors.auth",
"django.contrib.messages.context_processors.messages",
],
},
},
]

WSGI_APPLICATION = "asiancam.wsgi.application"

# DATABASE

DATABASES = {
"default": {
"ENGINE": "django.db.backends.sqlite3",
"NAME": BASE_DIR / "db.sqlite3",
}
}

# PASSWORD VALIDATION

AUTH_PASSWORD_VALIDATORS = [
{
"NAME": (
"django.contrib.auth.password_validation."
"UserAttributeSimilarityValidator"
),
},
{
"NAME": (
"django.contrib.auth.password_validation."
"MinimumLengthValidator"
),
},
{
"NAME": (
"django.contrib.auth.password_validation."
"CommonPasswordValidator"
),
},
{
"NAME": (
"django.contrib.auth.password_validation."
"NumericPasswordValidator"
),
},
]

# LANGUAGE AND TIME

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Phnom_Penh"

USE_I18N = True

USE_TZ = True

# STATIC FILES

# Browser URL examples:

# /assets/css/style.css

# /assets/img/logo.png

# /assets/js/lang.js

STATIC_URL = "/assets/"

STATICFILES_DIRS = [
BASE_DIR / "assets",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

# MEDIA FILES

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"

# LOGIN AND LOGOUT

LOGIN_URL = "/admin/login/"

LOGIN_REDIRECT_URL = "/dashboard/news/"

LOGOUT_REDIRECT_URL = "/"

# DEFAULT PRIMARY KEY

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# HTTP SETTINGS

# Keep these False while using the IP address without HTTPS.

SECURE_SSL_REDIRECT = False

SESSION_COOKIE_SECURE = False

CSRF_COOKIE_SECURE = False

