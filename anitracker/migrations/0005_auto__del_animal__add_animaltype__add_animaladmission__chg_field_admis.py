# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Animal'
        db.delete_table('anitracker_animal')

        # Adding model 'AnimalType'
        db.create_table('anitracker_animaltype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('sub_type', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('anitracker', ['AnimalType'])

        # Adding model 'AnimalAdmission'
        db.create_table('anitracker_animaladmission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('weight', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('animal_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anitracker.AnimalType'])),
        ))
        db.send_create_signal('anitracker', ['AnimalAdmission'])

        # Changing field 'Admission.animal'
        db.alter_column('anitracker_admission', 'animal_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anitracker.AnimalAdmission']))


    def backwards(self, orm):
        
        # Adding model 'Animal'
        db.create_table('anitracker_animal', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sub_type', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('anitracker', ['Animal'])

        # Deleting model 'AnimalType'
        db.delete_table('anitracker_animaltype')

        # Deleting model 'AnimalAdmission'
        db.delete_table('anitracker_animaladmission')

        # Changing field 'Admission.animal'
        db.alter_column('anitracker_admission', 'animal_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anitracker.Animal']))


    models = {
        'anitracker.admission': {
            'Meta': {'object_name': 'Admission'},
            'animal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anitracker.AnimalAdmission']"}),
            'animal_age': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_admission': ('django.db.models.fields.DateField', [], {}),
            'disposition': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'disposition_date': ('django.db.models.fields.DateField', [], {}),
            'follow_up': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'received_from': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'received_person'", 'null': 'True', 'to': "orm['anitracker.Person']"}),
            'released_to': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anitracker.Person']", 'null': 'True', 'blank': 'True'})
        },
        'anitracker.animaladmission': {
            'Meta': {'object_name': 'AnimalAdmission'},
            'animal_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anitracker.AnimalType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'anitracker.animaltype': {
            'Meta': {'ordering': "('name',)", 'object_name': 'AnimalType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'sub_type': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'anitracker.person': {
            'Meta': {'object_name': 'Person'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'address_two': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'person_type': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'telephone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['anitracker']
