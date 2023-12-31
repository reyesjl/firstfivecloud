from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("f5.urls")),
    path("admin/", admin.site.urls),
    path("members/", include("members.urls")),
    path("clubs/", include("teams.urls")),
    path("store/", include("store.urls")),
]
