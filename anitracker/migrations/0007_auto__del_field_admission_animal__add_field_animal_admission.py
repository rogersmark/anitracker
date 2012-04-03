# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Admission.animal'
        db.delete_column('anitracker_admission', 'animal_id')

        # Adding field 'Animal.admission'
        db.add_column('anitracker_animal', 'admission', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['anitracker.Admission']), keep_default=False)


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Admission.animal'
        raise RuntimeError("Cannot reverse this migration. 'Admission.animal' and its values cannot be restored.")

        # Deleting field 'Animal.admission'
        db.delete_column('anitracker_animal', 'admission_id')


    models = {
        'anitracker.admission': {
            'Meta': {'object_name': 'Admission'},
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
        'anitracker.animal': {
            'Meta': {'object_name': 'Animal'},
            'admission': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anitracker.Admission']"}),
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
