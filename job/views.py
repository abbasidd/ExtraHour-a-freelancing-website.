from django.shortcuts import render
from . import models
from django.db.models import Q
from client import models as c_model
from freelancer import models as f_model
from django.contrib.postgres.search import SearchVector


def post_job(request):
    if request.method == 'POST':

        main_skill = request.POST['main_skill']
        main_skill_obj = f_model.Skill.objects.get(skill_name=main_skill)

        #skill_name = request.POST['skill_name']

        duration_text = request.POST['duration_text']
        
        title = request.POST['title']
        complexity_text = request.POST['complexity_text']
        complexity = models.Complexity.objects.get(
            complexity_text=complexity_text)

        hire_manager_obj = c_model.Hire_manager.objects.get(user=request.user)
        #hire_manager_obj = c_model.Hire_manager.objects.get(id=hire_manager_id)

        # main Skill
        expected_duration = models.Expected_duration(
            duration_text=duration_text)
        expected_duration.save()


        description = request.POST['description']
        payment_amount = request.POST['payment_amount']
        job_obj = models.Job(title=title, payment_amount=payment_amount, description=description,
                             expected_duration=expected_duration, complexity=complexity, hire_manager=hire_manager_obj, main_skill=main_skill_obj)
        job_obj.save()
        other_skills = [20]
        skill = request.POST.getlist('other_skills')
        i = 0
        for kills in skill:
            expected_duration.other_skill.add(f_model.Skill.objects.get(skill_name=kills))
            # i += 1
            # models.Other_skills(skill=other_skills[i], job=job_obj).save()
        #    i+=1
        expected_duration.save()
        return render(request, 'test.html')
    else:
        skills = f_model.Skill.objects.all()
        context = {'skills': skills,
                   'complexity': models.Complexity.objects.all()}
        return render(request, 'post-job.html', context)


def job_single(request, job_id):
    job = models.Job.objects.get(pk=job_id)
    all_jobs = models.Job.objects.filter(
        main_skill=job.main_skill).exclude(pk=job_id)
    suggested_jobs = models.Job.objects.filter(main_skill=job.main_skill)
    other_skills = job.expected_duration.other_skill.all()

    # for skill in other_skills:
    #     i = 0
    #     all_[i] = models.Job.objects.filter(main_skill = skill.skill)
    #     i += 1

    context = {'job': job, 'suggested_jobs': suggested_jobs,
               'other_skills': other_skills, 'all_jobs': all_jobs}
    return render(request, 'job-single.html', context)


def job_search(request):
    job = models.Job.objects.none()
    other_skill_job = models.Expected_duration.objects.none()
    skill = request.GET.getlist('skill')

    if len(request.GET['query']) > 200:
        return render(request,'index.html')
    
    if skill:
        other_skill_job = models.Job.objects.filter(
            expected_duration__other_skill__skill_name__in=skill)
    #     other_skill_job = models.Job.objects.filter(
    #         expected_duration__other_skill__skill_name__in=skill)
        # for skills in skill:
        #     other_skill_exd = other_skill_exd.union(models.Expected_duration.objects.filter(other_skill__skill_name = skills))
        #     for jobb in Ex_D:
        #         job=models.Job.objects.get(expected_duration = jobb)
        #         list.append(job)

    elif request.GET['query']:
        more_jobs = models.Job.objects.filter(
            Q(title__icontains=request.GET['query'])
            | Q(main_skill__skill_name__icontains=request.GET['query']) |
            Q(description__icontains=request.GET['query']) | Q(
                hire_manager__location__icontains=request.GET['query'])
        )

        jobs = models.Job.objects.annotate(
            search=SearchVector(
                'title', 'main_skill__skill_name', 'description')
        ).filter(search=request.GET['query'])
        other_skill_job = models.Job.objects.filter(
            expected_duration__other_skill__skill_name__in=skill)
        job = jobs | more_jobs | other_skill_job
        return render(request, 'job-search.html', {'jobs': job })

    elif len(request.GET['query']) == 0 and len(skill) == 0:
        job = models.Job.objects.all()
        
        return render(request, 'job-search.html', {'jobs': job })
        
    # job= job | job_skill
    # skills = f_model.Skill.objects.all()
    # query = request.GET['query']
    # job_title = models.Job.objects.filter(title__icontains = query)
    # job_skills = models.Job.objects.filter(main_skill__skill_name__icontains = query)
    # job_description = models.Job.objects.filter(description__icontains = query)
    # job_otherskill = models.Job.objects.none()
    # job = models.Job.objects.none()
    # otherskill = models.Other_skills.objects.filter(skill__skill_name__icontains = query)
    # if otherskill.count() == 0 :
    #     pass
    # else:
    #     for skill in job_otherskill:
    #         job_otherskil = skill.job
    #         job_otherskill.union(job_otherskil)

    # job =job.union(job_title,job_skills,job_description,job_otherskill)'more_jobs': more_jobs, 'other_skill_job': other_skill_job
    return render(request, 'job-search.html', {'jobs': job })

def job_listing(request):
    job=models.Job.objects.all()
    skill = f_model.Skill.objects.all()
    print(request.user.freelancer)
    freelancer = request.user.freelancer
    print(freelancer.user)
    return render(request,'job-listings.html',{'user':request.user,'jobs':job , 'skill' : skill })