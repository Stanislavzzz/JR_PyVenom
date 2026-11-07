from django import forms
from django.core.exceptions import ValidationError

from blog_app.models import Post


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        label="Заголовок",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
    )
    content = forms.CharField(
        label="Содержание",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите содержание', 'rows': '5'}),
    )
    rating = forms.IntegerField(
        min_value=0,
        max_value=100,
        label="Рейтинг",
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )


class PostModelForm(forms.ModelForm):
    """Форма для создания и редактирования постов на основе Post."""
    class Meta:
        model = Post
        fields = ('title', 'author', 'content', 'rating', 'tags')
        labels = {
            'title': "Заголовок",
            'author': "Автор",
            'content': "Содержание",
            'rating': "Рейтинг",
            'tags': "Тэги",
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите содержание', 'rows': '5'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 0 or rating > 10:
            raise ValidationError('Рейтинг не может быть меньше 0 или более 10')
        return rating

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise ValidationError('Заголовок должен быть более 5 символов')
        return title

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        forbidden_words = ["крипта", "казино"]

        for word in forbidden_words:
            if title:
                if word.lower() in title.lower():
                    raise ValidationError(f'Заголовок не должен содержать слово {word}')
            if content:
                if word.lower() in content.lower():
                    raise ValidationError(f'Пост не должен содержать слово {word}')


class PostDeleteForm(forms.Form):
    """..."""
    confirm = forms.BooleanField(
        label='Подтвердите удаление',
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )