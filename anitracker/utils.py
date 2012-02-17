import tablib

from django.http import HttpResponse

HEADERS = [
    'Admission Date',
    'Finder First Name',
    'Finder Last Name',
    'Finder Address',
    'Finder Address Two',
    'Finder City',
    'Finder County',
    'Finder State',
    'Finder Zipcode',
    'Finder Telephone',
    'Finder Email',
    'Animal',
    'Animal SubType',
    'Animal Age',
    'Disposition',
    'Disposition Date',
    'Rehabber First Name',
    'Rehabber Last Name',
    'Rehabber Address',
    'Rehabber Address Two',
    'Rehabber City',
    'Rehabber County',
    'Rehabber State',
    'Rehabber Zipcode',
    'Rehabber Telephone',
    'Rehabber Email'
    'Follow Up',
    'Notes',
]

def gather_person_data(person=None):
    ''' Convert a person object to an array of data for export '''
    if not person:
        return ['', '', '', '', '', '', '', '', '']

    return [
        person.last_name,
        person.first_name,
        person.address,
        person.address_two,
        person.city,
        person.county,
        person.state,
        person.zipcode,
        person.telephone,
        person.email,
    ]

def gather_export_data(queryset):
    ''' Gather up admission info into an exportable format '''
    data = []
    for admission in queryset:
        released_data = gather_person_data(admission.released_to)
        received_data = gather_person_data(admission.received_from)
        row = [admission.date_of_admission, ]
        row += received_data
        row.append(admission.animal.name)
        row.append(admission.animal.sub_type)
        row.append(admission.disposition)
        row.append(admission.disposition_date)
        row += released_data
        row.append(admission.follow_up)
        row.append(admission.notes)
        data.append(row)

    dataset = tablib.Dataset(*data, headers=HEADERS)
    return dataset

def export_to_csv(modeladmin, request, queryset):
    ''' Export to CSV functionality for Admissions '''
    dataset = gather_export_data(queryset)
    response = HttpResponse(
        dataset.csv,
        mimetype='text/csv',
        content_type='text/csv; charset=utf-8'
    )
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % 'wildlife'
    return response

def export_to_xlsx(modeladmin, request, queryset):
    ''' Export to XSLX functionality for Admissions '''
    dataset = gather_export_data(queryset)
    response = HttpResponse(
        dataset.xlsx,
        mimetype='application/ms-excel',
    )
    response['Content-Disposition'] = 'attachment; filename=%s.xlsx' % 'wildlife'
    return response

export_to_xlsx.short_description = 'Export Selected Admissions to Excel'
export_to_csv.short_description = 'Export Selected Admissions to CSV'
