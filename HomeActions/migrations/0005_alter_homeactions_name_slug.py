# Generated by Django 3.2.7 on 2021-09-25 06:06

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HomeActions', '0004_homeactions_name_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeactions',
            name='name_slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name'),
        ),
    ]
