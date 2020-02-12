from django.db import models
from django.urls import reverse

class Hobbies(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("hobbies-detail", kwargs={"pk": self.pk})

class Attend(models.Model):
    hobby = models.ForeignKey(Hobbies, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice

    