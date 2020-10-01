from django.db import migrations
from django.contrib.auth.hashers import make_password

data = [
    {
        'username': 'haradrimmanrope',
        'password': make_password('haradrimmanrope'),
        'about': '',
    },
    {
        'username': 'meriadocprobable',
        'password': make_password('meriadocprobable'),
        'about': '',
    },
    {
        'username': 'midgewaterprevent',
        'password': make_password('midgewaterprevent'),
        'about': '',
    },
    {
        'username': 'oliphauntettenmoors',
        'password': make_password('oliphauntettenmoors'),
        'about': '',
    },
    {
        'username': 'hassanyesterday',
        'password': make_password('hassanyesterday'),
        'about': '',
    },
    {
        'username': 'berserkdiamonds',
        'password': make_password('berserkdiamonds'),
        'about': '',
    },
    {
        'username': 'collectedvein',
        'password': make_password('collectedvein'),
        'about': '',
    },
    {
        'username': 'mithrandirperegrine',
        'password': make_password('mithrandirperegrine'),
        'about': '',
    },
    {
        'username': 'denyspeedy',
        'password': make_password('denyspeedy'),
        'about': '',
    },
    {
        'username': 'drivepickleball',
        'password': make_password('drivepickleball'),
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
