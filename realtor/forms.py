from django import forms
from django.forms import ModelForm
from .models import Property

class PropertyForm(forms.Form):
    Name = forms.CharField(max_length=40)
    Email = forms.EmailField()
    Message = forms.CharField(widget=forms.Textarea)

class AddProperty(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'

