# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('summary', models.CharField(max_length=256)),
                ('patient', models.ForeignKey(to='portal.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('subject', models.CharField(max_length=50)),
                ('body', models.CharField(max_length=2048)),
                ('patient', models.ForeignKey(to='portal.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Physician',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('phystype', models.CharField(default=b'DR', max_length=2, choices=[(b'DR', b'Doctor'), (b'PA', b'Physician Assistant'), (b'NP', b'Nurse Practitioner')])),
            ],
        ),
        migrations.RemoveField(
            model_name='visit',
            name='patient',
        ),
        migrations.DeleteModel(
            name='Visit',
        ),
        migrations.AddField(
            model_name='appointment',
            name='physician',
            field=models.ForeignKey(to='portal.Physician'),
        ),
    ]
