from django.urls import path
from quota import views 
from users import views as uv

urlpatterns = [
    path('', views.index),
    path('subject_list', views.subject_list),
    path('my_quota', views.my_quota, name='my_quota'),
    path('add_subject/<id>', views.add_subject),
    path('del_subject/<id>', views.del_subject),
]