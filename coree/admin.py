from django.contrib import admin

from django.contrib import admin
from .models import Beach
from .models import CommentSection
from .models import Comment
from .models import Report
from .models import Source
from .models import GeneralCommentSection

# Register your models here.
admin.site.register(Beach)
admin.site.register(Comment)
admin.site.register(CommentSection)
admin.site.register(Report)
admin.site.register(Source)
admin.site.register(GeneralCommentSection)
