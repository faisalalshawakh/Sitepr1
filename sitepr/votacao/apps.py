from django.apps import AppConfig


class VotacaoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'votacao'

INSTALLED_APPS = [
    'votacao.apps.VotacaoConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]