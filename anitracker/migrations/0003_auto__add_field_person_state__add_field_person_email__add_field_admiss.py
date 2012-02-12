# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Person.state'
        db.add_column('anitracker_person', 'state', self.gf('django.contrib.localflavor.us.models.USStateField')(default='MO', max_length=2), keep_default=False)

        # Adding field 'Person.email'
        db.add_column('anitracker_person', 'email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True), keep_default=False)

        # Adding field 'Admission.animal_age'
        db.add_column('anitracker_admission', 'animal_age', self.gf('django.db.models.fields.CharField')(default='juvenile', max_length=64), keep_default=False)

        # Adding field 'Admission.disposition'
        db.add_column('anitracker_admission', 'disposition', self.gf('django.db.models.fields.CharField')(default='captivity', max_length=64), keep_default=False)

        # Adding field 'Admission.disposition_date'
        db.add_column('anitracker_admission', 'disposition_date', self.gf('django.db.models.fields.DateField')(default=datetime.date(2012, 2, 12)), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Person.state'
        db.delete_column('anitracker_person', 'state')

        # Deleting field 'Person.email'
        db.delete_column('anitracker_person', 'email')

        # Deleting field 'Admission.animal_age'
        db.delete_column('anitracker_admission', 'animal_age')

        # Deleting field 'Admission.disposition'
        db.delete_column('anitracker_admission', 'disposition')

        # Deleting field 'Admission.disposition_date'
        db.delete_column('anitracker_admission', 'disposition_date')


    models = {
        'anitracker.admission': {
            'Meta': {'object_name': 'Admission'},
            'animal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anitracker.Animal']"}),
            'animal_age': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'animal_subtype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anitracker.SpecieType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_admission': ('django.db.models.fields.DateField', [], {}),
            'disposition': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'disposition_date': ('django.db.models.fields.DateField', [], {}),
            'follow_up': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'received_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'received_person'", 'to': "orm['anitracker.Person']"}),
            'released_to': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anitracker.Person']"})
        },
        'anitracker.animal': {
            'Meta': {'object_name': 'Animal'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'anitracker.person': {
            'Meta': {'object_name': 'Person'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'address_two': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'telephone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'anitracker.specietype': {
            'Meta': {'object_name': 'SpecieType'},
            'animal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anitracker.Animal']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['anitracker']
