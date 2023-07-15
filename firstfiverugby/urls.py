from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include("f5.urls")),
    path('f5/', include("f5.urls")),
    path('admin/', admin.site.urls),
    path('members/', include("django.contrib.auth.urls")),
    path('members/', include("members.urls")),
    path('catalog/', include("catalog.urls")),
]
