from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms

User = get_user_model()


class UserChange(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ('username', 'email', 'newsletter', 'picture')
        model = User


class UserCreation(UserCreationForm):
    newsletter = forms.BooleanField(initial=True, required=False)
    email = forms.EmailField(label='Email', required=True)
    error_message = UserCreationForm.error_messages.update(
        {
            "duplicate_username": _("This username has already been taken."),
            "duplicate_email": _("This email has already been taken."),
        }
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'newsletter')

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).count() > 0:
            raise ValidationError(self.error_messages["duplicate_email"])
        return data
