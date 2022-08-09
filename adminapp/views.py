from django.shortcuts import render,get_object_or_404,redirect
from userapp.models import *
from csmicapp.models import *
from adminapp.models import *
from cloudserviceproviderapp.models import *
from mcdmproject.settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
# Create your views here.

def admin_home(request):
    data=Provider_registration.objects.filter(provider_status='Pending')
    data1=Provider_registration.objects.all().count()
    data2=Provider_registration.objects.filter(provider_status='Accepted').count()
    data3=Provider_registration.objects.filter(provider_status='Pending').count()
    data4=Provider_registration.objects.filter(provider_status='Rejected').count()
    
    return render(request,'admin/admin-index.html',{'data':data,'serviceproviders':data1,'accepted':data2,'pending':data3,'rejected':data4})

def admin_view_service_provider(request):
    data=Provider_registration.objects.all()
    return render(request,'admin/view-serviceproviders.html',{'data':data})

def admin_user_signup_request(request):
    data=user_registration.objects.all()
    return render(request,'admin/admin-user-signup-request.html',{'data':data})

def user_registration_accept(request,id):
    
    data = get_object_or_404(user_registration,user_id=id)
     #file encryption start
   
  
    data.user_status = 'Accepted'
    data.save(update_fields=['user_status'])
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
            return redirect('admin_user_signup_request')
    except:
        pass
            
    
   
    return redirect('admin_user_signup_request')

def user_registration_reject(request,id):
    
    data = get_object_or_404(user_registration,user_id=id)
     #file encryption start
   
  
    data.user_status = 'Rejected'
    data.save(update_fields=['user_status'])
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
            return redirect('admin_user_signup_request')
    except:
        pass
            
    
   
    return redirect('admin_user_signup_request')

def Provider_registration_accept(request,id):
    
    data = get_object_or_404(Provider_registration,provider_id=id)
     #file encryption start
   
  
    data.provider_status = 'Accepted'
    data.save(update_fields=['provider_status'])
    data.save()
    print("this is accept")
    
     #email message
    html_content =  "<br/> <p>   Your Application has been Accepted .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.provider_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("MCDM Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    try:
        if msg.send():
            print(msg)
            return redirect('admin_view_service_provider')
    except:
        pass
            
    
   
    return redirect('admin_view_service_provider')

def Provider_registration_reject(request,id):
    
    data = get_object_or_404(Provider_registration,provider_id=id)
     #file encryption start
   
  
    data.provider_status = 'Rejected'
    data.save(update_fields=['provider_status'])
    data.save()
    print("this is accept")
    
     #email message
    html_content =  "<br/> <p>   Your Application has been Rejected.Please Reapply it .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.provider_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("MCDM Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    try:
        if msg.send():
            print(msg)
            return redirect('admin_view_service_provider')
    except:
        pass
            
    
   
    return redirect('admin_view_service_provider')

def logoutadmin(request):
    
  
         
    return redirect('home')

# def (request):
#     return render(request,'admin/')

# def (request):
#     return render(request,'admin/')
