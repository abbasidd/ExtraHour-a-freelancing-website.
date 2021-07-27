from django.shortcuts import render
from job import models as j_model
from client import models as c_model
from freelancer import models as f_model
from . import models
from itertools import chain
from datetime import datetime ,timedelta
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

def purposal(request,job_id):
    if request.method == 'POST':
        freelancer = f_model.Freelancer.objects.get(user = request.user)
        if freelancer.bid > 0: 
            freelancer.bid -= 1
            freelancer.save()
            description = request.POST['description']
            title = request.POST['title']
            payment_typ = request.POST['payment_type']
            payment_type = f_model.Payment_type.objects.get(type_name=payment_typ)   
            job_id = request.POST['job_id']
            job = j_model.Job.objects.get(pk = job_id)
            payment_amount =request.POST['payment_amount']
            days = request.POST['days']
            purposal_status_catalog = models.Purposal_status_catalog.objects.get(status_name='Open')
            models.Purposal(title =title,purposal_status_catalog=purposal_status_catalog,days=days,description=description,payment_type=payment_type,job=job,freelancer=freelancer,payment_amount=payment_amount).save()
            return render(request,'purposal.html')
        else :
            return HttpResponse("please upgrade ur bid")
    else:
        payment_type = f_model.Payment_type.objects.all()
        return render(request,'purposal.html',{'job_id':job_id ,'payment_type':payment_type})
def activate(request, purposal_id, token):
    
    purposal_id = force_text(urlsafe_base64_decode(purposal_id))
    user = models.Purposal.objects.get(pk = purposal_id )
    if account_activation_token.check_token(user, token):
        purposal =user
        job = purposal.job

        purposal_status_catalog =models.Purposal_status_catalog.objects.get(status_name = 'Awaiting Acceptance')
        purposal.purposal_status_catalog = purposal_status_catalog
        purposal.save()

        hire_manager = c_model.Hire_manager.objects.get(user = request.user)
        company = hire_manager.company
        freelancer = f_model.Freelancer.objects.get(user = purposal.freelancer.user)
        end_time = datetime.now() + timedelta(days = purposal.days)
        payment_type = purposal.payment_type
        payment_amount = purposal.payment_amount
        models.Contract(payment_amount=payment_amount,payment_type=payment_type,end_time=end_time,freelancer=freelancer,company=company,purposal=purposal).save()
        return HttpResponse('contract is done')
        
    


def contract(request ,purposal_id, freelancer_id):
    user = request.user
    purposal = models.Purposal.objects.get(pk = purposal_id )
    purposal_status_catalog =models.Purposal_status_catalog.objects.get(status_name = 'Awaiting Acceptance')
    purposal.purposal_status_catalog = purposal_status_catalog
    purposal.save()

    email = f_model.Freelancer.objects.get(pk = freelancer_id).user.email


    current_site = get_current_site(request)
    message = render_to_string('contract_email.html', {
                        'freelancer': purposal.freelancer.user.username,
                        'user':purposal, 
                        'domain':current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(purposal_id)),
                        'token': account_activation_token.make_token(user),
                    })
    mail_subject = 'Activate your ExtraHour account.'
    to_email = email
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()
    return HttpResponse('contract is done')


    

def message_listing(request):
    freelancers = models.freelancer_recipient.objects.filter(message__creator = request.user).distinct('freelancer')
    print(freelancers)
    message = []
    i = 1
    j = 0 
    for f in freelancers:
        print( '1')
        freelance = f_model.Freelancer.objects.get(pk = f.freelancer.id)
        
        message.append(models.freelancer_recipient.objects.filter(freelancer=freelance).last())
        print( '3')
        i = i+1
        j = j+1
    print(message[0].message.message_text)
    zip_list = zip(freelancers,message)
    return render(request , 'message.html' , {'freelancers':zip_list})
    
@csrf_exempt
def client(request):
    if request.user.profile.type == True :
        print(request.POST.get('purposal_status_catalog_id') + 'iiui' )
        # print(int(request.POST.get('purposal_status_catalog_id')))
        purposal_status_catalog_id = request.POST.get('purposal_status_catalog_id')
        purposal_status_catalog = models.Purposal_status_catalog.objects.get(pk = int(purposal_status_catalog_id))
        creator = request.user
        print(request.POST.get('p_id'))
        p_id = int(request.POST.get('p_id'))
        purposal = models.Purposal.objects.get(pk=p_id)
        message_text = request.POST.get('message_text')
        message = models.Message(creator=creator,message_text=message_text,purposal=purposal,purposal_status_catalog=purposal_status_catalog)
        message.save()
        parent_id = message.id - 1
        if parent_id > 0 :
            print(parent_id)
            # models.Parent_message(parent = models.Message.objects.get(pk=parent_id)).save() 
            print(parent_id)
            message.save()
        else:
            message.save()
        #print('ydhjdjshjkhdskj')        
        parent_id = message.id - 1
        f_id = int(request.POST.get('f_id'))
        freelancer = f_model.Freelancer.objects.get(pk = f_id)
        models.freelancer_recipient(message=message,is_read =False,freelancer=freelancer).save()
        
        #return HttpResponse(json.dumps({'ss':'asas'}),content_type='text/json-comment-string',status = 200) 
