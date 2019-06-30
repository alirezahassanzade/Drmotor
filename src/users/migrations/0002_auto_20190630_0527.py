# Generated by Django 2.2 on 2019-06-30 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.IntegerField(choices=[(10, 'Admin'), (20, 'User'), (30, 'Mechanic')], default=10, verbose_name='User Type'),
        ),
    ]