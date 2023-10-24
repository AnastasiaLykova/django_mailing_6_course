import random

from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from users.forms import UserForm, UserChangeManagerForm
from users.models import Users


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = Users
    form_class = UserForm
    success_url = reverse_lazy('users:verify')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        verify_key = ''.join([str(random.randint(0, 9)) for _ in range(5)])
        send_mail(
            subject='верификация',
            message=f'код {verify_key}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],
        )
        new_user.verify_key = verify_key
        new_user.save()
        return super().form_valid(form)


def verify_key(request):
    if request.method == 'POST':
        ver_key = request.POST.get('key')
        user_email = request.POST.get('email')
        user_verify = Users.objects.get(email=user_email)
        if user_verify.verify_key == ver_key:
            user_verify.is_verified = True
            user_verify.save()
    return render(request, 'users/verify.html')


class UsersListView(ListView):
    permission_required = "users.view_users"
    model = Users


class UsersDetailView(DetailView):
    permission_required = "users.view_users"
    model = Users


class UsersActiveUpdateView(UpdateView):
    permission_required = "users.change_users"
    model = Users
    form_class = UserChangeManagerForm

    def get_success_url(self):
        return reverse('users:detail_user', args=[self.object.pk])


class UsersUpdateView(UpdateView):
    model = Users
    form_class = UserForm

    def get_success_url(self):
        return reverse('users:detail_user', args=[self.object.pk])

    def get_queryset(self):
        return Users.objects.filter(email=self.request.user.email)
