from django.contrib import admin

from vote.models import Choice, Reply, Topic

# Register your models here.
admin.site.register(Topic)
admin.site.register(Choice)
admin.site.register(Reply)