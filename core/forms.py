from django import forms

from core.models import Post


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'body', 'is_published')
