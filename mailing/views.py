from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView

from mailing.forms import MailingChangeStatusForm, MailingFormSet, MessageForm, MailingForm
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
    form_class = MailingFormSet
    success_url = reverse_lazy('service:list_mailing')
    template_name = 'mailing/mailing_create.html'


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing')


class MailingChangeStatusView(UpdateView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing')
    form_class = MailingChangeStatusForm


