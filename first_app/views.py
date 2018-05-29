from django.shortcuts import render
from first_app.models import books,subject,UserProfileInfo,User
from first_app import forms
from first_app.forms import bookdetails,UserForm,UserProfileInfoForm
from django.http import HttpResponse,HttpResponseRedirect
from  django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):

    books_list=books.objects.order_by('name')
    my_dict = {'book':books_list}

    return render(request,'first_app/index.html',context=my_dict)

def homepage(request):
    return render(request,'first_app/homepage.html',{})


def bookform(request):
    form = bookdetails()

    if request.method == 'POST':
        form =bookdetails(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)



    return  render(request,'first_app/book.html',{'form':form})


def register(request):
    registered = False
    if request.method=="POST":
        user_form = UserForm(data=request.POST)
        profile_form =UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user =user
            if 'profile_pic' in request.FILES :
                profile.profile_pic =request.FILES['profile_pic']

            profile.save()
            registered =True
        else :
            print("errors")
            print(user_form.errors,profile_form.errors)

    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    return render(request,'first_app/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered })

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return  HttpResponse("this urls open only when u r logged in")





def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('special'))
            else:
                return HttpResponse("User Not Active")
        else:
            print("login failed")
            print(username,password)
            return  HttpResponse("Invalid login details")
    else:
        return render(request,'first_app/login.html',{})

