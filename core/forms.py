from django import forms
from django.contrib.auth.models import User

from core.models import Post
from core.widgets import TinyMceWidget


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'body', 'is_published')
        widgets = {
            'body': TinyMceWidget
        }


class FilterForm(forms.Form):
    NEWS_TYPE = 0
    STORY_TYPE = 1
    ART_TYPE = 2

    TYPE_CHOICES = (
        (NEWS_TYPE, 'News'),
        (STORY_TYPE, 'Story'),
        (ART_TYPE, 'Art')
    )
    price_from = forms.FloatField()
    price_to = forms.FloatField()

    text = forms.CharField(
        # widget=forms.widgets.Textarea
    )

    owners = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.widgets.SelectMultiple,
    )

    category = forms.ChoiceField(
        choices=TYPE_CHOICES,
        widget=forms.widgets.SelectMultiple
    )

    # def clean(self):
    #     if self.cleaned_data['price_from'] > \
    #        self.cleaned_data['price_to']:
    #         raise forms.ValidationError("Price from cant be greater then Price to")
    #     return self.cleaned_data

    def clean_price_from(self):
        if self.cleaned_data['price_from'] < 0:
            raise forms.ValidationError(
                "Price from should be positive.")
        return self.cleaned_data['price_from']

    def clean_price_to(self):
        if self.cleaned_data['price_to'] < 0:
            raise forms.ValidationError(
                "Price from should be positive.")
        return self.cleaned_data['price_to']
