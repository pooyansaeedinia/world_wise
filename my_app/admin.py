from django.contrib import admin

from my_app.models import Comments, Position

# Register your models here.

admin.site.register(Comments)
admin.site.register(Position)
