# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-23 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chatSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Session title', max_length=128)),
                ('profile_name', models.CharField(help_text="The person's name", max_length=128)),
                ('profile_url', models.URLField(help_text="The Url of the person's website")),
                ('description', models.TextField(help_text='Session details', max_length=512)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('register_url', models.URLField(help_text='URL for the event registration')),
            ],
        ),
    ]
