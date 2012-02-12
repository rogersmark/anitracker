from django.shortcuts import render

from anitracker import forms


def index(request):
    animal_form = forms.AnimalForm()
    specie_form = forms.SpecieTypeForm()
    admission_form = forms.AdmissionForm()

    return render(request, 'anitracker/index.html', {
            'animal_form': animal_form,
            'specie_form': specie_form,
            'admission_form': admission_form
        })
