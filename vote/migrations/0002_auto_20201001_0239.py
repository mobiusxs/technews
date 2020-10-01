from django.db import migrations

data = [
    {
        'value': 1,
        'thread_id': 15,
        'user_id': 10
    },

    {
        'value': 1,
        'thread_id': 15,
        'user_id': 9
    },
    {
        'value': 1,
        'thread_id': 15,
        'user_id': 8
    },
    {
        'value': 1,
        'thread_id': 15,
        'user_id': 7
    },
    {
        'value': 1,
        'thread_id': 15,
        'user_id': 6
    },
    {
        'value': 1,
        'thread_id': 15,
        'user_id': 5
    },
    {
        'value': 1,
        'thread_id': 15,
        'user_id': 4
    },
    {
        'value': 1,
        'thread_id': 15,
        'user_id': 3
    },
    {
        'value': 1,
        'thread_id': 15,
        'user_id': 2
    },
    {
        'value': 1,
        'thread_id': 15,
        'user_id': 1
    },
    {
        'value': 1,
        'thread_id': 14,
        'user_id': 1
    },
    {
        'value': 1,
        'thread_id': 13,
        'user_id': 1
    },
    {
        'value': 1,
        'thread_id': 12,
        'user_id': 1
    },
    {
        'value': 1,
        'thread_id': 12,
        'user_id': 2
    },
    {
        'value': 1,
        'thread_id': 12,
        'user_id': 3
    },
    {
        'value': 1,
        'thread_id': 10,
        'user_id': 1
    },
    {
        'value': 1,
        'thread_id': 10,
        'user_id': 2
    },
    {
        'value': 1,
        'thread_id': 9,
        'user_id': 1
    },
    {
        'value': 1,
        'thread_id': 8,
        'user_id': 3
    },
    {
        'value': 1,
        'thread_id': 8,
        'user_id': 2
    },
    {
        'value': 1,
        'thread_id': 8,
        'user_id': 1
    },
    {
        'value': 1,
        'thread_id': 7,
        'user_id': 1
    },
    {
        'value': 1,
        'thread_id': 5,
        'user_id': 1
    },
    {
        'value': 1,
        'thread_id': 4,
        'user_id': 1
    },
    {
        'value': 1,
        'thread_id': 3,
        'user_id': 2
    },
    {
        'value': 1,
        'thread_id': 3,
        'user_id': 1
    },
    {
        'value': 1,
        'thread_id': 2,
        'user_id': 1
    },
]


def create_records(apps, schema_editor):
    model = apps.get_model('vote', 'ThreadVote')
    for record in data:
        model(**record).save()


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
        ('comment', '0003_comment_user'),
        ('user', '0002_auto_20201001_0238'),
        ('thread', '0003_auto_20201001_0238'),
    ]

    operations = [
        migrations.RunPython(create_records),
    ]
