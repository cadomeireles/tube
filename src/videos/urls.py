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
    url(
        r'^thumb/create/(?P<video_pk>\d+)/$',
        views.CreateThumbView.as_view(),
        name='create_thumb',
    ),
    url(
        r'^comment/create/(?P<video_pk>\d+)/$',
        views.CreateCommentView.as_view(),
        name='create_comment',
    ),
]
