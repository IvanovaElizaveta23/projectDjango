from django.contrib import admin
from .models import *


class DifficultionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]
    list_display_links = [
        'id',
        'name',
    ]
    search_fields = [
        'id',
        'name',
    ]
    list_filter = [
        'name',
    ]


admin.site.register(Difficultion, DifficultionAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]
    list_display_links = [
        'id',
        'name',
    ]
    search_fields = [
        'id',
        'name',
    ]
    list_filter = [
        'name',
    ]


admin.site.register(Category, CategoryAdmin)


class TestAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'cat',
        'dif',
        'time_limit',
        'quantity_attempts'
    ]
    list_display_links = [
        'id',
        'name',
    ]
    search_fields = [
        'id',
        'name',
    ]
    list_filter = [
        'name',
    ]
    autocomplete_fields = [
        'cat',
        'dif',
    ]


admin.site.register(Test, TestAdmin)


class AnswerInline(admin.TabularInline):
    model = Answer


admin.site.register(Answer)


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

    list_display = [
        'id',
        'content',
        'test',
    ]
    list_display_links = [
        'id',
        'content',
    ]
    search_fields = [
        'id',
        'content',
    ]
    list_filter = [
        'content',
    ]


admin.site.register(Question, QuestionAdmin)


class SessionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'test',
        'time_start',
        'time',
        'result'
    ]
    list_display_links = [
        'id',
    ]
    search_fields = [
        'id',
    ]
    list_filter = [
        'test',
    ]


admin.site.register(Session, SessionAdmin)


class AnswerUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(AnswerUser, AnswerUserAdmin)
