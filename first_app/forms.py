from django import forms
from first_app.models import books,UserProfileInfo
from django.contrib.auth.models import User

class bookdetails(forms.ModelForm):
    class Meta():
        model = books
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model =User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('fblink','profile_pic')
