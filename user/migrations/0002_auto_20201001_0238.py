from django.db import migrations
from django.contrib.auth.hashers import make_password

data = [
    {
        'username': 'doctor',
        'password': make_password('doctor'),
        'about': '',
    },
    {
        'username': 'engineer',
        'password': make_password('engineer'),
        'about': '',
    },
    {
        'username': 'researcher',
        'password': make_password('researcher'),
        'about': '',
    },
    {
        'username': 'professor',
        'password': make_password('professor'),
        'about': '',
    },
    {
        'username': 'lawyer',
        'password': make_password('lawyer'),
        'about': '',
    },
    {
        'username': 'pilot',
        'password': make_password('pilot'),
        'about': '',
    },
    {
        'username': 'student',
        'password': make_password('student'),
        'about': '',
    },
    {
        'username': 'architect',
        'password': make_password('architect'),
        'about': '',
    },
    {
        'username': 'nurse',
        'password': make_password('nurse'),
        'about': '',
    },
    {
        'username': 'diplomat',
        'password': make_password('diplomat'),
        'about': '',
    },
]


def create_records(apps, schema_editor):
    model = apps.get_model('user', 'User')
    for record in data:
        model(**record).save()


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_records),
    ]
