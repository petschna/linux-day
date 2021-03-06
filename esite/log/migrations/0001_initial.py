# Generated by Django 2.2.9 on 2020-06-03 09:45

import django.core.validators
from django.db import migrations, models
import esite.user.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workpackage',
            fields=[
                ('name', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(choices=[('new', 'Workpackage has not been started'), ('ongoing', 'Workpackage is in progress'), ('waiting', 'Workpackage cannot be continued due to dependencies'), ('review', 'Workpackage is under review'), ('fin', 'Workpackage is complted and reviewed')], default='new', max_length=32)),
                ('durration', models.DurationField(null=True)),
                ('realtime', models.DurationField(default='00:00:00', null=True)),
                ('starttime', models.DateTimeField(blank=True, null=True)),
                ('sid', models.CharField(default='000', max_length=3, unique=True, validators=[django.core.validators.RegexValidator(message='ID doesnt comply', regex='^\\d{3}$')])),
                ('did', models.CharField(default='000-000', max_length=7, validators=[django.core.validators.RegexValidator(message='ID doesnt comply', regex='^\\d{3}\\-\\d{3}$')])),
                ('pid', models.CharField(default='000-000-000', max_length=11, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='ID doesnt comply', regex='^\\d{3}\\-\\d{3}-\\d{3}$')])),
                ('start', models.TimeField(null=True)),
                ('end', models.TimeField(null=True)),
                ('assoc_user_list', wagtail.core.fields.StreamField([('userchooser', esite.user.blocks.UserChooserBlock(help_text='A user associated with the workpackage'))], blank=True, null=True)),
            ],
        ),
    ]
