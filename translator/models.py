from django.db import models
from django.contrib.sessions.models import Session
# Create your models here.
class Translations(models.Model):
  original_text = models.TextField()
  language = models.TextField()
  translated_text = models.TextField()

  def __str__(self):
    return self.original_text