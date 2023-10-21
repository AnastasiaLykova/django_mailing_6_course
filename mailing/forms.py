from mailing.models import Mailing, Message
from clients.models import Clients
from users.forms import StyleFormMixin
from django import forms


class MailingChangeStatusForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Mailing
        fields = ('status',)


class MessageForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Message
        exclude = ('creator',)


class MailingForm(forms.ModelForm):

    clients = forms.ModelMultipleChoiceField(
        queryset=Clients.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Клиенты'
    )

    class Meta:
        model = Mailing
        exclude = ('creator',)
