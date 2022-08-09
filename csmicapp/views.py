from django.shortcuts import render,redirect,get_object_or_404
from userapp.models import *
from csmicapp.models import *
from adminapp.models import *
from cloudserviceproviderapp.models import *
from mcdmproject.settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives

# Create your views here.
def csmic_dashboard(request):
    data=Provider_add_services.objects.filter(cloud_upload_status='Pending')
    data1=Provider_add_services.objects.all().count()
    data2=Provider_add_services.objects.filter(cloud_upload_status='Accepted').count()
    data3=Provider_add_services.objects.filter(cloud_upload_status='Pending').count()
    data4=Provider_add_services.objects.filter(cloud_upload_status='Rejected').count()
    return render(request,'csmic/csmic-dashboard.html',{'data':data,'totalcsmic':data1,'accepted':data2,'pending':data3,'rejected':data4})

def csmic_request(request):
    data=user_registration.objects.filter(user_service_request_status='Pending')\
        |user_registration.objects.filter(user_service_request_status='Accepted')\
            |user_registration.objects.filter(user_service_request_status='Rejected')
    return render(request,'csmic/csmic-request.html',{'data':data})

def csmic_service_provider_requset(request):
    data=Provider_add_services.objects.all()
    return render(request,'csmic/csmic-service-provider-request.html',{'data':data})

def csmic_view_accepted(request,id):
    data=Provider_add_services.objects.filter(cloud_id=id)
    return render(request,'csmic/csmic-view-accepted.html',{'data':data})

def service_provider_csmic_accept(request,id):
    
    data = get_object_or_404(Provider_add_services,cloud_id=id)
     #file encryption start
   
  
    data.cloud_upload_status = 'Accepted'
    data.save(update_fields=['cloud_upload_status'])
    data.save()
    print("this is accept")
   
    a=data.service_provider_details.provider_email
    print(a)
    
     #email message
    html_content =  "<br/> <p>   Your Application has been Accepted .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [a]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("MCDM Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    try:
        if msg.send():
            print(msg)
            return redirect('csmic_service_provider_requset')
    except:
        pass
            
    
   
    return redirect('csmic_service_provider_requset')

def service_provider_csmic_reject(request,id):
    
    data = get_object_or_404(Provider_add_services,cloud_id=id)
     #file encryption start
   
  
    data.cloud_upload_status = 'Rejected'
    data.save(update_fields=['cloud_upload_status'])
    data.save()
    
    a=data.service_provider_details.provider_email
    print(a)
    print("this is accept")
    
     #email message
    html_content =  "<br/> <p>   Your Application has been Rejected.Please Reapply it .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [a]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("MCDM Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    try:
        if msg.send():
            print(msg)
            return redirect('csmic_service_provider_requset')
    except:
        pass
            
    
   
    return redirect('csmic_service_provider_requset')


def user_plan_request_accept(request,id):
    
    data = get_object_or_404(user_registration,user_id=id)
     #file encryption start
   
  
    data.user_service_request_status = 'Accepted'
    data.save(update_fields=['user_service_request_status'])
    data.save()
    print("this is accept")
    
     #email message
    html_content =  "<br/> <p>   Your Application has been Accepted .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.user_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("MCDM Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    try:
        if msg.send():
            print(msg)
            return redirect('csmic_request')
    except:
        pass
            
    
   
    return redirect('csmic_request')

def user_plan_request_reject(request,id):
    
    data = get_object_or_404(user_registration,user_id=id)
     #file encryption start
   
  
    data.user_service_request_status = 'Rejected'
    data.save(update_fields=['user_service_request_status'])
    data.save()
    print("this is accept")
    
     #email message
    html_content =  "<br/> <p>   Your Application has been Rejected.Please Reapply it .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.user_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("MCDM Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    try:
        if msg.send():
            print(msg)
            return redirect('csmic_request')
    except:
        pass
            
    
   
    return redirect('csmic_request')

def logoutcsmic(request):
    
    
         
    return redirect('home')

# def (request):
#     return render(request,'csmic/')
# def (request):
#     return render(request,'csmic/')

# def (request):
#     return render(request,'csmic/')

# def (request):
#     return render(request,'csmic/')

# def (request):
#     return render(request,'csmic/')

# def (request):
#     return render(request,'csmic/')