from django.contrib import admin
from .models import Profile,Follow,Post,Comment,Like
admin.site.register([Profile,Follow,Post,Comment,Like])
