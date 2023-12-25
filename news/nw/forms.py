from .models import CommentModel
from django import forms

class AddCommentFormUsername(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('content',)

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
        
class AddCommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('username' ,'content')
        
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }
        