# Generated by Django 3.2.18 on 2023-04-01 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxy', '0013_auto_20230401_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(through='proxy.Membership', to='proxy.User'),
        ),
    ]
