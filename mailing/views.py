from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView

from mailing.forms import MailingChangeStatusForm, MessageForm, MailingForm
from mailing.models import Mailing, Message


class MailingListView(ListView):
    model = Mailing
    extra_context = {'title': 'Рассылки'}

    def get_queryset(self):
        if self.request.user.is_staff:
            return Mailing.objects.all()
        else:
            return Mailing.objects.filter(creator=self.request.user)


class MailingDetailView(DetailView):
    model = Mailing
    extra_context = {'title': 'Статья'}


def create_mailing(request):
    if request.method == 'POST':
        heading = request.POST.get('heading')
        content = request.POST.get('content')
        new_message = Message.objects.create(heading=heading, content=content)
        new_message.save()
        datetime = request.POST.get('datetime')
        new_mailing = Mailing.objects.create(datetime=datetime, message=new_message, creator=request.user)
        new_mailing.save()
    return render(request,'mailing/mailing_create.html')


class CreateMailingView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing')
    template_name = 'mailing/mailing_create.html'

    def _get_formset(self):
        MailingFormSet = inlineformset_factory(
            parent_model=Mailing,
            model=Message,
            form=MessageForm,
            exclude=('creator',),
            extra=1
        )

        if self.request.method == "POST":
            return MailingFormSet(self.request.POST, instance=self.object)
        return MailingFormSet(instance=self.object)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['formset'] = self._get_formset()
        return context_data

    def form_valid(self, form):
        mailing = form.save()
        mailing.creator = self.request.user
        mailing.save()
        return super().form_valid(form)


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing')


class MailingChangeStatusView(UpdateView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing')
    form_class = MailingChangeStatusForm


