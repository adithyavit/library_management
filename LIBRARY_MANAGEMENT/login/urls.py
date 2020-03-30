from django.urls import path
from .views import login_view
# from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',login_view)
    # path('', auth_views.login, name='login')
]


##from django.conf.urls import url
## from .import views

##app_name ='accounts'
##urlpatterns = [

    ##url(r'^login/$',views.login_view,name="login"),


##]