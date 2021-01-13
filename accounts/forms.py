from django import forms
from users.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(label="패스워드", widget=forms.PasswordInput)
    password2 = forms.CharField(label="패스워드 확인", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ("nick_name", "username", "password", "password2", "email")
        
        labels = {
            "nick_name": "닉네임",
            "username": "아이디",
            }
    
    
    def clean_password2(self):
        check = self.cleaned_data
        if check.get("password") != check.get("password2"):
            raise forms.ValidationError("패스워드를 확인해주세요")
        return check.get("password2")