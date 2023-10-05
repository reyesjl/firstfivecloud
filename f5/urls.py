from django.urls import path

from . import views

urlpatterns = [
    path("", views.handlePreviewRoute, name="preview"),
    # Teams page route
    path("teams/", views.handleTeamsRoute, name="teams"),
    # Team Detail route
    path("teams/<int:id>/details/", views.handleFetchTeamDetailsRoute, name="teamdetails"),
    # Team Fixture route
    path("teams/<int:id>/fixtures/", views.handleFetchTeamFixturesRoute, name="teamfixtures"),
    # Players Page route
    path("players/", views.handlePlayersRoute, name="players"),
    # Schedules Page route
    path("schedules/", views.handleSchedulesRoute, name="schedules"),
    # Store Page route
    path("store/", views.handleStoreRoute, name="store"),
    # Product detail page
    path("store/<int:id>/details", views.handleFetchProductDetailsRoute, name="productdetails"),
    # Coaches Page route
    path("coaches/", views.handleCoachesRoute, name="coaches"),
    # Camps page route
    path("camps/", views.handleCampsRoute, name="camps"),
    # Camp details route
    path("campdetails/", views.handleCampDetailsRoute, name="campdetails"),
    # Tours Page Route
    path("tours/", views.handleToursRoute, name="tours"),
    # Partners Page Roue
    path("partners/", views.handlePartnersRoute, name="partners"),
]
