from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField, BooleanField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    picture = ImageField(_("Picture"), upload_to='image/%Y/', null=True, blank=True)
    biography = CharField(_("biography"), blank=True, null=True, max_length=500)
    newsletter = BooleanField(_('Newsletter subscribe'), default=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
