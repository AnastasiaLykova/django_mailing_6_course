import random

from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserForm
from users.models import Users


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = Users
    form_class = UserForm
    success_url = reverse_lazy('mailing:mailing')
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