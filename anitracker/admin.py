from django.contrib import admin

from anitracker import models

class SpecieTypeInLine(admin.StackedInline):
    model = models.SpecieType

class AnimalAdmin(admin.ModelAdmin):
    inlines = [SpecieTypeInLine,]

admin.site.register(models.Animal, AnimalAdmin)
admin.site.register(models.Person)
admin.site.register(models.Admission)
admin.site.register(models.SpecieType)
