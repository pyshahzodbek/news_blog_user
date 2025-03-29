from  django.urls import path
from .views import HomePageViews

urlpatterns=[
    path('',HomePageViews.as_view(),name='home'),
]