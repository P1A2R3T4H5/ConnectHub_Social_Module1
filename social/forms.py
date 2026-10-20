from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Post,Comment
class SignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta: model=User; fields=("username","email","password1","password2")
    def save(self,commit=True):
        u=super().save(commit=False); u.email=self.cleaned_data["email"]
        if commit: u.save(); Profile.objects.get_or_create(user=u)
        return u
class ProfileForm(forms.ModelForm):
    class Meta: model=Profile; fields=("bio","avatar","website"); widgets={"bio":forms.Textarea(attrs={"rows":3})}
class PostForm(forms.ModelForm):
    class Meta: model=Post; fields=("image","caption"); widgets={"caption":forms.Textarea(attrs={"rows":3,"placeholder":"Write a caption..."})}
class CommentForm(forms.ModelForm):
    class Meta: model=Comment; fields=("text",); widgets={"text":forms.TextInput(attrs={"placeholder":"Add a comment..."})}
