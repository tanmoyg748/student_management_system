from django.contrib import admin
from django.urls import path, include, URLPattern, URLResolver

urlpatterns: list[URLPattern | URLResolver] = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
]