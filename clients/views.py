from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from clients.forms import CreateClientForm
from clients.models import Clients


class ClientsListView(ListView):
    model = Clients

    def get_queryset(self):
        return Clients.objects.filter(creator=self.request.user)


class ClientsDetailView(DetailView):
    model = Clients

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.creator == self.request.user:
            return self.object
        else:
            return None


class ClientsCreateView(CreateView):
    model = Clients
    form_class = CreateClientForm
    success_url = reverse_lazy('clients:clients_list')

    def form_valid(self, form):
        client = form.save()
        client.creator = self.request.user
        client.save()
        return super().form_valid(form)


class ClientsUpdateView(UpdateView):
    model = Clients
    form_class = CreateClientForm

    def get_success_url(self):
        return reverse('clients:detail_client', args=[self.object.pk])

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.creator == self.request.user:
            return self.object
        else:
            return None


class ClientsDeleteView(DeleteView):
    model = Clients
    success_url = reverse_lazy('clients:clients_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.creator == self.request.user:
            return self.object
        else:
            return None