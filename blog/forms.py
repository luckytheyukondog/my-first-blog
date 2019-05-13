from django import forms

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
        "angle": "Angle of feature to core axis",
        "dhthick":"Downhole thickness"
       }