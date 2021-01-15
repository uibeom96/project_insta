from django import forms
from dista.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("image", "hash_tag")

    def clean_hash_tag(self):
        check = self.cleaned_data.get("hash_tag")
        check1 = ""
        for i in check:
            if i == "#":
                del(i)
            else:
                check1 += i
        print(check1)
        
        check = check1.replace(" ", " #")
        return "#"+check

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment", )