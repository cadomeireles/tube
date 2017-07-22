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
