from django.shortcuts import render
from first_app.models import books,subject
from first_app import forms
from first_app.forms import bookdetails
# Create your views here.

def index(request):

    books_list=books.objects.order_by('name')
    my_dict = {'book':books_list}

    return render(request,'first_app/index.html',context=my_dict)


def bookform(request):
    form = bookdetails()

    if request.method == 'POST':
        form =bookdetails(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)



    return  render(request,'first_app/book.html',{'form':form})