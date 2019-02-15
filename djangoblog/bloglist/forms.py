from django import forms
from . import models

class CreateBlog(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ['title','slug','description','thumb']

class CreateComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update({'class': 'special'})
        # self.fields['upvote'].widget.attrs.update({'type':'button', 'class': 'special'})



