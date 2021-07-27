from django.shortcuts import render , redirect
from django.contrib.auth import models
from django.contrib import messages 
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

def signup_freelancer(request):
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
    return HttpResponse('Please confirm your email address to complete the registration')

    return render(request, 'signup_freelancer.html')
# Create your views here.
