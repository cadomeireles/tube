from django.core.urlresolvers import reverse_lazy as r
from django.views.generic import CreateView

from .forms import (
    CreateCommentForm,
    CreateThemeForm,
    CreateThumbForm,
    CreateVideoForm,
)
from .models import Video


class CreateThemeView(CreateView):
    '''
    Creates a new theme
    '''
    form_class = CreateThemeForm
    success_url = r('videos:create_theme')
    template_name = 'videos/create_theme.html'


class CreateVideoView(CreateView):
    '''
    Creates a new video
    '''
    form_class = CreateVideoForm
    success_url = r('videos:create_video')
    template_name = 'videos/create_video.html'


class CreateMetricView(CreateView):
    '''
    Create a view to save a videos.Metric child object
    '''
    raw_success_url = None

    def get_raw_success_url(self):
        '''
        Return the raw success url
        '''
        return self.raw_success_url

    def get_video(self):
        '''
        Get video according PK sent
        '''
        return Video.objects.get(pk=self.kwargs['video_pk'])

    def get_context_data(self, **kwargs):
        '''
        Add video object to context
        '''
        context = super().get_context_data(**kwargs)
        context.update({
            'video': self.get_video()
        })

        return context

    def form_valid(self, form):
        '''
        Perform creation
        '''
        metric = form.save(commit=False)
        metric.video = self.get_video()
        metric.save()

        return super().form_valid(form)

    def get_success_url(self):
        '''
        Return to same thump page
        '''
        video = self.get_video()
        return r(self.get_raw_success_url(), kwargs={'video_pk': video.pk})


class CreateThumbView(CreateMetricView):
    '''
    Makes a thumb on a video
    '''
    form_class = CreateThumbForm
    raw_success_url = 'videos:create_thumb'
    template_name = 'videos/create_thumb.html'


class CreateCommentView(CreateMetricView):
    '''
    Makes a thumb on a video
    '''
    form_class = CreateCommentForm
    raw_success_url = 'videos:create_comment'
    template_name = 'videos/create_comment.html'
