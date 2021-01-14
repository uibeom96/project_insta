from django import forms
from dista.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("image", "hash_tag")

    def clean_hash_tag(self):
        check = self.cleaned_data.get("hash_tag")
        check = check.replace(" ", " #")
        return "#"+check