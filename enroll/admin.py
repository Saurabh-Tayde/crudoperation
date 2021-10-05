from django.contrib import admin

from enroll.models import Class


# from stockapp.models import stock
class student(admin.ModelAdmin):
    list_display=['Name','email','password']
admin.site.register(Class,student)

# Register your models here.

# Register your models here.
