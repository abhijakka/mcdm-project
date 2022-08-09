from django.db import models


# Create your models here.
class user_registration(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(help_text='user_name',max_length=50)
    user_email=models.EmailField(help_text='email',max_length=50)
    user_mobile=models.BigIntegerField(help_text='mobile_no')
    user_date_of_birth=models.CharField(help_text='user_birth',max_length=50)
    user_password=models.CharField(help_text='user_password',max_length=50)
    user_status=models.CharField(default='Pending',max_length=50)
    user_service_request_status=models.CharField(default='0',max_length=50)

    user_profile_upload=models.FileField(help_text='user_profile',max_length=50,upload_to='userprofile')
    class Meta:
            db_table='user_registraion_details' 
           
