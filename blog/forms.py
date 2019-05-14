from django import forms
from django.forms import TextInput
from .models import Post, thick

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        
class ThicknessForm(forms.ModelForm):
    class Meta:
        model = thick
        fields = ('angle', 'dhthick')
        labels = {
        "angle": "Angle of feature to core axis (0-90):",
        "dhthick":"Downhole thickness:"
       }
        widgets = {
            'angle': TextInput(attrs={'placeholder': ''}),
            'dhthick': TextInput(attrs={'placeholder': ''}),
        }