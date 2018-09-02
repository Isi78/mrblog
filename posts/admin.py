from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ["__str__", "data"]
    list_filter = ["data"]
    search_fields = ["titolo", "contenuto"]
    prepopulated_fields =  {"slug" : ("titolo",)}

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

# Register your models here.
