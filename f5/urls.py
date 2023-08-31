from django.urls import path

from . import views

urlpatterns = [
    # Root url
    path("", views.handleHomeRoute, name="home"),
    # Testing route for admin
    path("preview/<int:param>/", views.handlePreviewRoute, name="preview"),
    # About match
    path("about/", views.handleAboutRoute, name="about"),
    # Success route
    path("success/", views.handleSuccessRoute, name="success"),
]
