# Generated by Django 2.1.7 on 2019-08-14 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mcrh_Birth_Record', '0002_auto_20190814_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mcrh_Birth_Record.Parent'),
        ),
    ]