from django.contrib import admin
from blog.models import Post,Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','update','status']
    prepopulated_fields={'slug':('title',)}
    list_filter=('author','publish','status','created')
    search_fields=('title','body')
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=('status','publish')

class CommentAdmin(admin.ModelAdmin):
    list_display=['name','email','post','body','created','update','active']
    list_filter=('created','update')
    serach_fields=('name','email','body')


admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
