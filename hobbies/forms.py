from django import forms
from .models import Hobbies


class HobbiesForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta:
        model = Hobbies
        fields = '__all__'
