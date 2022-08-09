from django.db import models
from userapp.models import *
from csmicapp.models import *
from adminapp.models import *
from cloudserviceproviderapp.models import *
# Create your models here.
class User_Plan_Request(models.Model):
    plan_id=models.AutoField(primary_key=True)
    user_plan_id=models.ForeignKey(user_registration,models.CASCADE,null=True)
    user_purchased=models.CharField(help_text='userpurchased',null=True, max_length=50)
    cloud_id=models.ForeignKey(Provider_add_services,on_delete=models.CASCADE,null=True)
    user_upload_times=models.CharField(default=0, max_length=50)
    user_card_no=models.CharField(help_text='user_card_no',null=True, max_length=500)
    purchased_price=models.CharField(help_text='purchased_price',null=True, max_length=500)
    user_address=models.CharField(help_text='user_address',null=True, max_length=500)
    storage_purchased_converted=models.CharField(help_text='storage_purchased_converted',null=True, max_length=500)
    storage_purchased=models.CharField(help_text='storage_purchased',null=True, max_length=500)
    debited_storage=models.CharField(help_text='debited_storage',default=0,max_length=500)
    class Meta:
        
            db_table='user_request_plan_details'