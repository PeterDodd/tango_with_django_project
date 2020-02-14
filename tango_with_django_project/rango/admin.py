from django.contrib import admin
from rango.models import Category, Page, Question, Choice


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date information', {'fields': ['pub_date']})]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
