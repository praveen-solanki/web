from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path("about",views.about,name='about'),
    path("contact",views.Contact,name='contact'),
    path("Education",views.Education,name='Education'),
    path("Certifications",views.Certifications,name='Certifications'),
    path("Achievement",views.Achievement,name='Achievement'),
    path("Wip",views.Wip,name='Wip'),
    path("Resume",views.Resume,name='Resume'),
    path("interests",views.interests,name='interests'),
    path("Travelings",views.Travelings,name='Travelings'),

]
