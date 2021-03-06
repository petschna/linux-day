# Generated by Django 2.2.9 on 2020-06-03 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('registration', '0001_initial'),
        ('home', '0001_initial'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
            ],
            options={
                'ordering': ('date_joined',),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('user.user',),
        ),
        migrations.AddField(
            model_name='registrationformsubmission',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Page'),
        ),
        migrations.AddField(
            model_name='registrationformsubmission',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='registrationformpage',
            name='registration_button',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.Button'),
        ),
        migrations.AddField(
            model_name='formfield',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='registration.RegistrationFormPage'),
        ),
    ]
