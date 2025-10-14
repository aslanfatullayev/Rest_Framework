from django.urls import path

from .views import studentsListApi

urlpatterns = [
    path('', studentsListApi.as_view(),)
]

