# Generated by Django 5.1.4 on 2024-12-17 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_reference_academic_yr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='academic_yr',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='reference',
            name='coursecode',
            field=models.TextField(),
        ),
    ]
