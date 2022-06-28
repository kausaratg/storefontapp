# user_name = kaygee
# password = kassy
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .models import User, Message, Register
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
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
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return redirect('signup')
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'username taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username= username, password=password, email=email)
                user.save()
                user_model = User.objects.get(username=username)
                new_register = Register.objects.create(profile = user_model, f_name=f_name, l_name=l_name)
                new_register.save()
                messages.info(request, 'Profile Created.')
                return redirect('signup')
        else:
            messages.info(request, 'password does not match. Please try again')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        user =auth.authenticate(username = username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('signin')

    else:
        return render(request, 'signin.html')

def logout(request):
    auth.logout(request)
    return redirect('signin')

 