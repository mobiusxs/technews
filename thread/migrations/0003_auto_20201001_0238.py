from django.db import migrations

data = [
    {
        'url': 'https://www.google.com',
        'text': 'Google to close operations on Google Search as usage continues to fall.',
        'user_id': 1,
    },
    {
        'url': 'https://www.youtube.com',
        'text': 'Viral YouTube video has more views than all other YouTube videos combined, including itself.',
        'user_id': 2,
    },
    {
        'url': 'https://www.facebook.com',
        'text': 'Mark Zuckerberg out as Facebook CEO. 15-year-old savant programmer to takeover after successful hack session.',
        'user_id': 3,
    },
    {
        'url': 'https://www.amazon.com',
        'text': 'Amazon sales drop for a record 56 months in a row after CEO loses interest in platform.',
        'user_id': 4,
    },
    {
        'url': 'https://www.wikipedia.com',
        'text': 'Wikipedia rated most trustworthy site on internet.',
        'user_id': 5,
    },
    {
        'url': 'https://www.zoom.com',
        'text': 'Zoom still unsecure despite commitment to improve security.',
        'user_id': 6,
    },
    {
        'url': 'https://www.reddit.com',
        'text': 'More reposts hit the Reddit frontpage, catapulting long-time users to alternatives.',
        'user_id': 7,
    },
    {
        'url': 'https://www.live.com',
        'text': 'Gmail surpassed by Outlook in daily emails.',
        'user_id': 8,
    },
    {
        'url': 'https://www.netflix.com',
        'text': 'Actor dies on-set while filming Netflix Original about movie stars who die on movie sets.',
        'user_id': 9,
    },
    {
        'url': 'https://www.microsoft.com',
        'text': 'Microsoft lags behind competitors in cloud services.',
        'user_id': 10,
    },
    {
        'url': 'https://www.office.com',
        'text': 'Man creates worlds first general AI using Microsoft Excel.',
        'user_id': 5,
    },
    {
        'url': 'https://www.instagram.com',
        'text': 'Instagram superstar Christopher Walken describes his rise in an exclusive interview with Stephen Colbert.',
        'user_id': 4,
    },
    {
        'url': 'https://www.twitch.com',
        'text': 'E-Sports legend "buttonpusher41" signs a $2 billion streaming contract with Twitch',
        'user_id': 3,
    },
    {
        'url': 'https://www.bing.com',
        'text': 'CEO of worlds largest search engine, Bing.com, says brain implant can create direct connection to their server.',
        'user_id': 2,
    },
    {
        'url': 'https://www.ebay.com',
        'text': 'Shia LaBeouf auctions beard trimmings on eBay to raise awareness of male balding.',
        'user_id': 1,
    },
]


def create_records(apps, schema_editor):
    model = apps.get_model('thread', 'Thread')
    for record in data:
        model(**record).save()


class Migration(migrations.Migration):

    dependencies = [
        ('thread', '0002_thread_user'),
        ('user', '0002_auto_20201001_0238'),
    ]

    operations = [
        migrations.RunPython(create_records),
    ]
