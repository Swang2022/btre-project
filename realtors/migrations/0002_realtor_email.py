# Generated by Django 4.0.3 on 2022-05-04 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='email',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
