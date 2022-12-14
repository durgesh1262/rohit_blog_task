# Generated by Django 4.1.2 on 2022-11-01 13:37

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_alter_blogapplicationcreationmodel_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogapplicationcreationmodel',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True),
        ),
    ]
