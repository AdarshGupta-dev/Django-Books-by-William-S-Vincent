from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="Home Page"),
    path("about/", views.AboutPageView.as_view(), name="About Page")
]
