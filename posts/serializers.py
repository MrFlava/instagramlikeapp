from rest_framework import serializers

from posts.models import Post, Like, Comment


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    # like = serializers.StringRelatedField(read_only=True)
    # user = serializers.IntegerField(required=False)

    class Meta:
        model = Like
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    # comment = serializers.StringRelatedField(read_only=True)
    # user = serializers.IntegerField(required=False)

    class Meta:
        model = Comment
        fields = '__all__'
