from datetime import datetime

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

    @property
    def score(self):
        '''
        Returns theme score, that consists of sum of videos' score
        '''
        return sum([video.score for video in self.videos.all()])


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

    def get_time_factor(self):
        '''
        Returns time factor rate
        '''
        days_since_upload = datetime.now().date() - self.date_uploaded
        return max(0, 1 - (days_since_upload.days / 365))

    def get_good_comments(self):
        '''
        Returns good comments rate
        '''
        positive_comments = self.comments_set.filter(is_positive=True).count()
        negative_comments = self.comments_set.filter(is_positive=False).count()

        if not positive_comments:
            return 0

        return positive_comments / (positive_comments + negative_comments)

    def get_thumbs_up(self):
        '''
        Returns thumbs up rate
        '''
        thumbs_up = self.thumbs_set.filter(is_positive=True).count()
        thumbs_down = self.thumbs_set.filter(is_positive=False).count()

        if not thumbs_up:
            return 0

        return thumbs_up / (thumbs_up + thumbs_down)

    def get_positivity_factor(self):
        '''
        Returns positivity factor rate
        '''
        good_comments = self.get_good_comments()
        thumbs_up = self.get_thumbs_up()

        return 0.7 * good_comments + 0.3 * thumbs_up

    @property
    def score(self):
        '''
        Returns video score
        '''
        time_factor = self.get_time_factor()
        positivity_factor = self.get_positivity_factor()

        return self.views * time_factor * positivity_factor


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
