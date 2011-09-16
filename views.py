from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from mongoengine.django.auth import User
from models import TextPost, Post

def create(request, name):

#    user = User.create_user(username='jill', email='lennon@thebeatles.com', password='jill')
#    user.is_staff = True
#    user.save()
    post1 = TextPost(title='Fun with MongoEngine', author=name)
    post1.save()
    return HttpResponse("Created")

@login_required(login_url='/accounts/login')
def show(request):
    return render_to_response("post.html",{"posts":Post.objects})

def home(request):
    return HttpResponse("home")


