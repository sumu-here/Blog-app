from django.contrib import admin
from .models import Post,Answers

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=('title','author')
    search_fields=('title','detail')
    
admin.site.register(Post,PostAdmin)
admin.site.register(Answers)
