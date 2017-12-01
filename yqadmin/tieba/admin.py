from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from tieba import models


@admin.register(models.Tieba)
class TiebaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'men_mun', 'topic_mun', 'url']
    search_fields = ('name',)
    list_per_page = 20
    list_display_links = ['name']


@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'post_date', 'url']
    search_fields = ('title',)
    list_per_page = 20
    list_display_links = ['id']
