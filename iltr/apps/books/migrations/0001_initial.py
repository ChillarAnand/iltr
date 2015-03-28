# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(related_name='created_author_set', verbose_name='Created By', to=settings.AUTH_USER_MODEL, null=True, blank=True)),
                ('modified_by', models.ForeignKey(related_name='updated_author_set', verbose_name='Modified By', to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('name', models.CharField(max_length=255)),
                ('published_date', models.DateField()),
                ('author', models.ForeignKey(to='books.Author')),
                ('created_by', models.ForeignKey(related_name='created_book_set', verbose_name='Created By', to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(related_name='created_language_set', verbose_name='Created By', to=settings.AUTH_USER_MODEL, null=True, blank=True)),
                ('modified_by', models.ForeignKey(related_name='updated_language_set', verbose_name='Modified By', to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(to='books.Language'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='modified_by',
            field=models.ForeignKey(related_name='updated_book_set', verbose_name='Modified By', to=settings.AUTH_USER_MODEL, null=True, blank=True),
            preserve_default=True,
        ),
    ]
