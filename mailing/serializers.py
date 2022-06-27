from rest_framework import serializers
from .models import MailingTask


class MailingTaskSerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField()

    class Meta:
        model = MailingTask
        fields = '__all__'
