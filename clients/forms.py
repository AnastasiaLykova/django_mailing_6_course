from django import forms
from clients.models import Clients
from users.forms import StyleFormMixin


class CreateClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Clients
        exclude = ('creator',)
