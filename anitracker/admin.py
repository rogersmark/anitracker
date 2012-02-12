from django.contrib import admin

from anitracker import models


class AdmissionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('date_of_admission', 'received_from')
        }),
        ('Animal Information', {
            'fields': ('animal', 'animal_age', 'disposition',
                'disposition_date', 'released_to')
        }),
        ('Misc.', {
            'fields': ('follow_up', 'notes')
        }),
    )
    list_filter = (
        'date_of_admission',
        'disposition',
        'follow_up',
        'animal_age',
        'animal__name'
    )
    list_display = ('date_of_admission', 'animal', 'disposition', 'follow_up')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'released_to':
            kwargs['queryset'] = models.Person.objects.receivers

        if db_field.name == 'received_from':
            kwargs['queryset'] = models.Person.objects.finders

        return super(AdmissionAdmin, self).formfield_for_foreignkey(
                db_field, request, **kwargs)
admin.site.register(models.Animal)
admin.site.register(models.Person)
admin.site.register(models.Admission, AdmissionAdmin)
