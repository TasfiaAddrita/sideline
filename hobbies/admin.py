from django.contrib import admin
from hobbies.models import Hobbies

class HobbiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created', 'modified')


admin.site.register(Hobbies, HobbiesAdmin)
