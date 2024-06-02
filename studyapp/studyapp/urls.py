from django.contrib import admin
from django.urls import path, include


urlpatterns = [ # All the URLS of our website will be here like Home, about etc.
    path('admin/', admin.site.urls),
    path('', include('base.urls')) # whenver an empty string is matched, use the include function and send the user to base.urls
]
