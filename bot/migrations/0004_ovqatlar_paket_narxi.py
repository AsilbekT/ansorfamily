# Generated by Django 4.0.6 on 2022-08-27 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_remove_ovqatlar_paket_narxi'),
    ]

    operations = [
        migrations.AddField(
            model_name='ovqatlar',
            name='paket_narxi',
            field=models.IntegerField(default=0),
        ),
    ]