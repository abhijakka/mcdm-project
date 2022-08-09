"""mcdmproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from userapp import views as user_views
from adminapp import views as admin_views
from csmicapp import views as csmic_views
from cloudserviceproviderapp import views as cloudserviceprovider_views


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('admin_home', admin_views.admin_home ,name='admin_home'),
    path('admin_view_service_provider', admin_views.admin_view_service_provider,name='admin_view_service_provider'),
    path('admin_user_signup_request', admin_views.admin_user_signup_request ,name='admin_user_signup_request'),
    path('user_registration_accept/<int:id>/', admin_views.user_registration_accept ,name='user_registration_accept'),
    path('user_registration_reject/<int:id>/', admin_views.user_registration_reject ,name='user_registration_reject'),
    path('Provider_registration_accept/<int:id>/', admin_views.Provider_registration_accept ,name='Provider_registration_accept'),
    path('Provider_registration_reject/<int:id>/', admin_views.Provider_registration_reject ,name='Provider_registration_reject'),
    path('logoutadmin', admin_views.logoutadmin ,name='logoutadmin'),
    path('service_provider_dashboard', cloudserviceprovider_views.service_provider_dashboard,name='service_provider_dashboard'),
    path('service_provider_profile', cloudserviceprovider_views.service_provider_profile ,name='service_provider_profile'),
    path('service_provider_add_services', cloudserviceprovider_views.service_provider_add_services ,name='service_provider_add_services'),
    path('service_provider_manage/<int:id>/', cloudserviceprovider_views.service_provider_manage ,name='service_provider_manage'),
    path('service_provider_view_added_services', cloudserviceprovider_views.service_provider_view_added_services ,name='service_provider_view_added_services'),
    path('logoutcsr', cloudserviceprovider_views.logoutcsr ,name='logoutcsr'),
    # path('', cloudserviceprovider_views. ,name=''),
    
    path('csmic_dashboard', csmic_views.csmic_dashboard ,name='csmic_dashboard'),
    path('csmic_request', csmic_views.csmic_request ,name='csmic_request'),
    path('csmic_service_provider_requset', csmic_views.csmic_service_provider_requset ,name='csmic_service_provider_requset'),
    path('csmic_view_accepted/<int:id>/', csmic_views.csmic_view_accepted ,name='csmic_view_accepted'),
    path('service_provider_csmic_accept/<int:id>/', csmic_views.service_provider_csmic_accept ,name='service_provider_csmic_accept'),
    path('service_provider_csmic_reject/<int:id>/', csmic_views.service_provider_csmic_reject ,name='service_provider_csmic_reject'),
    path('user_plan_request_accept/<int:id>/', csmic_views.user_plan_request_accept ,name='user_plan_request_accept'),
    path('user_plan_request_reject/<int:id>/', csmic_views.user_plan_request_reject ,name='user_plan_request_reject'),
    path('logoutcsmic', csmic_views.logoutcsmic ,name='logoutcsmic'),
    
    
    
    
    
    
    path('', user_views.home ,name='home'),
    path('publicplans', user_views.publicplans ,name='publicplans'),
    path('contact', user_views.contact ,name='contact'),
    path('user_login', user_views.user_login ,name='user_login'),
    path('admin_login', user_views.admin_login ,name='admin_login'),
    path('cloud_serivce_provider_login', user_views.cloud_serivce_provider_login ,name='cloud_serivce_provider_login'),
    path('user_dashboard', user_views.user_dashboard ,name='user_dashboard'),
    path('user_profile', user_views.user_profile ,name='user_profile'),
    path('user_activated_plans', user_views.user_activated_plans ,name='user_activated_plans'),
    path('user_downloads', user_views.user_downloads ,name='user_downloads'),
    path('user_upload/<int:id>/<int:planid>', user_views.user_upload ,name='user_upload'),
    path('user_plans', user_views.user_plans ,name='user_plans'),
    path('user_activated_plans_review/<int:id>/<int:planid>', user_views.user_activated_plans_review ,name='user_activated_plans_review'),
    path('logout', user_views.logout ,name='logout'),
    path('user_register', user_views.user_register ,name='user_register'),
    path('csmic_login', user_views.csmic_login ,name='csmic_login'),
    path('serviceprovider_registration', user_views.serviceprovider_registration ,name='serviceprovider_registration'),
    path('user_plan_request/<int:id>/', user_views.user_plan_request ,name='user_plan_request'),
    path('cloud_plans', user_views.cloud_plans ,name='cloud_plans'),
    path('purchased_plan/<int:id>/', user_views.purchased_plan ,name='purchased_plan'),
    path('payment_gateway/<int:id>/', user_views.payment_gateway ,name='payment_gateway'),
    # path('', user_views. ,name=''),
    
    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

