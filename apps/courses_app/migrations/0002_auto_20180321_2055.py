# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-21 20:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewCourse',
            new_name='Course',
        ),
    ]