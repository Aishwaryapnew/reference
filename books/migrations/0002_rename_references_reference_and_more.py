# Generated by Django 5.1.4 on 2024-12-17 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='references',
            new_name='reference',
        ),
        migrations.RenameField(
            model_name='reference',
            old_name='references',
            new_name='referencesis',
        ),
        migrations.AlterModelTable(
            name='reference',
            table='reference',
        ),
    ]
