# Generated by Django 2.0.8 on 2019-03-19 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_django', '0008_partial_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersocialauth',
            name='unionid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
