
from django import forms

from blogs.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rate", "review"]
