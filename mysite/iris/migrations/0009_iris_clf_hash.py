# Generated by Django 2.0.5 on 2018-05-28 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iris', '0008_remove_iris_clf_hash'),
    ]

    operations = [
        migrations.AddField(
            model_name='iris',
            name='clf_hash',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]