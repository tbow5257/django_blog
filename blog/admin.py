# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp"]
    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)

