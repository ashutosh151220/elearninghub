from django.urls import path
from .views import courses, course_videos, player

urlpatterns = [
    path('',courses),
    path('<int:course_id>', course_videos),
    path('<int:course_id>/<int:video_id>', player)
]