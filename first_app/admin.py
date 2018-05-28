from django.contrib import admin
from first_app.models import books,subject,UserProfileInfo
# Register your models here.

admin.site.register(books)
admin.site.register(subject)

admin.site.register(UserProfileInfo)