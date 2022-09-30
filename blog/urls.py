from django.contrib import admin
#include importado para usar nas urls
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
        path('', include('posts.urls')),
        path("admin/", admin.site.urls),
        path('summernote/', include('django_summernote.urls')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
        import debug_toolbar
        urlpatterns = [
            path('__debug__', include(debug_toolbar.urls)),
        ] + urlpatterns
        
        # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)