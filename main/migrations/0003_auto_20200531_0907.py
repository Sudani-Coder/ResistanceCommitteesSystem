# Generated by Django 3.0.6 on 2020-05-31 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200531_0900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='Family',
        ),
        migrations.AddField(
            model_name='family',
            name='Area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Area'),
        ),
    ]
