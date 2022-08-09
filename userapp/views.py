from ast import Add
from audioop import avgpp
from dataclasses import field
from itertools import count
from logging import Filter
from tkinter import N
from turtle import update
from django.shortcuts import render,redirect,get_object_or_404
from userapp.models import *
from csmicapp.models import *
from adminapp.models import *
from cloudserviceproviderapp.models import *
from django.contrib import messages
from mcdmproject.settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
from django.db.models import Avg,Sum,Count,F,Max
from django.contrib import auth 
from django.core.files.storage import FileSystemStorage
import sys
from operator import itemgetter 
from hurry.filesize import size,alternative


import statistics
# Create your views here.
def home(request):
    data=User_reviews_feedbacks.objects.all()
    return render(request,'user/index.html',{'data':data})

def publicplans(request):
    data=Provider_add_services.objects.filter(cloud_upload_status='Accepted')
    return render(request,'user/public-plans.html',{'data':data})

def contact(request):
    return render(request,'user/contact.html')

def user_login(request):
    if request.method == 'POST': 
                email = request.POST.get('user_email') 
                password = request.POST.get('user_password') 
                try: 
                     check = user_registration.objects.get(user_email=email,user_password=password)   
                     request.session['user_id']=check.user_id  
                       
                     user_status = check.user_status 
                     if user_status =='Accepted': 
                         messages.success(request,'login success') 
                         return redirect('user_dashboard')  
                     elif user_status =='Rejected' :  
                         messages.error(request,'Your request is Rejected so you cannot login')   
                     elif user_status == 'Pending': 
                         messages.info(request,'Your request is Pending so cannot login')   
 
                      
                except: 
                     messages.warning(request,'invalid login') 
    return render(request,'user/user-login.html')

def admin_login(request):
    if request.method=='POST':
        name=request.POST.get('user_email') 
        password=request.POST.get('user_password') 
        if name=='admin@gmail.com' and password=='admin123':
           return redirect('admin_home')
    return render(request,'user/admin-login.html')

def cloud_serivce_provider_login(request):
        if request.method == 'POST': 
                email = request.POST.get('user_email') 
                print(email)
                password = request.POST.get('user_password') 
                print(password)
                try: 
                     check = Provider_registration.objects.get(provider_email=email,provider_password=password)  
                     print(check) 
                     a=request.session['provider_id']=check.provider_id  
                     print(a)
                       
                     user_status = check.provider_status 
                     if user_status =='Accepted': 
                         messages.success(request,'login success') 
                         return redirect('service_provider_dashboard')  
                     elif user_status =='Rejected' :  
                         messages.error(request,'Your request is Rejected so you cannot login')   
                     elif user_status == 'Pending': 
                         messages.info(request,'Your request is Pending so cannot login')   
 
                      
                except: 
                     messages.warning(request,'invalid login') 
        return render(request,'user/service-provider-login.html')

def user_dashboard(request):
    data=User_reviews_feedbacks.objects.all()
    return render(request,'user/user-dashboard.html',{'data':data})

def user_profile(request):
    user= request.session['user_id']
    data=user_registration.objects.filter(user_id=user)
    user=get_object_or_404(user_registration,user_id=user)
    if request.method =='POST' :
          
        user_name=request.POST.get('user_name')
        user_password=request.POST.get('user_location')

       
        
        if not request.FILES.get('profile'):
            user.user_name=user_name
            user.user_password=user_password

       
            user.save(update_fields=['user_name','user_password'])
            user.save()
            if user:
                    messages.success(request,"Your Profile is Updated")       
            else:
                pass
        if request.FILES.get('profile'):
            user_profile_upload=request.FILES('profile')
            user.user_name=user_name
            user.user_password=user_password
            user.user_profile_upload=user_profile_upload
        
            user.save(update_fields=['user_name','user_password','user_profile_upload'])
            user.save()
            if user:
                    messages.success(request,"Your Profile is Updated")       
            else:
                pass
            
        
    return render(request,'user/user-profile.html',{'data':data})

def user_activated_plans(request):
    id=request.session['user_id']
    
    data=User_Plan_Request.objects.filter(user_plan_id=id)
    # data2=UserUploadFile.objects.filter(user_upload_id=id).values('user_upload_id').count()
    # print(data2)
    return render(request,'user/user-activate-plans.html',{'data':data,})

def user_downloads(request):
    id=request.session['user_id']
    data=UserUploadFile.objects.filter(user_id=id)
    print(data)
    return render(request,'user/user-downloads.html',{'data':data})

def user_upload(request,id,planid):
    userid=request.session['user_id']
    data5=user_registration.objects.get(user_id=userid)
    
    
    data3=User_Plan_Request.objects.filter(cloud_id=id)
    print(data3)
    data=Provider_add_services.objects.get(cloud_id=id)
    print(data)
    data8=User_Plan_Request.objects.filter(cloud_id=id).filter(user_plan_id=userid).filter(plan_id=planid)
    data7=User_Plan_Request.objects.filter(cloud_id=id).filter(user_plan_id=userid).filter(plan_id=planid).values('storage_purchased_converted')
    for item in data7:
           for key, value in item.items():
               
                try:
                   ac=item[key] = int(value)
                   print(ac)
                #    convert=ac*1073741824
                #    print(convert)
                #    b= size(convert,system=alternative)
                #    print(b) 
                except :
                   ac=item[key] = (value)
                   print(ac)
    
  
   
    if request.method =='POST' and request.FILES['file_image']:
          
        file_name=request.POST.get('file_name')
        print('file_name')
        file_describition=request.POST.get('file_describition')
        
        
        upload_file=request.FILES['file_image']
        
        print(upload_file)
        file_size=upload_file.size
        print(file_size)
        file_type=upload_file.content_type
        
        #File Extension
        file_extension = file_type
        print(file_extension)
        start_index = file_extension.index("/") 
        end_index = len(file_extension)
        x =  file_extension[start_index+1:end_index]
        print("kkkkk")
        print(x)
        print("jjjj")
        
        
        
        
        
        
        print(file_type)
        if ac == 'unlimted':
            b=ac
            print(b)
        else:    
            ab=(ac)-int(file_size)
            print(ab)
            b = size(ab,system=alternative)
            
            print(b) 
        
        
        
        # file_post_name=request.POST.get('file_image')
        for i in data8:
            print(i.debited_storage)
            i.debited_storage = b
            i.save(update_fields=['debited_storage'])
        

        
           
        data22=UserUploadFile.objects.create(upload_file=upload_file,user_creator=data,file_size=file_size,file_name=file_name,file_describition=file_describition,file_type=x,user_id=data5)
        data22.save()
            
        if data22:
              messages.success(request,"Your File Is Successfully Uploaded")  
              data2=User_Plan_Request.objects.filter(cloud_id=id).filter(user_plan_id=userid).filter(plan_id=planid).update(user_upload_times=F('user_upload_times')+1)
              return redirect('user_activated_plans')     
        else:
              messages.info(request,"please check filetype and Upload file type is different ") 
              
    return render(request,'user/user-upload.html')

def user_plans(request):
    id=request.session['user_id']
    data=Provider_add_services.objects.filter(cloud_upload_status='Accepted')
   
      
      
    data2=user_registration.objects.filter(user_id=id)
  
    data3=User_Plan_Request.objects.filter(user_plan_id=id)
 
 
    return render(request,'user/user-plans.html',{'data':data,'data2':data2,'data3':data3})


def user_plan_request(request,id):
    data3=Provider_add_services.objects.filter(cloud_id=id)
    user=request.session['user_id']
    data = user_registration.objects.get(user_id=user)
    
    user_plan_request_status = 'Pending'
    hi=User_Plan_Request.objects.create(user_plan_request_status=user_plan_request_status,user_plan_id=data,cloud_id=data3)
    hi.save()
     #file encryption start
   
  
    # data.user_plan_request_status = 'Pending'
    # data.save(update_fields=['user_service_request_status'])
    # data.save()
    # print("this is accept")
   
    a=data.user_email
    print(a)
    
     #email message
    html_content =  "<br/> <p>   Your Application has been Sent.Please wait For Approval .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [a]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("MCDM Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    try:
        if msg.send():
            print(msg)
            return redirect('user_plans')
    except:
        pass
    return redirect('user_plans')

def user_activated_plans_review(request,id,planid):
    user2= request.session['user_id']
    data55=user_registration.objects.get(user_id=user2)
    data=User_Plan_Request.objects.filter(plan_id=planid).filter(user_plan_id=user2)
    data2=Provider_add_services.objects.get(cloud_id=id)
    data5=User_reviews_feedbacks.objects.filter(product_id=id)
      
    # bb=str(hh)
    # h6=statistics.mean(bb)
    # print(str(h6))
    
   
    # for i in list(data5):
    #     v=([int(i.feedback_agility),int(i.feedback_usability),int(i.feedback_performance),int(i.feedback_security_privacy)])
    #     ac=sum(v)
    #     # az=(ac)
    #     z=statistics.mean(v)
        # print(str(z))
        # ax=[]
        # ax.append(z)
        # print(ax)
      
     
        # app=[]
        # for r in str(z):
        #     app.append(z)
         #     print(app)
   
    if request.method == 'POST':
        feedback_performance=request.POST.get('performance')
        feedback_usability=request.POST.get('usability')
        feedback_agility=request.POST.get('review')
        feedback_security_privacy=request.POST.get('Security')
        feedback_describtion=request.POST.get('describtion')
        feedback_Assurance=request.POST.get('feedback')
        feeback_financial=request.POST.get('rrating')
        feedback_accountability=request.POST.get('rating')
        a=[int(feedback_performance),int(feedback_usability),int(feedback_agility),int(feedback_security_privacy),int(feedback_Assurance),int(feeback_financial),int(feedback_accountability)]
        z=statistics.mean(a)
        print(z)
        za=(round(z,1))
        
        data52=User_reviews_feedbacks.objects.filter(product_id=id).aggregate(avg=Avg('user_review'))
        print(data52)
        
        # h=data52['user_review__avg']
        # h6=(round(h,1))
        hh=data52['avg']
        if hh == None:
           h6=(za)
           print(h6)
        else:
            h6=(round(hh,1))
            print(h6)
        data2.user_reviews=h6
        ar=(int(data2.user_review_counts)+ int(1))
    
        data2.user_review_counts=ar
    
        

        
       
        # print(add(a))
        data5555=User_reviews_feedbacks.objects.create(feedback_performance=feedback_performance,
                                           feedback_usability=feedback_usability,
                                           feedback_agility=feedback_agility,
                                           feedback_security_privacy=feedback_security_privacy,
                                           feedback_describtion=feedback_describtion,product_id=data2,
                                           user_review=za,user_id=data55,feedback_Assurance=feedback_Assurance,feeback_financial=feeback_financial,feedback_accountability=feedback_accountability)
        data2.save(update_fields=['user_reviews','user_review_counts'])
        data2.save()
        
        if data5555:
          
            data22=User_Plan_Request.objects.filter(cloud_id=id).filter(user_plan_id=user2).filter(plan_id=planid).update(user_upload_times=F('user_upload_times')+int(1))
            print(data22)
            messages.success(request,"Your Review Is Successfully Uploaded")  
            return redirect('user_activated_plans')     
        else:
              pass
        
    
    return render(request,'user/user-activated-plan-reviews.html',{'data':data,'data555':data5})

def user_register(request):
    if request.method =='POST' and request.FILES['user_upload']:
        user_name=request.POST.get('user_name')
        user_mobilenumber=request.POST.get('user_mobile')
        user_email=request.POST.get('user_email')
        user_password=request.POST.get('user_password')
        user_date_of_birth=request.POST.get('user_birth')
        user_profile_upload=request.FILES['user_upload']
        data5555=user_registration.objects.create(user_password=user_password,user_name=user_name,
                                         user_mobile=user_mobilenumber,user_email=user_email,
                                         user_date_of_birth=user_date_of_birth,
                                         user_profile_upload=user_profile_upload)
        if data5555:
              messages.success(request,"Your Registration Is Successfully Completed")  
                  
        else:
              pass
    return render(request,'user/user-register.html')

def csmic_login(request):
    if request.method=='POST':
        name=request.POST.get('user_email') 
        print(name)
        password=request.POST.get('user_password') 
        print(password)
        if name=='csmic@gmail.com' and password=='csmic123':
            
            return redirect('csmic_dashboard')
    return render(request,'user/csmi-login.html')

def logout(request):
    
    request.session['user_id'] == None
         
    return redirect('home')
   
    
def serviceprovider_registration(request):
    if request.method =='POST' and request.FILES['user_upload']:
        Provider_name=request.POST.get('user_name')
        provider_mobile=request.POST.get('user_mobile')
        provider_email=request.POST.get('user_email')
        provider_password=request.POST.get('user_password')
        provider_date_of_birth=request.POST.get('user_birth')
        provider_profile=request.FILES['user_upload']
        if Provider_registration.objects.filter(provider_email=provider_email).exists():
                messages.error(request,"Email Already Existed")
                return redirect("serviceprovider_registration")
        else:
             data5555=Provider_registration.objects.create(Provider_name=Provider_name,provider_mobile=provider_mobile,
                                             provider_email=provider_email,provider_password=provider_password,
                                             provider_date_of_birth=provider_date_of_birth,provider_profile=provider_profile)
        
        if data5555:
            messages.success(request,"Your Registration Form Is Successfully Uploaded")       
        else:
            pass
       
      
    return render(request,'user/cloudserviceprovider-registration.html')

def cloud_plans(request):
    user= request.session['user_id']
    print(user)
    data=Provider_add_services.objects.filter(cloud_upload_status='Accepted').all()
    for i in data:
       z= list((i.user_review_counts))
       print(z)
    # data23=Provider_add_services.objects.filter(cloud_upload_status='Accepted').values('user_review_counts') 
 
    
   
   
      
    data98=Provider_add_services.objects.filter(cloud_upload_status='Accepted').order_by('-user_review_counts').first()
    a=(data98.user_review_counts)
    print(a)
    data58=Provider_add_services.objects.filter(cloud_upload_status='Accepted').aggregate(abhi2=(Max('user_reviews')) )
    b=(data58['abhi2'])
    print(b)
    
    # data5=(Provider_add_services.objects.filter(cloud_upload_status='Accepted').filter(user_review_counts=a).filter(user_reviews=b) or Provider_add_services.objects.filter(cloud_upload_status='Accepted').filter(user_review_counts=a)).exclude(user_review_counts='0')
    # print(data5)
    data5=Provider_add_services.objects.filter(cloud_upload_status='Accepted').exclude(user_review_counts='0')
 
 
  
  
   
    data2=(Provider_add_services.objects.filter(cloud_upload_status='Accepted').order_by('cloud_Basic_price').first()) or (Provider_add_services.objects.order_by('cloud_Business_price').first()) or (Provider_add_services.objects.order_by('cloud_Premium_price').first())
    data3=(Provider_add_services.objects.filter(cloud_upload_status='Accepted').filter(cloud_agility='Fast',cloud_performance='Fast',cloud_security_and_privacy='High') or Provider_add_services.objects.filter(cloud_upload_status='Accepted').filter(cloud_agility='Smooth',cloud_performance='Fast',cloud_security_and_privacy='High') or Provider_add_services.objects.filter(cloud_upload_status='Accepted').filter(cloud_security_and_privacy='Medium',cloud_performance='Smooth',cloud_agility='Fast'))
    reviews=User_reviews_feedbacks.objects.all()
    data4=User_reviews_feedbacks.objects.filter(product_id__in=[review.product_id for review in reviews]).aggregate(Avg(F('feedback_performance')))
    data55=User_Plan_Request.objects.filter(user_plan_id=user)
    data59=User_Plan_Request.objects.filter(user_plan_id=user).values('cloud_id')

    # for i in data55:
    # print(data55)
   
    print(data4,'ghghg')
    
    
   
    data88=Provider_add_services.objects.filter(cloud_upload_status='Accepted').values('user_reviews')
 
    
    
    
       
    for item in data88:
        for key, value in item.items():
            
            try:
                ac=item[key] = float(value)
                print((ac))
                 
            except :
               print('pass')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # a=dict(data4)
    # print((a))
    
    
    
    
    
    
    
    
    # data5=User_reviews_feedbacks.objects.all().aggregate(Count('userfeedback_id'))
    # print(type(data5))
    # h=data5['userfeedback_id__count']
    # print(h)
    # c=a['feedback_performance__avg'],a['feedback_usability__avg'],a['feedback_agility__avg'],a['feedback_security_privacy__avg']
    # z=statistics.mean(c)
    # # f=(Avg(c))
    # print(round(z,1))
    
  
    
    
    # b=(Sum(c))
    
    # print(b)
    # data5=User_reviews_feedbacks.objects.all().aggregate(Count('userfeedback_id'))
    # print(data5)
    # dat1=(data5['userfeedback_id__count'])
    # dat=round(data4["feedback_performance__avg"],1)
    # print(dat)
    
    
    
    return render(request,'user/csmi.html',{'data':data,'data2':data2,'data3':data3,'data5':data5,'data55':data55,'data59':data59})

def purchased_plan(request,id):


    user= request.session['user_id']
    user_purchased = 'Purchased'
    data=user_registration.objects.get(user_id=user)
    data2=get_object_or_404(Provider_add_services,cloud_id=id)
    user=User_Plan_Request.objects.create(user_purchased=user_purchased,cloud_id=data2,user_plan_id=data)
    
    
    if user:
            messages.success(request,"Your Susccessfully Purchased")  
                  
    else:
            pass
    # if user_purchased == 'Purchased' :
        
    # data2.cloud_purchase_user_id='Re'
    # data2.save(update_fields=['cloud_purchase_user_id'])
    # data2.save()
    return redirect('cloud_plans')

def payment_gateway(request,id):
    data5=Provider_add_services.objects.filter(cloud_id=id)
    user= request.session['user_id']
    user_purchased = 'Purchased'
    data=user_registration.objects.get(user_id=user)
    data2=get_object_or_404(Provider_add_services,cloud_id=id)
    
    if request.method=='POST':
       user_address=request.POST.get('user_address')
       purchased_price=request.POST.get('plan')
       print(purchased_price)
       user_card_no=request.POST.get('cardno')
       
      
       data6=Provider_add_services.objects.filter(cloud_id=id).filter(cloud_Basic_price=purchased_price).values('cloud_Basic_monthly_usage_data') or Provider_add_services.objects.filter(cloud_id=id).filter(cloud_Business_price=purchased_price).values('cloud_Business_monthly_usage_data') or Provider_add_services.objects.filter(cloud_id=id).filter(cloud_Premium_price=purchased_price).values('cloud_Premium_monthly_usage_data')
       
    
       
       
       for item in data6:
           for key, value in item.items():
               
                try:
                   ac=item[key] = int(value)
                   print(ac)
                   convert=ac*1073741824
                   print(convert)
                   b= size(convert,system=alternative)
                   print(b) 
                except :
                   convert=item[key] = (value)
                   print(convert)
                   b= (convert)
                   print(b)
                 
                       
 
       user=User_Plan_Request.objects.create(user_purchased=user_purchased,cloud_id=data2,user_plan_id=data,user_address=user_address,purchased_price=purchased_price,user_card_no=user_card_no,storage_purchased_converted=convert,storage_purchased=b,debited_storage=b)    
       if user:
            data22=Provider_add_services.objects.filter(cloud_id=id).update(user_purchase_counts=F('user_purchase_counts')+1)

            messages.success(request,"Your Susccessfully Purchased")  
            return redirect('user_activated_plans')       
       else:
            pass
    
    
    return render(request,'user/payment-gateway.html',{'data':data5})

