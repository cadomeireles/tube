from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^theme/create/$',
        views.CreateThemeView.as_view(),
        name='create_theme',
    ),
    url(
        r'^video/create/$',
        views.CreateVideoView.as_view(),
        name='create_video',
    ),
]
