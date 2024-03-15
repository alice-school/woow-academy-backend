import debug_toolbar
from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('industry/', include('apps.industry.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
