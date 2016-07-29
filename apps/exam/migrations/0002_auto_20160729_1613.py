# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 16:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasks', models.TextField(max_length=255)),
                ('status', models.TextField(max_length=250)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
            ],
            managers=[
                ('appointmanager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='trip',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='travellers',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='email',
        ),
        migrations.DeleteModel(
            name='Trip',
        ),
        migrations.AddField(
            model_name='appoint',
            name='appointment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to='exam.User'),
        ),
    ]