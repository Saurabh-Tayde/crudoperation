from django import forms
from django.core import validators
from enroll.models import Class
class stu(forms.ModelForm):
    class Meta:
        model= Class
        fields="__all__"
        widgets={
     'Name':forms.TextInput(attrs={'class':'form-control'}),
     'email':forms.EmailInput(attrs={'class':'form-control'}),
     'password':forms.PasswordInput(attrs={'class':'form-control'}),
}
