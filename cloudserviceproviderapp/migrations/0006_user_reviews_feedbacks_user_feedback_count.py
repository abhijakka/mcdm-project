# Generated by Django 4.0.6 on 2022-08-01 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloudserviceproviderapp', '0005_remove_useruploadfile_download_rank_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_reviews_feedbacks',
            name='user_feedback_count',
            field=models.CharField(default='0', max_length=70, null=True),
        ),
    ]
