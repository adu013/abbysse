# answers/urls.py
from rest_framework.routers import SimpleRouter

from django.urls import include, path

from .apis import AnswerViewSet


router = SimpleRouter()
router.register(r'answers', AnswerViewSet, basename='answer')

urlpatterns = [
    path('api/', include(router.urls)),
]
