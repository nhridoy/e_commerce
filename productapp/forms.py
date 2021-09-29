from django import forms
from productapp.models import Rating


class RatingForm(forms.ModelForm):
    product_rating = forms.ChoiceField(choices=Rating.rating, widget=forms.RadioSelect(attrs={}))
    product_comment = forms.Field(label='Comment',
                                  widget=forms.Textarea(attrs={'class': 'border-2 resize-none p-4', 'rows': '5'}))

    class Meta:
        model = Rating
        fields = '__all__'
