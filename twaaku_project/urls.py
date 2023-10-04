from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('twaaku_app.urls')),
]


# config Admin Page
admin.site.site_header = "TWAAKU TRADERS PANEL"
admin.site.site_title = "TWAAKU TRADERS WEBSITE"
admin.site.index_title = "Administration Area" 