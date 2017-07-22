from django.core.urlresolvers import reverse_lazy as r
from django.views.generic import CreateView

from .forms import CreateThemeForm


class CreateThemeView(CreateView):
    '''
    Creates a new theme
    '''
    form_class = CreateThemeForm
    success_url = r('videos:create_theme')
    template_name = 'videos/create_theme.html'
