from django.db import models
from django.contrib.localflavor.us.models import (
    PhoneNumberField,
    USStateField
)

class BaseModel(models.Model):
    ''' Simple base model class to inherit from '''

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Animal(BaseModel):
    ''' Animal that was brought into center '''

    name = models.CharField(max_length=256)
    sub_type = models.CharField(max_length=256)

    def __unicode__(self):
        return '%s - %s' % (self.name, self.sub_type)

class PersonManager(models.Manager):
    ''' Manager for Person Class '''

    @property
    def finders(self):
        return self.filter(
            person_type=self.model.FINDER)

    @property
    def receivers(self):
        return self.filter(
            person_type=self.model.RECEIVER)

class Person(BaseModel):
    ''' Person that dropped off, or received animal '''

    RECEIVER = 'receiver'
    FINDER = 'finder'

    PERSON_TYPES = (
        (RECEIVER, 'Receiver'),
        (FINDER, 'Finder')
    )

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    address_two = models.CharField(
        max_length=256, null=True, blank=True)
    county = models.CharField(max_length=128)
    state = USStateField()
    telephone = PhoneNumberField()
    zipcode = models.CharField(max_length=10)
    email = models.EmailField(null=True)
    person_type = models.CharField(
        max_length=16, choices=PERSON_TYPES)

    objects = PersonManager()

    def __unicode__(self):
        return u'%s %s - %s' % (self.first_name, self.last_name, self.zipcode)

class Admission(BaseModel):
    ''' Gathers all the information for an admission '''

    DIED = 'died'
    TRANSFERRED = 'transferred'
    EUTHANIZED = 'euthanized'
    RELEASED = 'released'
    CAPTIVITY = 'captivity'

    DISPOSITION_CHOICES = (
        (DIED, 'Died'),
        (TRANSFERRED, 'Transferred'),
        (EUTHANIZED, 'Euthanized'),
        (RELEASED, 'Released'),
        (CAPTIVITY, 'Still in Captivity')
    )

    RELEASED_STATES = (
        TRANSFERRED,
        RELEASED
    )

    NEONATE = 'neonate'
    JUVENILE = 'juvenile'
    ADULT = 'adult'

    ANIMAL_AGE_CHOICES = (
        (NEONATE, 'Neonate'),
        (JUVENILE, 'Juvenile'),
        (ADULT, 'Adult')
    )

    date_of_admission = models.DateField()
    received_from = models.ForeignKey('Person',
        related_name='received_person',
        null=True,
        blank=True,
    )
    released_to = models.ForeignKey('Person', null=True, blank=True)
    animal = models.ForeignKey('Animal')
    animal_age = models.CharField(max_length=64, choices=ANIMAL_AGE_CHOICES)
    disposition = models.CharField(max_length=64,
        choices=DISPOSITION_CHOICES)
    disposition_date = models.DateField()
    follow_up = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u'%s - %s' % (
            self.animal,
            self.date_of_admission.strftime('%y-%m-%d')
        )
