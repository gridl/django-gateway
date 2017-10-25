# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 13:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_uri', models.CharField(max_length=200)),
                ('destination_path', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backend_identifier', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('uri', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=200)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('start_datetime', models.DateTimeField(null=True)),
                ('end_datetime', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_uri', models.CharField(max_length=200)),
                ('destination_path', models.CharField(max_length=200)),
                ('action', models.CharField(max_length=20)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scripts', to='jobs.Job')),
            ],
        ),
        migrations.AddField(
            model_name='input',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inputs', to='jobs.Job'),
        ),
    ]
