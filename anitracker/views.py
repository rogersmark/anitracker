import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from anitracker import forms, models


def index(request):
    animal_form = forms.AnimalForm(prefix='animal')
    specie_form = forms.SpecieTypeForm(prefix='specie')
    released_person_form = forms.PersonForm(prefix='released')
    finder_form = forms.PersonForm(prefix='finder')
    form = forms.AdmissionForm()

    if request.method == 'POST':
        animal = None
        specie = None
        released_to = None
        finder = None
        admission = models.Admission()

        animal_form = forms.AnimalForm(request.POST, prefix='animal')
        specie_form = forms.SpecieTypeForm(request.POST, prefix='specie')
        released_person_form = forms.PersonForm(request.POST,
            prefix='released')
        finder_form = forms.PersonForm(request.POST, prefix='finder')

        if animal_form.is_valid():
            animal = animal_form.save()
            admission.animal = animal

        if specie_form.is_valid():
            specie = specie_form.save()
            admission.animal_subtype = specie

        if released_person_form.is_valid():
            released_to = released_person_form.save()
            admission.released_to = released_to

        if finder_form.is_valid():
            finder = finder_form.save()
            admission.received_from = finder

        form = forms.AdmissionForm(request.POST, instance=admission)
        import ipdb; ipdb.set_trace() ### XXX BREAKPOINT
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'anitracker/index.html', {
            'animal_form': animal_form,
            'specie_form': specie_form,
            'finder_form': finder_form,
            'released_person_form': released_person_form,
            'form': form
        })

def specie_type_json(request):
    ''' Takes animal PK, returns SpecieTypes tied to Animal '''
    animal = get_object_or_404(
        models.Animal,
        pk=request.GET.get('animal_pk') or -1)
    json_data = {
        'specie_types': [(x.pk, x.name) for x in animal.specietype_set.all()]
    }
    return HttpResponse(json.dumps(json_data), mimetype='application/json')
