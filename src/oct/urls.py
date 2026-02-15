from django.urls import path

from oct.views import oct_info

urlpatterns = [
    path("info/", oct_info),
]
