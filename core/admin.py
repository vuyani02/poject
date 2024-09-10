from django.contrib import admin
from .models import Beach
from .models import Comment


# Register the Beach model
admin.site.register(Beach)
admin.site.register(Comment)
