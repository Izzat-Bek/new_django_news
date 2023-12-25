from django.contrib import admin
from .models import PostModel, CategoryModel, CommentModel

class Postadmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    list_filter = ('category',)
    search_fields = ('title', 'category')
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)
    list_filter = ('name',)
    

class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'post', 'created_at')
    list_filter = ('username', 'post')
    search_fields = ('username', 'post')


admin.site.register(PostModel, Postadmin)
admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(CommentModel, CommentAdmin)
