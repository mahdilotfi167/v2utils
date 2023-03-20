from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "V2utils"

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
]
