from django import forms
from .models import Post, Profile, Comment, Subscriber
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ('title', 'content', 'image', 'category', 'tags')

        widgets = {}

        labels = {'title': "Заголовок"}


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Напишіть свій коментар...'
            })
        }

        labels = {
            'text': 'Ваш коментар'
        }

    def clean_text(self):
        text = self.cleaned_data['text'].strip()

        if len(text) < 5:
            raise forms.ValidationError(
                'Коментар повинен містити щонайменше 5 символів.'
            )

        if len(text) > 500:
            raise forms.ValidationError(
                'Коментар не може перевищувати 500 символів.'
            )

        return text


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email',)

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть вашу електронну адресу'
            })
        }

        labels = {
            'email': 'Електронна адреса'
        }

        error_messages = {
            'email': {
                'unique': 'Ця електронна адреса вже зареєстрована для отримання новин.'
            }
        }


