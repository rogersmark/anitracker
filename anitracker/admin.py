from django.contrib import admin

from anitracker import models

admin.site.register(models.Animal)
admin.site.register(models.Person)
admin.site.register(models.Admission)
