from django.shortcuts import render,redirect,get_object_or_404
from userapp.models import *
from csmicapp.models import *
from adminapp.models import *
from cloudserviceproviderapp.models import *
from django.contrib import messages
from django.db.models import Avg,Sum,Count,F
# Create your views here.
def service_provider_dashboard(request):
    id=request.session['provider_id']
    data=Provider_add_services.objects.filter(service_provider_details=id)
    print(data)
    data2=Provider_add_services.objects.filter(service_provider_details=id).values('user_purchase_counts')
    print(data2)
    # for i in data:
    #     a=i.cloud_id
    #     print(a)
    # data2=User_Plan_Request.objects.filter(cloud_id=a).values('cloud_id').count()
    # print(data2)
    data3=Provider_add_services.objects.filter(service_provider_details=id).values('cloud_manage_count').count()
    data4=Provider_add_services.objects.filter(service_provider_details=id).values('cloud_id').count()
    data5=Provider_add_services.objects.filter(service_provider_details=id).filter(cloud_upload_status = 'Pending') or Provider_add_services.objects.filter(service_provider_details=id).filter(cloud_upload_status = 'Accepted')
    print(data5)
    
    
    return render(request,'cloudserviceprovider/serviceprovidersdashboard.html',{'data':data,'manage':data3,'total':data4,'status':data5,'data2':data2})

def service_provider_profile(request):
    id=request.session['provider_id']
    user=get_object_or_404(Provider_registration,provider_id=id)
    data=Provider_registration.objects.filter(provider_id=id)
    if request.method =='POST' :
          
        Provider_name=request.POST.get('user_name')
        provider_password=request.POST.get('user_location')

       
       
        if not request.FILES.get('profile',False):
            # provider_profile=request.FILES['profile']
            user.Provider_name=Provider_name
            user.provider_password=provider_password
            # user.provider_profile=provider_profile
            user.save(update_fields=['Provider_name','provider_password'])
            user.save()
            if user:
                        messages.success(request,"Your Profile is Updated")       
            else:
                    pass
        if  request.FILES.get('profile',False):
              provider_profile=request.FILES['profile']
              user.provider_profile=provider_profile
              user.Provider_name=Provider_name
              user.provider_password=provider_password   
        
              user.save(update_fields=['Provider_name','provider_password','provider_profile'])
              user.save()
              if user:
                        messages.success(request,"Your Profile is Updated")       
              else:
                    pass
    return render(request,'cloudserviceprovider/service-provider-profile.html',{'data':data})

def service_provider_add_services(request):
    id=request.session['provider_id']
    data=Provider_registration.objects.get(provider_id=id)
    if request.method=='POST' and request.FILES['cloud_upload_image']:
        cloud_name=request.POST.get('cloud_name')
        cloud_Basic_price=request.POST.get('cloud_Basic_price')
        cloud_Business_price=request.POST.get('cloud_Business_price')
        cloud_Premium_price=request.POST.get('cloud_Premium_price')
        cloud_Basic_monthly_usage_data=request.POST.get('cloud_Basic_monthly_usage_data')
        cloud_Business_monthly_usage_data=request.POST.get('cloud_Business_monthly_usage_data')
        cloud_Premium_monthly_usage_data=request.POST.get('cloud_Premium_monthly_usage_data')
        cloud_service_model=request.POST.get('cloud_service_model')
        cloud_service_os=request.POST.get('cloud_service_os')
        cloud_agility=request.POST.get('cloud_agility')
        cloud_performance=request.POST.get('cloud_performance')
        cloud_security_and_privacy=request.POST.get('cloud_security_and_privacy')
        cloud_upload_image=request.FILES['cloud_upload_image']
        cloud_describtion=request.POST.get('describtion')
        cloud = Provider_add_services.objects.create(cloud_Premium_monthly_usage_data=cloud_Premium_monthly_usage_data,
                                             cloud_Business_monthly_usage_data=cloud_Business_monthly_usage_data,
                                             cloud_Basic_monthly_usage_data=cloud_Basic_monthly_usage_data,
                                             cloud_describtion=cloud_describtion,service_provider_details=data,
                                             cloud_service_model=cloud_service_model,cloud_name=cloud_name,
                                             cloud_Basic_price=cloud_Basic_price,cloud_Business_price=cloud_Business_price,
                                             cloud_Premium_price=cloud_Premium_price,cloud_service_os=cloud_service_os,
                                             cloud_agility=cloud_agility,cloud_performance=cloud_performance,
                                             cloud_security_and_privacy=cloud_security_and_privacy,
                                             cloud_upload_image=cloud_upload_image)
        if cloud:
            messages.success(request,"Your Service is Uploaded") 
        else:
            pass  
    return render(request,'cloudserviceprovider/serviceprovider-add-services.html')

def service_provider_manage(request,id):
    data=Provider_add_services.objects.filter(cloud_id=id)
    obj=get_object_or_404(Provider_add_services,cloud_id=id)
    if request.method=='POST':
        cloud_Basic_price=request.POST.get('cloud_Basic_price')
        cloud_Business_price=request.POST.get('cloud_Business_price')
        cloud_agility=request.POST.get('cloud_agility')
        cloud_performance=request.POST.get('cloud_performance')
        cloud_security_and_privacy=request.POST.get('cloud_security_and_privacy')
        cloud_Premium_price=request.POST.get('cloud_Premium_price')
        cloud_describtion=request.POST.get('describtion')

        obj.cloud_Basic_price=cloud_Basic_price
        obj.cloud_Business_price=cloud_Business_price
        obj.cloud_agility=cloud_agility
        obj.cloud_performance=cloud_performance
        obj.cloud_security_and_privacy=cloud_security_and_privacy
        obj.cloud_Premium_price=cloud_Premium_price
        obj.cloud_describtion=cloud_describtion
        obj.save(update_fields=['cloud_Basic_price','cloud_Business_price','cloud_agility','cloud_performance','cloud_security_and_privacy','cloud_Premium_price','cloud_describtion'])
       
        if obj:
                messages.success(request,"Your Services is Updated") 
                data2=Provider_add_services.objects.filter(cloud_id=id).update(cloud_manage_count=F('cloud_manage_count')+1)
                print(data2)
      
        else:
            pass
    return render(request,'cloudserviceprovider/serviceproviders-manage.html',{'data':data})

def service_provider_view_added_services(request):
    id=request.session['provider_id']
    data=Provider_add_services.objects.filter(service_provider_details=id)
    return render(request,'cloudserviceprovider/service-providers-view-added-services.html',{'data':data})

def logoutcsr(request):
    
    request.session['provider_id'] == None
         
    return redirect('home')
    