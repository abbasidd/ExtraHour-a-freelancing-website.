from django.shortcuts import render , redirect
from django.contrib.auth import models
from django.contrib import messages 
from django.core.mail import send_mail
from django.http import HttpResponse , JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from job import models as j_model
from freelancer import models as f_model
from skill_test import models as t_model
import json

def Logout(request):
    logout(request)
    return redirect('/accounts/')

def home(request):
    #send_mail('subject', 'body of the message', 'usmanaftababbasi420@gmail.com', ['abdul.bsit110@iiu.edu.pk',])
 #   request.user
    # freelancer = f_model.Freelancer.objects.get(user= request.user)
    # quiz = t_model.QuizTakers.objects.get(freelancer = freelancer)
 
    job=j_model.Job.objects.all()
    skill = f_model.Skill.objects.all()
 
    freelancer = request.user.freelancer
    return render(request,'index.html',{'freelancer':freelancer,'jobs':job , 'skill' : skill })

    return render(request,'index.html',{'user':request.user,'jobs':job , 'skill' : skill })
# Create your views here.


def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
          
            context = {'user':user}
            login(request,user)
         #   user.is_authenticated()
            return redirect('accounts:home')
            # User is authenticated
        else:
            return HttpResponse("not successful")

    else:    
        return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2 :
            if models.User.objects.filter(username = username):
                messages.info(request,'username taken')
                return redirect('accounts:signup')

            elif not models.User.objects.filter(email = email):
                user = models.User.objects.create_user(first_name = first_name , last_name=last_name,username=username,email=email,password = password1)
                
                user.save()
                login(request,user)
                return render(request,'signup_choice.html')

               
                
               


                return redirect('freelancer:signup_freelancer')
            else:
                messages.info(request,'email taken')
                return redirect('accounts:signup')    
        return redirect("accounts:signup")   
    else:

        return render(request,'signup.html') 


@csrf_exempt
def check_username_exist(request):
    username=request.POST.get("username")
    print()
    print(username)
    user_obj=User.objects.filter(username__icontains = username).exists()
    if user_obj:
        return HttpResponse(json.dumps({'r':'taken'}),content_type='text/json-comment-string', status= 200) 
    else :
         return JsonResponse({'r':'good'}, status= 200)


    
def reset_form(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = models.User.objects.get(email = email)
        current_site = get_current_site(request)
        message = render_to_string('reset_email.html', {
                    'user':user, 
                    'domain':current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
        mail_subject = 'Reset your ExtraHour account\'s password.'
        to_email = email
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()
        return render(request,'reset_done.html')
   
    else:
        return render(request,"reset_form.html")

def reset_done(request):
    return render(request,'reset_done.html')

def reset_confirm(request , uidb64 = None, token= None ):
    if request.method == 'POST':
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        password  = request.POST['password1']
        user.set_password(password)
        user.save()
        return render(request,'reset_complete.html')
    else:
        return render(request,'reset_confirm.html')




def about_us(request):
    return render(request , 'about.html')

def contact(request):
    return render(request, 'contact.html')


def blog(request):
    return render(request , 'blog.html')

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

