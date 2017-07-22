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
