# user_name = kaygee
# password = kassy
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .models import User, Message
from django.contrib.auth.models import auth


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    messager = Message()
    if request.method == 'POST':
        email = request.POST['email']
        message = request.POST['message']
        messager.email = email
        messager.message = message
        messager.save()
        messages.info(request, 'message successfully sent.')
        return redirect('contact')

    else:
        return render(request, 'contacts.html')


def signup(request):
    # if request.method == 'POST':
    #     f_name = request.POST['f_name']
    #     l_name = request.POST['l_name']
    #     email = request.POST['email']
    #     username = request.POST['username']
    #     password = request.POST['password1']
    #     password2 = request.POST['password2']
    #     if password == password2:
    #         if User.objects.filter(email = email).exists():
    #             messages.info(request, 'email already exist')
    #             return redirect('signup')
    #         elif User.objects.filter(username=username).exists():
    #             messages.info(request, 'username already exist')
    #             return redirect('signup')
    #         elif User.objects.filter(password = password).exists():
    #             messages.info(request, 'password taken')
    #             return redirect('signup')
    #         else:
    #             user = User.objects.create(f_name=f_name, l_name=l_name, email=email,  username=username, password=password)
    #             user.save()
    #             messages.info(request, 'signup successful')
        #         return redirect('signup')
        # else:
        #     messages.info(request, 'password does not match')
        #     return redirect('signup')
    # else:
    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('signin')
    else:
        return render(request, 'signin.html')

 