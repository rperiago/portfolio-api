from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from apps.users.forms import UserChange, UserCreation

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChange
    # add_form = UserCreation
    fieldsets = (("User", {"fields":
                               ("picture", "biography",  "newsletter")
                           }),) + auth_admin.UserAdmin.fieldsets
    list_display = ["id", "email", "name", "username", "is_superuser"]
    search_fields = ["name", "email"]
