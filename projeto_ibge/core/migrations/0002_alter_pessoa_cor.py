# Generated by Django 4.2.2 on 2023-06-29 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='cor',
            field=models.CharField(max_length=2),
        ),
    ]
