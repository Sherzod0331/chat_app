from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Group)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Message)
admin.site.register(role)
admin.site.register(login_required)