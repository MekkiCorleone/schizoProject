from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import NewUserForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


# Create your views here.

def ActivateEmail(request, user, to_email):
     mail_subject = "Activate your user account"
     message = render_to_string("template_activate_account.html",{ 
                'user': user.username,
                'domain': get_current_site(request).domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                'protocol': 'https' if request.is_secure() else 'http'})
     email = EmailMessage(mail_subject, message, to=[to_email])
     if email.send():
          messages.success(request, f'Dear {user} , please go to your email {to_email} inbox and click on received activation link to confirm and complete the registration. Note: check your spam folder.')
     else:
          messages.error(request, f'Problem sending email link to {to_email}, check if you typed it correctly')

def activate(request, uidb64, token):
     User = get_user_model()
     try:
          uid = force_str(urlsafe_base64_decode(uidb64))
          user = User.objects.get(pk=uid)
     except:
          user = None
     
     if user is not None and account_activation_token.check_token(user, token):
          user.is_active = True
          user.save()

          messages.success(request, "Thank you for your email verification, you can login your account now")
          return redirect('login_signup')
     else:
          messages.error(request, "Activation link is invalid!")
     return redirect('home')

def home(request):
    return render(request, "pages/home.html")

def about(request):
        
        return render(request, "pages/about.html")

def contact(request):
        
        return render(request, "pages/contact.html")

def login_signup(request):
    if request.method == 'POST':
        if 'signup' in request.POST:
        # do something with the user object
            first_name=request.POST.get('fname')
            last_name=request.POST.get('lname')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password  = request.POST.get('password')
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            
            user.is_active=False
            user.save()
            ActivateEmail(request, user, email)
            
            messages.success(request, 'Your account has been created successfully and an activation email has been sent to your email address.')
            return redirect("login_signup")
        elif 'signin' in request.POST:
            username = request.POST.get('Username')
            password = request.POST.get('Password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.success(request,"There was an error Invalid username or password")
                return redirect('login_signup')
        else:
            messages.success(request,"There was an error please try again")
            pass
    else:     
        return render(request, 'pages/login.html')


'''def sign_up(request):
    if request.method == "POST":    
            form = NewUserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active=False
                user.save()
                ActivateEmail(request, user, form.cleaned_data.get('email'))
                return redirect("home")
            else:
                 messages.error(request, "Unsuccessful registration. Invalid information.")
            
    form = NewUserForm()
    return render (request, "pages/signup.html", {"form":form})
def login_user(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password  = request.POST.get('password')
            user = authenticate(request,username=username, password=password)
            if user is not None:
              login(request, user)
              return redirect('home')
            else:
                messages.success(request,"There was an error in username or in password")
                return redirect('login_user')
            
          
    return render(request, 'pages/signup.html', {'lf':LoginForm})
'''
def logout_user(request):
     logout(request)
     messages.success(request,"You were logged out")
     return redirect('home')


