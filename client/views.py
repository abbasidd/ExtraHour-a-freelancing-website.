from django.shortcuts import render , redirect
from django.contrib.auth import models
from django.contrib import messages 
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from . import models
from purposal_contract import models as p_model
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from job import models as j_model



def signup_client(request):
    if request.method == 'POST':
        #skill_name = request.POST['skill_name']
        
        

        user = request.user
        location = request.POST['location']
        profile_pic = request.FILES['profile_pic']
        #registration_date= request.POST['registration_date']
        company= request.POST['company']
        if  models.Company.objects.filter(company_name=company) :
            company = models.Company.objects.get(company_name=company)
            hire_manager_obj = models.Hire_manager(user=user,location=location,company=company)
            hire_manager_obj.save()
        else:
            hire_manager_obj = models.Hire_manager(user=user,location=location)
            hire_manager_obj.save()
            #company = models.Company.objects.get(company_name=company)
        user = request.user
        email = user.email


        current_site = get_current_site(request)
        message = render_to_string('acc_active_email.html', {
                    'user':user, 
                    'domain':current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
        mail_subject = 'Activate your ExtraHour account.'
        to_email = email
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()
        user.is_active= False
        return HttpResponse('Please confirm your email address to complete the registration')

        return render(request,'index.html')
        

    else :
          return render(request,'signup_client.html')
# Create your views here.

def signup_company(request):
    if request.method == 'POST':
        #skill_name = request.POST['skill_name']
        
        company_name = request.POST['company_name']
        company_location = request.POST['company_location']
        if models.Company.objects.filter(company_name = company_name):
            #same name not register
             return HttpResponse("company name is not valid!")
        else:
            company_obj = models.Company(company_name = company_name,company_location = company_location)
            company_obj.save()
            return HttpResponse("company is save")
            #user = request.user
            #hire_manager_obj = models.Hire_manager.objects.get(user=user)
            #hire_manager_obj.company= company_obj
            #hire_manager_obj.save()
    else :
        return render(request, 'signup_company.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        #login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
#user purposal dkhay ga phr click kray ga
def purposal_list(request, job_id):
    job = j_model.Job.objects.get(pk = job_id)
    purposal = p_model.Purposal.objects.filter(job = job)
    return render(request,'purposal_list.html',{'purposal':purposal}) 

def purposal_single(request , purposal_id):
    purposal = p_model.Purposal.objects.get(pk = purposal_id)
    return render(request,'purposal_single.html',{'purposal':purposal})