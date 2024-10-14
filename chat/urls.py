from django.urls import path
from .views import ChatsView


urlpatterns = [
    path("", ChatsView.as_view()),
]