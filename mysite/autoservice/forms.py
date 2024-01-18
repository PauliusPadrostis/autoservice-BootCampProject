from .models import Comment
from django import forms


class OrderReviewForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'order', 'commenter',)
        widgets = {'order': forms.HiddenInput(), 'commenter': forms.HiddenInput()}