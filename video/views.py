from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from utils.utils import create_video_opencv
from video.models import Video


def index(request):
    message = str(request.GET.get('message', ''))
    result = create_video_opencv(message)
    new_video = Video(title=result['title'], message=message, video=result['path'])
    new_video.save()
    context = {'object': new_video}
    return render(request, 'video/index.html', context)


def download_file(request, pk):
    video = Video.objects.get(pk=pk)
    response = HttpResponse(video.video, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{video.video.name}"'
    return response


class VideoListView(ListView):
    model = Video

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        print(queryset)
        return queryset