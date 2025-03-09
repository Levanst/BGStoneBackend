from django.db import router
from django.urls import path
from django.conf.urls import include
from .views import BasicServiceEvaluation
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path("",include(router.urls)),
    path("evaluateBasicServices/", BasicServiceEvaluation),

]