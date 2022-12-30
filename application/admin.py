from django.contrib import admin
from .models import Poll, Vote, Choice, Comment


# Register your models here.

class PollAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Poll, PollAdmin)
admin.site.register(Vote)
admin.site.register(Choice)
admin.site.register(Comment)
