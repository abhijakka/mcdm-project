from django.db import models
from userapp.models import *
from cloudserviceproviderapp.models import *

# Create your models here.
class Provider_registration(models.Model):
    provider_id=models.AutoField(primary_key=True)
    Provider_name=models.CharField(help_text='provider_name',max_length=50)
    provider_email=models.EmailField(help_text='email',max_length=50)
    provider_mobile=models.BigIntegerField(help_text='mobile_no',)
    provider_date_of_birth=models.CharField(help_text='provider_birth',max_length=50)
    provider_password=models.CharField(help_text='provider_password',max_length=50)
    provider_profile=models.FileField(help_text='provider_profile',max_length=50,upload_to='csp_profile')
    provider_status=models.CharField(default='Pending',max_length=50)

    class Meta:
        db_table='service_provider_registraion_details' 

class Provider_add_services(models.Model): 
        cloud_id=models.AutoField(primary_key=True)
        cloud_name=models.CharField(help_text='cloud_name',max_length=50)
        cloud_service_model=models.CharField(help_text='cloud_service_model',max_length=50,null=True)
        cloud_upload_status=models.CharField(default='Pending',max_length=50)
        service_provider_details=models.ForeignKey(Provider_registration,models.CASCADE,null=True)
        cloud_Basic_price=models.BigIntegerField(help_text='cloud_Basic_price')
        cloud_Business_price=models.BigIntegerField(help_text='cloud_Business_price')
        cloud_Premium_price=models.BigIntegerField(help_text='cloud_Premium_price')
        cloud_Basic_monthly_usage_data=models.CharField(help_text='cloud_Basic_monthly_data',max_length=50,null=True)
        cloud_Business_monthly_usage_data=models.CharField(help_text='cloud_Business_monthly_usage_data',max_length=50,null=True)
        cloud_Premium_monthly_usage_data=models.CharField(help_text='cloud_Premium_monthly_usage_data',max_length=50,null=True)
        cloud_service_os=models.CharField(help_text='cloud_service_os',max_length=50)
        cloud_agility=models.CharField(help_text='cloud_agility',max_length=50)
        cloud_performance=models.CharField(help_text='cloud_performance',max_length=50)
        cloud_security_and_privacy=models.CharField(help_text='cloud_security_and_privacy',max_length=50)
        cloud_upload_image=models.FileField(help_text='cloud_upload_image',max_length=50,upload_to='company_logo')
        cloud_describtion=models.CharField(help_text='cloud_describtion',max_length=70,null=True)
        cloud_user_status_plan=models.CharField(default='0',max_length=50)
        cloud_manage_count=models.CharField(default='0',max_length=50)
        user_reviews=models.CharField(help_text='user_reviews',max_length=70,default='0')
        user_review_counts=models.CharField(default='0',max_length=70,null=True)
        user_purchase_counts=models.CharField(default='0',max_length=70,null=True)
        submitted_date=models.DateField(auto_now_add=True,null=True)
        
        class Meta:
            db_table='service_provider_add_cloud_details' 
            
class User_reviews_feedbacks(models.Model):
    
    userfeedback_id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Provider_add_services,models.CASCADE,null=True)
    feedback_performance=models.CharField(help_text='feedback_performance',max_length=50)
    feedback_usability=models.CharField(help_text='feedback_usability',max_length=50)
    feedback_agility=models.CharField(help_text='feedback_agility',max_length=50)
    feedback_security_privacy=models.CharField(help_text='feedback_security_privacy',max_length=50)
    feedback_describtion=models.CharField(help_text='feedback_describtion',max_length=500)
    user_review=models.CharField(help_text='user_reviews',max_length=70,default='0')
    user_id=models.ForeignKey(user_registration,models.CASCADE,null=True)
    feedback_Assurance=models.CharField(help_text='feedback_performance',max_length=50,null=True)
    user_feedback_count=models.CharField(default='0',max_length=70,null=True)
    feeback_financial=models.CharField(help_text='feedback_performance',max_length=50,null=True)
    feedback_accountability=models.CharField(help_text='feedback_performance',max_length=50,null=True)


    class Meta:
            db_table='user_reviews_details'   
            
class UserUploadFile(models.Model):
       
    file_id=models.AutoField(primary_key=True) 
    user_creator=models.ForeignKey(Provider_add_services,models.CASCADE)
    user_id=models.ForeignKey(user_registration,models.CASCADE,null=True)
    file_name=models.CharField(help_text='upload_post_name',max_length=200,null=True)
    file_post_name=models.CharField(help_text='upload_post_name',max_length=200,null=True)  
    file_describition=models.TextField(help_text='upload describtion' , max_length=500)
    file_type=models.CharField(help_text='upload_type',max_length=200,null=True)
    file_size=models.CharField(help_text='upload_file',max_length=200,null=True)
    upload_file=models.FileField(help_text='user_upload_image ' , max_length=5000,upload_to='user_files',null=True)


    class Meta:
        db_table='user_upload_files_details'                       
      