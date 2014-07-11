from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from listing1.models import Post1

def show(request,post_id):
    post = Post1.objects.get(id=post_id)
    template = loader.get_template('listing1/post.html')
    context = RequestContext(request, {'post': post,})
    return HttpResponse(template.render(context))

def index(request):
    posts = Post1.objects.all().order_by('-pub_date')
    template = loader.get_template('listing1/index.html')
    context = RequestContext(request, {'posts': posts,})
    return HttpResponse(template.render(context))

def ranking(request):
    template = loader.get_template('listing1/ranking.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def shop(request):
    template = loader.get_template('listing1/shop.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

