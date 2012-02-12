from django import forms

from anitracker import models


class AnimalForm(forms.ModelForm):
    ''' Form for creating Animals '''

    class Meta:
        model = models.Animal

class SpecieTypeForm(forms.ModelForm):
    ''' Form for creating SpecieTypes '''
    animal = forms.ModelChoiceField(
        models.Animal.objects.all(),
        widget=forms.widgets.HiddenInput
    )

    class Meta:
        model = models.SpecieType

class PersonForm(forms.ModelForm):
    ''' Form for creating new people '''

    class Meta:
        model = models.Person

class AdmissionForm(forms.ModelForm):
    ''' Form for creating admissions '''

    class Meta:
        model = models.Admission
