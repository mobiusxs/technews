# Generated by Django 3.1.1 on 2020-10-01 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('thread', '0001_initial'),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thread.thread'),
        ),
    ]
