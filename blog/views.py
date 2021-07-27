from django.shortcuts import render
from .models import *
from datetime import datetime
from django.http import HttpResponse , JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

def post_blog(request):
    if request.method == 'GET':
        catagory = Catagory.objects.all()
        tag = Tag.objects.all()
        print(catagory)
        return render(request, 'post_blog.html',{'tag':tag , 'catagory' : catagory})
    else:
        user = request.user
        title = request.POST['title']
        pic = request.FILES['pic']
        summary = request.POST['summary']
        content = request.POST['content']
        published = True
        tags = request.POST.getlist('tag')
        print(tags)
        catagorys = request.POST.getlist('catagory')
        
        post = Post(user=user,title=title,pic=pic,summary=summary,content=content,published=published,published_at=datetime.now())
        post.save()
        if len(tags) > 0:
            for tag in tags:
                tagg = Tag.objects.filter(title = tag).first()
                post.tag.add(tagg)
            post.save()
        if len(catagorys) > 0:
            for cat in catagorys:
                catagory = Catagory.objects.filter(title = cat).first()
                post.catagory.add(catagory)
            post.save()
        
def blog(request):
    blog = Post.objects.all()
    return render(request,'blog.html',{'blogs':blog})

def blog_single(request,id):
    blog = Post.objects.get(id = id )
    return render(request,'blog-single.html',{'blog':blog})
def publish_dashboard(request):
    pass


@csrf_exempt
def post_comment(request):
    print('sdjgksjafkjsfahasfhk')
    pos = request.POST.get('post_id')
    print(pos)
 
    post = Post.objects.get(pk = int(pos))
    message = request.POST.get('message')
    print(message)
    # content = request.POST['content']
    Comment(post = post , title ='shajkdfhsjkl' , content = message).save()
    return render(request,'blog.html',{'blogs':blog})
def publish_comment(request,id):
    comment = Comment.objects.get(id = id)
    comment.published = True
    comment.save()

@csrf_exempt
def comment_reply(request , id):
    pos = int(request.POST['comment_id'])
    comment = Comment.objects.get(id = pos)
    title = request.POST['title']
    content = request.POST['content']
    Comment(comment = comment , title =title , content = content).save()


def publish_comment_reply(request,id):
    comment = Comment_reply.objects.get(id = id)
    comment.published = True
    comment.save()
# Create your views here.
