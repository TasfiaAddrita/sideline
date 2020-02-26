from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import Permission, User

from models import Instructor

class IntructorBackend(BaseBackend):

    def authenticate(self, request, **kwargs):
        instructor_id = kwargs['username']
        password = kwargs['password']
        try:
            instructor = Instructor.objects.get(instructor_id=instructor_id)
            if instructor.user.check_password(password) is True:
                return instructor.user

        except Instructor.DoesNotExit:
            user = User(username=username)
            user.is_staff = True
            user.save()
