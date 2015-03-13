# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Content'
        db.create_table(u'content_content', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'content', ['Content'])

        # Adding M2M table for field contributors on 'Content'
        m2m_table_name = db.shorten_name(u'content_content_contributors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('content', models.ForeignKey(orm[u'content.content'], null=False)),
            ('contributor', models.ForeignKey(orm[u'content.contributor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['content_id', 'contributor_id'])

        # Adding model 'Article'
        db.create_table(u'content_article', (
            (u'content_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['content.Content'], unique=True, primary_key=True)),
            ('text', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal(u'content', ['Article'])

        # Adding model 'Image'
        db.create_table(u'content_image', (
            (u'content_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['content.Content'], unique=True, primary_key=True)),
            ('path', self.gf('django.db.models.fields.FilePathField')(path='/home/Dropbox/CrimsonComp/Assignments/3', max_length=100)),
        ))
        db.send_create_signal(u'content', ['Image'])

        # Adding model 'Contributor'
        db.create_table(u'content_contributor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'content', ['Contributor'])


    def backwards(self, orm):
        # Deleting model 'Content'
        db.delete_table(u'content_content')

        # Removing M2M table for field contributors on 'Content'
        db.delete_table(db.shorten_name(u'content_content_contributors'))

        # Deleting model 'Article'
        db.delete_table(u'content_article')

        # Deleting model 'Image'
        db.delete_table(u'content_image')

        # Deleting model 'Contributor'
        db.delete_table(u'content_contributor')


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