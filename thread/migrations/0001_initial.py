# Generated by Django 3.1.1 on 2020-10-01 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('text', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-datetime'],
            },
        ),
    ]
