# Generated by Django 4.0.6 on 2022-07-31 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider_add_services',
            fields=[
                ('cloud_id', models.AutoField(primary_key=True, serialize=False)),
                ('cloud_name', models.CharField(help_text='cloud_name', max_length=50)),
                ('cloud_service_model', models.CharField(help_text='cloud_service_model', max_length=50, null=True)),
                ('cloud_upload_status', models.CharField(default='Pending', max_length=50)),
                ('cloud_Basic_price', models.BigIntegerField(help_text='cloud_Basic_price')),
                ('cloud_Business_price', models.BigIntegerField(help_text='cloud_Business_price')),
                ('cloud_Premium_price', models.BigIntegerField(help_text='cloud_Premium_price')),
                ('cloud_Basic_monthly_usage_data', models.CharField(help_text='cloud_Basic_monthly_data', max_length=50, null=True)),
                ('cloud_Business_monthly_usage_data', models.CharField(help_text='cloud_Business_monthly_usage_data', max_length=50, null=True)),
                ('cloud_Premium_monthly_usage_data', models.CharField(help_text='cloud_Premium_monthly_usage_data', max_length=50, null=True)),
                ('cloud_service_os', models.CharField(help_text='cloud_service_os', max_length=50)),
                ('cloud_agility', models.CharField(help_text='cloud_agility', max_length=50)),
                ('cloud_performance', models.CharField(help_text='cloud_performance', max_length=50)),
                ('cloud_security_and_privacy', models.CharField(help_text='cloud_security_and_privacy', max_length=50)),
                ('cloud_upload_image', models.FileField(help_text='cloud_upload_image', max_length=50, upload_to='company_logo')),
                ('cloud_describtion', models.CharField(help_text='cloud_describtion', max_length=70, null=True)),
                ('cloud_user_status_plan', models.CharField(default='0', max_length=50)),
                ('cloud_manage_count', models.CharField(default='0', max_length=50)),
                ('user_reviews', models.CharField(help_text='user_reviews', max_length=70, null=True)),
                ('user_review_counts', models.CharField(default='0', max_length=70, null=True)),
                ('user_purchase_counts', models.CharField(default='0', max_length=70, null=True)),
                ('submitted_date', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'service_provider_add_cloud_details',
            },
        ),
        migrations.CreateModel(
            name='Provider_registration',
            fields=[
                ('provider_id', models.AutoField(primary_key=True, serialize=False)),
                ('Provider_name', models.CharField(help_text='provider_name', max_length=50)),
                ('provider_email', models.EmailField(help_text='email', max_length=50)),
                ('provider_mobile', models.BigIntegerField(help_text='mobile_no')),
                ('provider_date_of_birth', models.CharField(help_text='provider_birth', max_length=50)),
                ('provider_password', models.CharField(help_text='provider_password', max_length=50)),
                ('provider_profile', models.FileField(help_text='provider_profile', max_length=50, upload_to='csp_profile')),
                ('provider_status', models.CharField(default='Pending', max_length=50)),
            ],
            options={
                'db_table': 'service_provider_registraion_details',
            },
        ),
        migrations.CreateModel(
            name='UserUploadFile',
            fields=[
                ('file_id', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(help_text='upload_post_name', max_length=200, null=True)),
                ('file_post_name', models.CharField(help_text='upload_post_name', max_length=200, null=True)),
                ('file_describition', models.TextField(help_text='upload describtion', max_length=500)),
                ('file_type', models.CharField(help_text='upload_type', max_length=200, null=True)),
                ('file_size', models.CharField(help_text='upload_file', max_length=200, null=True)),
                ('view_rank', models.CharField(default=0, help_text='view_rank', max_length=200)),
                ('search_rank', models.CharField(default=0, help_text='view_rank', max_length=200)),
                ('update_rank', models.CharField(default=0, help_text='view_rank', max_length=200)),
                ('download_rank', models.CharField(default=0, help_text='view_rank', max_length=200)),
                ('user_upload_id', models.CharField(default=0, help_text='view_rank', max_length=200)),
                ('upload_file', models.FileField(help_text='user_upload_image ', max_length=50, null=True, upload_to='')),
                ('user_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloudserviceproviderapp.provider_add_services')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.user_registration')),
            ],
            options={
                'db_table': 'user_upload_files_details',
            },
        ),
        migrations.CreateModel(
            name='User_reviews_feedbacks',
            fields=[
                ('userfeedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('feedback_performance', models.CharField(help_text='feedback_performance', max_length=50)),
                ('feedback_usability', models.CharField(help_text='feedback_usability', max_length=50)),
                ('feedback_agility', models.CharField(help_text='feedback_agility', max_length=50)),
                ('feedback_security_privacy', models.CharField(help_text='feedback_security_privacy', max_length=50)),
                ('feedback_describtion', models.CharField(help_text='feedback_describtion', max_length=500)),
                ('user_review', models.CharField(help_text='user_reviews', max_length=70, null=True)),
                ('feedback_Assurance', models.CharField(help_text='feedback_performance', max_length=50, null=True)),
                ('feeback_financial', models.CharField(help_text='feedback_performance', max_length=50, null=True)),
                ('feedback_accountability', models.CharField(help_text='feedback_performance', max_length=50, null=True)),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cloudserviceproviderapp.provider_add_services')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.user_registration')),
            ],
            options={
                'db_table': 'user_reviews_details',
            },
        ),
        migrations.AddField(
            model_name='provider_add_services',
            name='service_provider_details',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cloudserviceproviderapp.provider_registration'),
        ),
    ]
