from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from datetime import datetime # from module datetime import datetime class
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    context = {
        #variables nhin bhhejenge hmm models mein se data queries fetch krke bhejenge
        "variable1":"Rhytech/Rhythm",
        "variable2":"I am Rhythm"

    }
    return render(request,'index.html',context)

@login_required(login_url='/login')
def about(request):
    # return HttpResponse("this is about page")
    return render(request,'about.html')

@login_required(login_url='/login')
def websites(request):
    return render(request,'websites.html')

@login_required(login_url='/login')
def articles(request):
    return render(request,'articles.html')

@login_required(login_url='/login')
def designing(request):
    return render(request,'designing.html')    

def contact(request):
    # return HttpResponse("this is contact page")
    if request.method == "POST":
        name = request.POST.get('name')#The argument in get function is the value of name attribute
        email=request.POST.get('email')
        desc = request.POST.get('desc')#request.POST is a dictionary and get is the method
        send_mail(
            'Subject - '+ name + '--' + email + ' has contacted you !', 
            'Hello ' + 'Rhytech' + ',\n' + '\n' + desc + '\n' + '\n' + 'My name is: ' + name + '\n' + '\n' + 'My email is: ' + email,
            settings.EMAIL_HOST_USER, 
            [
                'rhytech2020@gmail.com',
                'rhythmpangotra2017@gmail.com'
            ],
        fail_silently=False    
        ) 
        contactquery = Contact(name=name,email=email,desc=desc,date=datetime.today())
        contactquery.save()
        messages.success(request, 'Form is submitted successfully !')
    return render(request,'contact.html')

def loginuser(request):
    if request.method == "POST":
        #check if user has entered correct credentials
        username=request.POST.get('username')
        password=request.POST.get('password')
        valuenext= request.POST.get('next')
        print(valuenext)
        user = authenticate(request,username=username, password=password)
        if user is not None:
             # A backend authenticated the credentials
            login(request, user)
            # Redirect to a success page.
            messages.success(request, 'Welcome to Rhytech, User: ')
            if valuenext:
                return redirect(valuenext)
            else:
                return redirect('/')    
        else:
            # No backend authenticated the credentials the return to the same page
            messages.success(request, 'Wrong Credentials!')
            return render(request, 'login.html')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'You are now logged in as ')
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def logoutuser(request):
    logout(request)
    # Redirect to a success page.
    return redirect("/")