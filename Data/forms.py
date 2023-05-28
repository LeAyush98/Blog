from django import forms
from .models import BlogPost
from ckeditor.widgets import CKEditorWidget

class BlogPostForm(forms.ModelForm):
    body = forms.CharField(widget = CKEditorWidget())
    class Meta:
        model = BlogPost
        fields = "__all__"