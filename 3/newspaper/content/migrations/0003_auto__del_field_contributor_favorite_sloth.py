# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Contributor.favorite_sloth'
        db.delete_column(u'content_contributor', 'favorite_sloth')


    def backwards(self, orm):
        # Adding field 'Contributor.favorite_sloth'
        db.add_column(u'content_contributor', 'favorite_sloth',
                      self.gf('django.db.models.fields.CharField')(default='Punkin', max_length=500),
                      keep_default=False)


    models = {
        u'content.article': {
            'Meta': {'object_name': 'Article', '_ormbases': [u'content.Content']},
            u'content_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['content.Content']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('tinymce.models.HTMLField', [], {})
        },
        u'content.content': {
            'Meta': {'object_name': 'Content'},
            'contributors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'content'", 'null': 'True', 'to': u"orm['content.Contributor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'content.contributor': {
            'Meta': {'object_name': 'Contributor'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'content.image': {
            'Meta': {'object_name': 'Image', '_ormbases': [u'content.Content']},
            u'content_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['content.Content']", 'unique': 'True', 'primary_key': 'True'}),
            'path': ('django.db.models.fields.FilePathField', [], {'path': "'/home/Dropbox/CrimsonComp/Assignments/3'", 'max_length': '100'})
        }
    }

    complete_apps = ['content']