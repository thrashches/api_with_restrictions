from django.db import models


class MailingTask(models.Model):
    STATUS_CHOICES = [
        ('STARTED', 'started'),
        ('FINISHED', 'finished'),
        ('FAILED', 'failed'),
    ]

    started_at = models.DateTimeField(auto_now_add=True, verbose_name='время запуска')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              verbose_name='статус задачи', default='started')
    subject = models.CharField(max_length=255, verbose_name='тема рассылки')
    message = models.TextField(verbose_name='текст сообщения')

    def __str__(self):
        return f'{self.id}: {self.status}'
