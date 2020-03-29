from django.urls import path

from .views import login
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',login)
    # path('', auth_views.login, name='login')
]