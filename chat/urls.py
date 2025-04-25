from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path("", views.chat_view, name="index"),
    path("reset/", views.reset_chat, name="reset"),   # ← NEW
]
