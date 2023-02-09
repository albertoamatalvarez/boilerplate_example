import copy

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):

    def get_fieldsets(self, request, obj=None):
        fieldsets = copy.deepcopy(super().get_fieldsets(request, obj))
        # fieldsets that you can redefine
        # example:
        # fieldsets += (
        #     (_('person'), {
        #         'fields': ['person']}),
        # )
        return fieldsets
