from django.db import router
from django.urls import path
from django.conf.urls import include
from .views import SocialMediaServiceEvaluation, ProfessionalProfileServiceEvaluation
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path("",include(router.urls)),
    path("evaluateSocialMediaService/", SocialMediaServiceEvaluation),
    path("professionalProfileService/", ProfessionalProfileServiceEvaluation),

]