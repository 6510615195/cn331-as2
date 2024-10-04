from django.urls import path
from users import views

urlpatterns = [
    path('login/', views.login),
    # path("logout", views.logout_view, name="logout"),
]