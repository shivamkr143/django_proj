from django.conf.urls import url
from first_app import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^register/$',views.register,name='register'),
    url(r'^bookform/',views.bookform,name='bookform'),
    url(r'^logout/',views.user_logout,name='logout'),
    url(r'^login/',views.user_login,name='login'),
    url(r'^special/',views.special,name='special'),
    url(r'^homepage/',views.homepage,name='homepage'),


]