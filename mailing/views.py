from rest_framework import viewsets, mixins
from .models import MailingTask
from .serializers import MailingTaskSerializer
from .tasks import start_mailing


class MailingTaskViewSet(mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    queryset = MailingTask.objects.all()
    serializer_class = MailingTaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        start_mailing.delay(task.subject, task.message, task.id)
