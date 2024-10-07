from typing import Any

from django.http import Http404, HttpRequest
from django.shortcuts import render

from blog.data import posts

# Create your views here.

def blog(request):
    print('blog', request)
    context = {
        # 'text': 'Meu blog.',
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

def post(request: HttpRequest, post_id: int):
    print('post', post_id)

    found_post:dict[str, Any] | None = None
    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
    
    if found_post is None:
        raise Http404('Post não existe.')
    
    context = {
        # 'text': 'Meu blog.',
        'post': found_post,
        'title': found_post['title'] + ' - ',
    }
    return render(request, 'blog/post.html', context)

