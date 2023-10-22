from django.conf import settings
from django.core.mail import send_mail
from mailing.models import Mailing, Logs
from datetime import datetime, timedelta


def send_mailings(mailing):
    status_list = []
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


def start_mailing():
    mailings = Mailing.objects.all()
    print(mailings)
    for mailing in mailings:
        if mailing.status == Mailing.CREATED:
            obj = Logs.objects.filter(mailing=mailing).last()

            if obj is None:
                mail_time = mailing.datetime.replace(second=0, microsecond=0)
                now_time = datetime.now().time().replace(second=0, microsecond=0)
                if mail_time == now_time:
                    send_mailings(mailing)

            else:
                periodicity = mailing.periodicity
                obj_time = obj.change_time
                print(periodicity)
                print(obj_time)

                if periodicity == Mailing.DAY:
                    obj_time += timedelta(days=1)
                elif periodicity == Mailing.WEEK:
                    obj_time += timedelta(days=7)
                elif periodicity == Mailing.MONTH:
                    obj_time += timedelta(days=30)
                obj_time = obj_time.replace(second=0, microsecond=0)
                now_time = datetime.now().replace(second=0, microsecond=0)
                if obj_time == now_time:
                    send_mailings(mailing)
