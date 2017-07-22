from django import forms

from .models import Theme


class CreateThemeForm(forms.ModelForm):
    '''
    Form used to create a theme
    '''
    class Meta:
        fields = '__all__'
        model = Theme
