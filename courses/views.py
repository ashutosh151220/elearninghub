from django.shortcuts import render
from .models import Course, Videos
from django.shortcuts import get_object_or_404, render

# Create your views here.
def courses(request):
    courses_list = Course.objects.all()
    return render(request,"courses.html", {"courses_list" : courses_list})

def course_videos(request, course_id):
    videos_list = Videos.objects.filter(course__id=course_id)
    return render(request, "videos.html", {"videos_list": videos_list})

def player(request, course_id,video_id):

    video=Videos.objects.filter(id=video_id)
    video= get_object_or_404(Videos, pk=video_id)

    return render(request, 'video_play.html', {'question': video})