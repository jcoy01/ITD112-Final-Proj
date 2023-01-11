from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('project2', views.project2, name='project2'),
    path('project3', views.project3, name='project3')

]
