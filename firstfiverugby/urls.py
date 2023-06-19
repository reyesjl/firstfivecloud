from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include("f5.urls")),
    path('f5/', include("f5.urls")),
    path('admin/', admin.site.urls),
]