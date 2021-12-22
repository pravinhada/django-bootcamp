from django.urls import path, include
from rest_framework import routers
from profiles_api.views import HelloApiView, HelloViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='hello-viewset')


urlpatterns = [
    path('hello/', HelloApiView.as_view(), name='hellow_view'),
    path('', include(router.urls)),
]
