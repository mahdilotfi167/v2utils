# Generated by Django 3.2.18 on 2023-04-01 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proxy', '0011_auto_20230331_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trojan',
            fields=[
                ('inbound_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='proxy.inbound')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('proxy.inbound',),
        ),
    ]