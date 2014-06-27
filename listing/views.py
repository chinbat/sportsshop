from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from listing.models import Post

#def show(request, post_id):
#    return HttpResponse('This is post %s', % post_id)
def show(request,post_id):
    post = Post.objects.get(id=post_id)
    template = loader.get_template('listing/post.html')
    context = RequestContext(request, {'post': post,})
    return HttpResponse(template.render(context))

def index(request):
    posts = Post.objects.all()
    template = loader.get_template('listing/index.html')
    context = RequestContext(request, {'posts': posts,})
    return HttpResponse(template.render(context))
