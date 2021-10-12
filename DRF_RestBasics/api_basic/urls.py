from django.contrib import admin
from django.db import router
from django.urls import path
from django.urls.conf import include
from .views import ArticleDetails, ArticleViewSet, article_detail, article_list, ArticleAPIView, ArticleDetails, GenericAPIView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    # # FUNCTION BASED API VIEW
    # path('article/', article_list),
    # path('detail/<int:pk>/', article_detail),

    # # CLASS BASED API VIEW
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view()),

    # # Generic BASED API VIEW
    path('generic/article/<int:id>/', GenericAPIView.as_view()),

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]