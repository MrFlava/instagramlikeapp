import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (CreateAPIView, ListAPIView)

from stories.serializers import StorySerializer
from stories.models import Story, WatchedStory


class StoryCreateView(CreateAPIView):

    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)


class StoryListView(ListAPIView):

    queryset = Story.objects.filter(date__range=[datetime.datetime.now() - datetime.timedelta(days=1),
                                    datetime.datetime.now()], watchedstories__isnull=True).all()
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticated]


class WatchStoryView(CreateAPIView):

    queryset = WatchedStory.objects.all()
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

