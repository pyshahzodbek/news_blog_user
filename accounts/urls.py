from tkinter.font import names

from django.urls import path
from .views import SignUpView, LogoutPageView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutPageView.as_view(), name='logout')
]
