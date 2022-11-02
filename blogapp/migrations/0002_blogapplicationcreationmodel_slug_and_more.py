# Generated by Django 4.1.2 on 2022-11-01 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogapplicationcreationmodel',
            name='slug',
            field=models.SlugField(default=1, max_length=250, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogapplicationcreationmodel',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blogapplicationcreationmodel',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]