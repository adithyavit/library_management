from django.shortcuts import render
from .models import student
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
#https://medium.com/@himanshuxd/how-to-create-registration-login-webapp-with-django-2-0-fd33dc7a6c67
def login_view(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            context={
                'user_name'=u
            }

            if user is not None:
                return render(request, 'dummy.html',context)
            else:
                print("The account has been disabled!")
        else:
            print("The username and password were incorrect.")
    
    else:
       form = LoginForm()
       return render(request, 'login.html',{'form': form})
