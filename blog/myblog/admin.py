from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}
    pass

admin.site.register(Post, PostAdmin)
# Register your models here.
