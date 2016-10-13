from django.db import models
from django.contrib.sessions.models import Session
# Create your models here.
class Translations(models.Model):
  entered_text = models.TextField()
  language = models.TextField()
  translated_text = models.TextField()
  session = models.CharField(max_length=40)