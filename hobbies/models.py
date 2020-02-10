from django.db import models
from django.urls import reverse

class Hobbies(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("hobbies-detail", kwargs={"pk": self.pk})