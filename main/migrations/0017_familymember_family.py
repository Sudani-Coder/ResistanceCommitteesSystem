# Generated by Django 3.0.6 on 2020-07-01 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20200701_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='familymember',
            name='Family',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Family'),
        ),
    ]
