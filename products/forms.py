from django import forms 
from .models import ProductReview



class PorductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields=['rate','review']
