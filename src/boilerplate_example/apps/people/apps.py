from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PeopleConfig(AppConfig):
    name = 'boilerplate_example.apps.people'
    verbose_name = _('People')
    verbose_name_plural = _('People')
