from django import forms

from anitracker import models


class AnimalForm(forms.ModelForm):
    ''' Form for creating Animals '''

    class Meta:
        model = models.Animal

class SpecieTypeForm(forms.ModelForm):
    ''' Form for creating SpecieTypes '''

    class Meta:
        model = models.SpecieType

class AdmissionForm(forms.ModelForm):
    ''' Form for creating admissions '''

    class Meta:
        model = models.Admission
