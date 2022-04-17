from multiprocessing.spawn import import_main_path
from django.urls import path, include
from .views import AnswerListAPIView, QuestionViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"questions", QuestionViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path('answers/', AnswerListAPIView.as_view()),
]