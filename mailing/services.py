from django.conf import settings
from django.core.mail import send_mail
from mailing.models import Mailing, Logs


def send_mailings():
    status_list = []
    mailings = Mailing.objects.filter(status='created')
    for mailing in mailings:

        
        mail_list = mailing.clients.all()
        mailing.status = 'started'
        mailing.save()
        for client in mail_list:
            try:
                send_mail(
                    subject=mailing.message.heading,
                    message=mailing.message.content,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email],
                )
            except Exception as e:
                response = {'status': Logs.FAILED,
                            'response': 'Ошибка при отправке: {}'.format(str(e)),
                            'mailing': Mailing.objects.get(pk=mailing.id)}
                status_list.append(Logs(**response))
            else:
                response = {'status': Logs.SENT,
                            'response': 'Сообщение отправлено',
                            'mailing': Mailing.objects.get(pk=mailing.id)}
                status_list.append(Logs(**response))
        Logs.objects.bulk_create(status_list)
        mailing.status = 'completed'
        mailing.save()

