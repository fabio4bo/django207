from django.urls import path

from . import views

app_name = 'blog'

#url mais específica primeiro
urlpatterns = [
    path("<int:post_id>/", views.post, name='post'), # <> url dinâmica
    path("", views.blog, name='home'), #somente porque tem namespace
]
