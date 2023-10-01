from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from clients.models import Clients


class ClientsListView(ListView):
    model = Clients
    extra_context = {'title': 'Клиенты'}


class ClientsDetailView(DetailView):
    model = Clients
    extra_context = {'title': 'Клиента'}


class ClientsCreateView(CreateView):
    model = Clients
    fields = ('email', 'fullname', 'annotation', )
    success_url = reverse_lazy('clients:clients_list')


class ClientsUpdateView(UpdateView):
    model = Clients
    fields = ('email', 'fullname', 'annotation')

    def get_success_url(self):
        return reverse('clients:detail_client', args=[self.object.pk])


class ClientsDeleteView(DeleteView):
    model = Clients
    success_url = reverse_lazy('clients:clients')


