from django.shortcuts import render , redirect
from django.contrib.auth import models
from freelancer import models as f_model
from django.contrib import messages 
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from . import models
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

def test(request):
    return render(request, 'test.html')



def signup_freelancer(request):
    if request.method == 'POST':
        #skill_name = request.POST['skill_name']
        user = request.user
        location = request.POST['location']
        profile_pic = request.FILES['profile_pic']
        overview = request.POST['overview']
        freelance = models.Freelancer(user = user,location = location,profile_pic=profile_pic,overview=overview)
        freelance.save()

        freelance = models.Freelancer.objects.get(user = request.user)
        skills = request.POST['skills']
        skill = models.Skill.objects.get(skill_name=skills)
        freelance.skill.add(skill)
        

        certification_name = request.POST['certification_name']
        provider= request.POST['provider']
        description= request.POST['description']
        date_earned= request.POST['date']
        certification_link= request.POST['certification_link']
        certification_obj =models.Certification.objects.create(freelancer = freelance,provider=provider,certification_name=certification_name,description=description,certification_link=certification_link,date_earned=date_earned)
        certification_obj.save()
        
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
        

    else :
        f_model.Skill.objects.all()
      
        return render(request, 'freelancer_signup.html',{'skills':  f_model.Skill.objects.all()})
    
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.login()
        user.save()
        #login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def portfolio_save(request):
    if request.method == 'POST':
        freelancer = models.Freelancer.objects.get(user = request.user)
        project_name= request.POST['project_name']
        short_description= request.POST['short_description']
        skill= request.POST['skill']
        image= request.FILES['image']
        portfolio_obj = models.Portfolio(freelancer=freelancer,project_name=project_name,short_description=short_description)
        
        skills = request.POST['skills']
        skill = models.Skill.objects.get(skill_name=skills)
        portfolio_obj.skill.add(skill)

        portfolio_obj.save()
# portfolio_obj = models.Prtfoil.objects.get(freelancer=freelancer)
        image_obj =models.Images(image=image ,portfolio=portfolio_obj )
        image_obj.save()
        
       
        return HttpResponse("ok") 
    else:
        return render(request, 'signup_client.html')
    