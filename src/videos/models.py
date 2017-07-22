from django.db import models
from django.utils.translation import ugettext_lazy as _


class Theme(models.Model):
    '''
    Representation of a theme
    '''
    name = models.CharField(
        _('name'),
        max_length=80,
    )

    class Meta:
        ordering = ['name']
        verbose_name = _('theme')
        verbose_name_plural = _('themes')

    def __str__(self):
        return self.name


class Video(models.Model):
    '''
    Representation of a video
    '''
    title = models.CharField(
        _('title'),
        max_length=160,
    )
    url = models.URLField(
        _('video URL'),
    )
    date_uploaded = models.DateField(
        _('uploaded at'),
    )
    views = models.PositiveIntegerField(
        _('views quantity'),
    )
    themes = models.ManyToManyField(
        Theme,
        related_name='videos',
        verbose_name=_('themes'),
    )

    class Meta:
        ordering = ['title']
        verbose_name = _('video')
        verbose_name_plural = _('videos')

    def __str__(self):
        return self.title


class Metric(models.Model):
    '''
    Base class for video evaluation metrics
    '''
    is_positive = models.BooleanField(
        _('is positive'),
    )
    time = models.DateTimeField(
        _('time'),
        auto_now_add=True,
    )
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        related_name='%(class)ss_set',
        related_query_name='%(class)ss',
        verbose_name=_('video'),
    )

    class Meta:
        abstract = True


class Thumb(Metric):
    '''
    Representation of a thumb
    '''
    class Meta:
        ordering = ['-time']
        verbose_name = _('thumb')
        verbose_name_plural = _('thumbs')

    def __str__(self):
        data = {'title': self.video.title, 'time': self.time}

        if self.is_positive:
            return _('Like on %(title)s at %(time)s') % data
        else:
            return _('Dislike on %(title)s at %(time)s') % data


class Comment(Metric):
    '''
    Representation of a comment
    '''
    message = models.TextField(
        _('message'),
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['-time']
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

    def __str__(self):
        data = {'title': self.video.title, 'time': self.time}

        return _('Comment on %(title)s at %(time)s') % data
