from django.contrib.auth import get_user_model
from django.core.mail import send_mass_mail
from django.conf import settings
from celery import shared_task
from .models import MailingTask

User = get_user_model()


@shared_task
def start_mailing(subject: str, message: str, task_id: int):
    task = MailingTask.objects.get(id=task_id)
    recipient_list = [u.email for u in User.objects.all() if u.email]
    from_email = settings.DEFAULT_FROM_EMAIL
    try:
        send_mass_mail(((subject, message, from_email, recipient_list),))
        task.status = 'finished'
    except Exception:
        # В случе если send_mass_email вызовет исключение, задача пометится как проваленная.
        task.status = 'failed'
    task.save()
