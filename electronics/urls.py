from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve 
from .admin import admin_site

urlpatterns = [
    path('', views.home , name='home'),
    path('profile/', views.profile , name='profile'),
    path('video_lectures/', views.video_lectures , name='video_lectures'),
    path('laboratory_videos/', views.laboratory_videos , name='laboratory_videos'),
    path('classnotes/', views.Class_notes , name='class_notes'),
    url(r'classnotes/^view-pdf/$', views.pdf_view, name='pdf_view'),
    #path('elctronics/', admin.site.urls , name='elc-admin'),

]
