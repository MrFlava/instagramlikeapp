from django.urls import path
from stories import views

app_name = "stories"

urlpatterns = [
    path("create", views.StoryCreateView.as_view(), name="add-story"),
    path("show-stories", views.StoryListView.as_view(), name="show-stories"),
    path("watch-story", views.StoryListView.as_view(), name="watch-story"),
]
