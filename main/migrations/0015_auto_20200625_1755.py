# Generated by Django 3.0.6 on 2020-06-25 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20200625_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='profile_pics'),
        ),
    ]
