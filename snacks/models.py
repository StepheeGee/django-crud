# snacks/models.py
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

class Snack(models.Model):
    name = models.CharField(max_length=64, default='Steph\'s Goodies')
    rating = models.IntegerField(default=0)
    critical_description = models.TextField()
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=settings.DEFAULT_REVIEWER_ID)

    def __str__(self):
        return self.name
