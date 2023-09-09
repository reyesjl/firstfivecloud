from django.urls import path

from . import views

urlpatterns = [
    # Root url
    path("", views.handleHomeRoute, name="home"),
    # Testing route for admin
    path("preview/", views.handlePreviewRoute, name="preview"),
    # About match
    path("about/", views.handleAboutRoute, name="about"),
    # Teams route
    path("teams/", views.handleTeamsRoute, name="teams"),
    # Team Page route
    path ("teams/<int:id>/details/", views.handleFetchTeamDetailsRoute, name="teamdetails"),
    # Team Fixture route
    path ("teams/<int:id>/fixtures/", views.handleFetchTeamFixturesRoute, name="teamfixtures"),
    # Success route
    path("success/", views.handleSuccessRoute, name="success"),
]
