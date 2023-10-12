from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import Users


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserForm(StyleFormMixin, UserCreationForm):

    class Meta:
        model = Users
        fields = ('email', 'password1', 'password2')


class ResetForm(StyleFormMixin, UserCreationForm):

    class Meta:
        model = Users
        fields = ('email',)


class UserChangeManagerForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Users
        fields = ('email', 'is_active',)
