from .models import News
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'short_description', 'content', 'author', 'created_at']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание'}),
            'content': Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание'}),
            'author': TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'}),
            'created_at': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'}),
        }