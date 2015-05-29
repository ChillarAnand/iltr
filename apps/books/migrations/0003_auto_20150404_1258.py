# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_translated_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='full_name',
            field=models.CharField(blank=True, max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(blank=True, max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(blank=True, max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='author',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='translated_name',
            field=models.CharField(blank=True, max_length=255),
            preserve_default=True,
        ),
    ]
