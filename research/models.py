from django.db import models

class Request (models.Model):
  url = models.CharField(max_length=100)
  params = models.CharField(max_length=100)
  def __str__(self):
    return self.url + "?" + self.params
