from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^theme/create/$',
        views.CreateThemeView.as_view(),
        name='create_theme',
    ),
]
