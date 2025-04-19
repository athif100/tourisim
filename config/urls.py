
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from.sitemap import mysitemap
allsitemaps={"sitemaps":mysitemap}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Include your app URLs
    path('Sitemap.xml',sitemap,allsitemaps,name='django.contrib.sitemaps.views.sitemap'),
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
                            
from django.contrib import admin
from django.urls import path
