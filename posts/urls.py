from django.urls import path
from posts import views

app_name = "posts"

urlpatterns = [
    path("create", views.PostCreateView.as_view(), name="add-post"),
    path("show-posts", views.PostsListView.as_view(), name="show-posts"),
    path("like-post", views.PostLikeView.as_view(), name="like-post"),
    path("add-comment", views.PostCommentView.as_view(), name="add-comment"),

]
