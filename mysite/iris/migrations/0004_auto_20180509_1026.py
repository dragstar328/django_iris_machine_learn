# Generated by Django 2.0.2 on 2018-05-09 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iris', '0003_iris_classified_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iris',
            name='classified',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
