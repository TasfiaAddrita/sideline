from django.contrib.auth.models import User

# Create your models here.
class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # add more fields

    # to create permissions, use model Meta
    class Meta:
        permissions = [()]

    def __str__(self):
        return self.user.username


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # add more fields

    class Meta:
        permissions = [()]

    def __str__(self):
        return self.user.username
