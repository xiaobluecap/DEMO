from django.contrib import admin
from myapp.models import Videos
# Register your models here.


class VideosAdmin(admin.ModelAdmin):
    pass


admin.site.register(Videos,VideosAdmin)