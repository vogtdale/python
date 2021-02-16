from django.contrib import admin
from django.urls import path

from djongproject.posts.views import post_list_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', post_list_views),
]
