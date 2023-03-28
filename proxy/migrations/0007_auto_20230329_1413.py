# Generated by Django 3.2.18 on 2023-03-29 14:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('proxy', '0006_auto_20230326_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='inbound',
            name='expires_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inbound',
            name='last_reset',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inbound',
            name='reset_period',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='expires_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_reset',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='reset_period',
            field=models.DurationField(blank=True, null=True),
        ),
    ]