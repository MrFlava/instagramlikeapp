from django.contrib import admin
from stories.models import Story, WatchedStory

# Register your models here.


class StoryAdmin(admin.ModelAdmin):
    model = Story


class WatchedStoryAdmin(admin.ModelAdmin):
    model = WatchedStory


admin.site.register(Story, StoryAdmin)
admin.site.register(WatchedStory, WatchedStoryAdmin)
