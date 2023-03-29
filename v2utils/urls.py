from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "V2utils"
admin.site.site_title = "V2utils"
admin.site.index_title = "Management panel"

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('proxy/', include('proxy.urls'))
]
