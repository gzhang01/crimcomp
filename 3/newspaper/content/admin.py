from django.contrib import admin
from content.models import Article, Image, Contributor

class ImageInline(admin.TabularInline):
	model = Image
	# fk_name = 'article'
	extra = 1


class ArticleAdmin(admin.ModelAdmin):
	fieldsets = [
		('Title',               {'fields': ['title', 'subtitle']}),
		('Date Information',    {'fields': ['pub_date'], 'classes': ['collapse']}),
		('Text', 				{'fields': ['text']}),
		('Contributors',		{'fields': ['contributors']}),
	]
	inlines = [ImageInline]
	list_display = ('title', 'pub_date')
	list_filter = ['pub_date']
	search_fields = ['title']
	date_hierarchy = 'pub_date'

admin.site.register(Article, ArticleAdmin)
admin.site.register(Contributor)

