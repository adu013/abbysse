# questions/urls.py
from rest_framework.routers import SimpleRouter

from django.urls import include, path

from .apis import QuestionViewSet


router = SimpleRouter()
router.register(r'questions', QuestionViewSet, basename="question")

urlpatterns = [
    path('api/', include(router.urls)),
]
