from django.contrib import admin
from myapp.models import User
from myapp.forms import UserForm

# Register your models here.
admin.site.register(User)
