from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from chat.views import IntentViewSet

router = DefaultRouter()
router.register('api/intent', IntentViewSet, basename='intent')

urlpatterns = []
urlpatterns += router.urls