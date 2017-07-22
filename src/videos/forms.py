from datetime import datetime

from dateutil.relativedelta import relativedelta
from django import forms
from django.utils.translation import ugettext_lazy as _


from .models import Comment, Theme, Thumb, Video


class CreateThemeForm(forms.ModelForm):
    '''
    Form used to create a theme
    '''
    class Meta:
        fields = '__all__'
        model = Theme


class CreateVideoForm(forms.ModelForm):
    '''
    Form used to create a video
    '''
    class Meta:
        fields = '__all__'
        model = Video

    def clean_date_uploaded(self):
        '''
        Validate field date_uploaded, the date can't be older than one year
        '''
        date = self.cleaned_data['date_uploaded']
        time = relativedelta(datetime.now(), date)

        # If years and days are equals 1 or more raise the exception
        if time.years and time.days:
            raise forms.ValidationError(
                _('Uploaded at can\'t be older than one year!')
            )

        return date


class CreateThumbForm(forms.ModelForm):
    '''
    Form used to create a thumb
    '''
    class Meta:
        exclude = ('video',)
        model = Thumb


class CreateCommentForm(forms.ModelForm):
    '''
    Form used to create a comment
    '''
    class Meta:
        exclude = ('video',)
        model = Comment
