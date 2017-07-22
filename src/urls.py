from django.conf.urls import include, url
from django.contrib import admin

from .videos import urls as videos_urls


urlpatterns = [
    # Videos URLs
    url(r'^videos/', include(videos_urls, namespace='videos')),

    url(r'^admin/', admin.site.urls),
]
