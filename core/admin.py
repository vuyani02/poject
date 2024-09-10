from django.contrib import admin
from .models import Beach
from .models import Comment
from .models import Map
from .models import Source
from .models import Report
from .models import CommentSection





# Register the Beach model
admin.site.register(Beach)
admin.site.register(Comment)
admin.site.register(Map)
admin.site.register(Source)
admin.site.register(Report)
admin.site.register(CommentSection)