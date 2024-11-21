from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("recipe_proposer/", include("MainRP.urls")),
    path("admin/", admin.site.urls),
]
