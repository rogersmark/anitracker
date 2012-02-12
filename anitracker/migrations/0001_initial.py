# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Animal'
        db.create_table('anitracker_animal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('sub_type', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('anitracker', ['Animal'])

        # Adding model 'Person'
        db.create_table('anitracker_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('address_two', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('state', self.gf('django.contrib.localflavor.us.models.USStateField')(max_length=2)),
            ('telephone', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
            ('finder', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('receiver', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('anitracker', ['Person'])

        # Adding model 'Admission'
        db.create_table('anitracker_admission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_of_admission', self.gf('django.db.models.fields.DateField')()),
            ('received_from', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='received_person', null=True, to=orm['anitracker.Person'])),
            ('released_to', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anitracker.Person'], null=True, blank=True)),
            ('animal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anitracker.Animal'])),
            ('animal_age', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('disposition', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('disposition_date', self.gf('django.db.models.fields.DateField')()),
            ('follow_up', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('anitracker', ['Admission'])


    def backwards(self, orm):
        
        # Deleting model 'Animal'
        db.delete_table('anitracker_animal')

        # Deleting model 'Person'
        db.delete_table('anitracker_person')

        # Deleting model 'Admission'
        db.delete_table('anitracker_admission')


    models = {
        'anitracker.admission': {
            'Meta': {'object_name': 'Admission'},
            'animal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anitracker.Animal']"}),
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
            'county': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'finder': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'receiver': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'telephone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['anitracker']
