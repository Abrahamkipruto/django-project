from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('hosi.urls')),
    path('admin/', admin.site.urls),
    path('account/',include("django.contrib.auth.urls")),


]