# Generated by Django 3.0.3 on 2020-02-29 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200223_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='local_evento',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
