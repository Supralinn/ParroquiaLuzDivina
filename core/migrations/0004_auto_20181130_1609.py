# Generated by Django 2.1.3 on 2018-11-30 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20181130_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='comunidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Comunidad'),
        ),
    ]