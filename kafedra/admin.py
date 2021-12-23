# -*- coding:utf-8 -*-
from django.contrib import admin
from kafedra.models import *


class ContentAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('page', 'title')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)


class CollectiveAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id','name','position')


class ConferenceAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('name', 'desc')


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('names', 'work_name')


admin.site.register(Content, ContentAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Collective, CollectiveAdmin)
admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Publication, PublicationAdmin)
