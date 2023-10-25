from . import views
from django.urls import path

urlpatterns = [
    path("", views.handleHomeRoute, name="home"),
    path("about/", views.handleAboutRoute, name="about"),
    # Research page route
    path("research/", views.handleResearchRoute, name="research"),
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
    # Camp details by id
    path("camps/<int:id>", views.handleCampDetailsRoute, name="campdetails"),
    # Success page
    path("camps/<int:id>/success", views.handleCampSuccessRoute, name="campsuccess"),
    # Tours Page Route
    path("tours/", views.handleToursRoute, name="tours"),
    # Partners Page Roue
    path("partners/", views.handlePartnersRoute, name="partners"),
    
]
