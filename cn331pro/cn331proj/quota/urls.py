from django.urls import path
from quota import views 

urlpatterns = [
    path('', views.index),
    path('subject_list',views.subject_list),
    path('my_quota',views.my_quota),
]