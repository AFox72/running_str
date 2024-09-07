from django.urls import path
from video.apps import VideoConfig

from video.views import index, VideoListView, download_file

app_name= VideoConfig.name


urlpatterns = [
    path('', index, name="index"),
    path('download/<int:pk>/', download_file, name='download_file'),
    path('videos/', VideoListView.as_view(), name='videos'),
]