from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('groceries/', include('groceries.urls')),
    path('admin/', admin.site.urls),
]
