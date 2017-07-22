from django import forms

from .models import Theme, Video


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
