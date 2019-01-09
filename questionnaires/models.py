from django.db import models

from meetings.models import Meeting

class Quiz(models.Model):

    description = models.CharField(max_length=40)

    questionnaires_meeting = models.ForeignKey(Meeting, null=True, blank=True, on_delete=models.CASCADE)