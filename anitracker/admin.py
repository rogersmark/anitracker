from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError

from anitracker import models, utils


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'sub_type')
    search_fields = ('name', 'sub_type')

class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('General', {
            'fields': ('organization', 'first_name', 'last_name', 'person_type')
        }),
        ('Address', {
            'fields': ('address', 'address_two', 'city',
                'county', 'state', 'zipcode')
        }),
        ('Contact Information', {
            'fields': ('email', 'telephone')
        })
    )
    list_display = (
        'last_name',
        'first_name',
        'city',
        'county',
        'zipcode',
        'state',
        'person_type'
    )
    list_filter = ('person_type', )
    search_fields = ('last_name', 'county', 'zipcode')

class AdmissionAdminForm(forms.ModelForm):
    class Meta:
        model = models.Admission

    def clean_released_to(self):
        disp = self.cleaned_data['disposition']
        released_to = self.cleaned_data['released_to']
        if disp in models.Admission.RELEASED_STATES and not released_to:
            raise ValidationError(
                'Animal has been transferred or released, please select who'
                ' the animal was released to.'
            )
        return self.cleaned_data['released_to']


class AdmissionAdmin(admin.ModelAdmin):
    form = AdmissionAdminForm
    actions = (utils.export_to_csv, utils.export_to_xlsx)
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
    search_fields = (
        'received_from__last_name',
        'received_from__city',
        'received_from__county',
        'received_from__zipcode',
        'released_to__last_name',
        'released_to__city',
        'released_to__county',
        'released_to__zipcode',
        'animal__name',
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'released_to':
            kwargs['queryset'] = models.Person.objects.receivers

        if db_field.name == 'received_from':
            kwargs['queryset'] = models.Person.objects.finders

        return super(AdmissionAdmin, self).formfield_for_foreignkey(
                db_field, request, **kwargs)

admin.site.register(models.Animal, AnimalAdmin)
admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Admission, AdmissionAdmin)
