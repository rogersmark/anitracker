# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SpecieType'
        db.create_table('anitracker_specietype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('animal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anitracker.Animal'])),
        ))
        db.send_create_signal('anitracker', ['SpecieType'])

        # Adding model 'Animal'
        db.create_table('anitracker_animal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
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
            ('address_two', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('telephone', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('anitracker', ['Person'])

        # Adding model 'Admission'
        db.create_table('anitracker_admission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_of_admission', self.gf('django.db.models.fields.DateTimeField')()),
            ('received_from', self.gf('django.db.models.fields.related.ForeignKey')(related_name='received_person', to=orm['anitracker.Person'])),
            ('released_to', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anitracker.Person'])),
            ('animal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anitracker.Animal'])),
            ('animal_subtype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anitracker.SpecieType'])),
            ('follow_up', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('anitracker', ['Admission'])


    def backwards(self, orm):
        
        # Deleting model 'SpecieType'
        db.delete_table('anitracker_specietype')

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
            'animal_subtype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anitracker.SpecieType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_admission': ('django.db.models.fields.DateTimeField', [], {}),
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
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
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
