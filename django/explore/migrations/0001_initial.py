# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieObj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('titleWords', models.CharField(max_length=500, null=True)),
                ('year', models.IntegerField(null=True)),
                ('actor1', models.CharField(max_length=50, null=True)),
                ('actor2', models.CharField(max_length=50, null=True)),
                ('actor3', models.CharField(max_length=50, null=True)),
                ('director', models.CharField(max_length=50, null=True)),
                ('keywords', models.CharField(max_length=500, null=True)),
                ('genres', models.CharField(max_length=500, null=True)),
                ('relevance', models.IntegerField(null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('language', models.CharField(max_length=50, null=True)),
                ('criteria', models.CharField(max_length=1000, null=True)),
                ('rating', models.IntegerField(null=True)),
                ('score', models.IntegerField(null=True)),
                ('movieID', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]