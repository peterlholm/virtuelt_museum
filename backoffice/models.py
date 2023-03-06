"Models for db"
from django.db import models

class MuseumTopic(models.Model):
    "Udstillingsgenstande"
    TopicNo = models.IntegerField()
    Titel = models.CharField(max_length=40)
    Manufacturer = models.CharField(max_length=40)
    Factual_text = models.CharField(max_length=400)
    Description = models.CharField(max_length=800)
    Long_Description = models.CharField(max_length=800, blank=True)
    Picture1_path = models.CharField(max_length=40, blank=True)
    Picture2_path = models.CharField(max_length=40, blank=True)
    Picture3_path = models.CharField(max_length=40, blank=True)
