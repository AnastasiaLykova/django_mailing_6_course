from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DeleteView, DetailView

from mailing.models import Mailing, Message


class MailingListView(ListView):
    model = Mailing
    extra_context = {'title': 'Рассылки'}

    def get_queryset(self):
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


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing')



