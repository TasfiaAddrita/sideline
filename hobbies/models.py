from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Hobbies(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(max_length=1000, default="https://www.okea.org/wp-content/uploads/2019/10/placeholder.png")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("hobbies-detail", kwargs={"pk": self.pk})

class UserHobbies(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hobbies = models.ForeignKey(Hobbies, on_delete=models.SET_NULL, null=True)