from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView

from clients.models import Clients
from mailing.forms import MailingChangeStatusForm, MessageForm, MailingForm
from mailing.models import Mailing, Message, Logs


class MailingListView(ListView):
    model = Mailing
    extra_context = {'title': 'Рассылки'}

    def get_queryset(self):
        if self.request.user.is_staff:
            return Mailing.objects.all()
        else:
            return Mailing.objects.filter(creator=self.request.user)


class MessageListView(ListView):
    model = Message

    def get_queryset(self):
        if self.request.user.is_staff:
            return Message.objects.all()
        else:
            return Message.objects.filter(creator=self.request.user)


class LogsListView(ListView):
    model = Logs


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

    def form_valid(self, form):
        mailing = form.save()
        mailing.creator = self.request.user
        mailing.save()
        return super().form_valid(form)


class CreateMessageView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message')

    def form_valid(self, form):
        message = form.save()
        message.creator = self.request.user
        message.save()
        return super().form_valid(form)


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message')


class MailingChangeStatusView(UpdateView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing')
    form_class = MailingChangeStatusForm


