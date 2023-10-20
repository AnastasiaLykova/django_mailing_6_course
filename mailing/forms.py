from mailing.models import Mailing, Message
from users.forms import StyleFormMixin
from django import forms
from django.forms.models import inlineformset_factory, BaseInlineFormSet


class MailingChangeStatusForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Mailing
        fields = ('status',)


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class MailingForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Mailing
        fields = ('datetime','periodicity','status','clients',)


# MailingDetailFormSet = inlineformset_factory(parent_model=Mailing, model=Message,
#                                        form=forms.ModelForm, formset=BaseInlineFormSet,
#                                        fields='__all__',
#                                        extra=1)
