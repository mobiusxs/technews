from django.db import migrations

data = [
    {
        'value': 1,
        'comment_id': 1,
        'user_id': 1
    },
    {
        'value': 1,
        'comment_id': 2,
        'user_id': 1
    },
    {
        'value': 1,
        'comment_id': 3,
        'user_id': 1
    },
    {
        'value': 1,
        'comment_id': 4,
        'user_id': 1
    },
    {
        'value': 1,
        'comment_id': 5,
        'user_id': 1
    },
    {
        'value': 1,
        'comment_id': 6,
        'user_id': 1
    },
    {
        'value': 1,
        'comment_id': 1,
        'user_id': 2
    },
    {
        'value': 1,
        'comment_id': 2,
        'user_id': 3
    },
    {
        'value': 1,
        'comment_id': 3,
        'user_id': 4
    },
    {
        'value': 1,
        'comment_id': 4,
        'user_id': 5
    },
    {
        'value': 1,
        'comment_id': 5,
        'user_id': 6
    },
    {
        'value': 1,
        'comment_id': 6,
        'user_id': 7
    },
    {
        'value': 1,
        'comment_id': 1,
        'user_id': 3
    },
    {
        'value': 1,
        'comment_id': 2,
        'user_id': 4
    },
    {
        'value': 1,
        'comment_id': 1,
        'user_id': 4
    },
    {
        'value': 1,
        'comment_id': 2,
        'user_id': 5
    },
    {
        'value': 1,
        'comment_id': 1,
        'user_id': 6
    },
    {
        'value': 1,
        'comment_id': 2,
        'user_id': 7
    },
    {
        'value': 1,
        'comment_id': 1,
        'user_id': 8
    },
    {
        'value': 1,
        'comment_id': 2,
        'user_id': 9
    },
]


def create_records(apps, schema_editor):
    model = apps.get_model('vote', 'CommentVote')
    for record in data:
        model(**record).save()


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_auto_20201001_0239'),
        ('comment', '0003_comment_user'),
        ('user', '0002_auto_20201001_0238'),
        ('thread', '0003_auto_20201001_0238'),
    ]

    operations = [
        migrations.RunPython(create_records),
    ]
