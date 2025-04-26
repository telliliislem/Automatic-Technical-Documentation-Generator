from django.contrib import admin
from django.urls import path
from api.views import comment_code  
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/comment/', comment_code),  
]

# Sert les fichiers MEDIA pendant le DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)