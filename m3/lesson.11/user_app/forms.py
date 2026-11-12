from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    """Форма для регистрации нового пользователя."""
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш email'})
    )

    class Meta:
        model = get_user_model()
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        User = get_user_model()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже существует')
        return email


class CustomAuthenticationForm(AuthenticationForm):
    """Форма для входа в систему."""
    username = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш email'})
    )

    def clean_username(self):
        username = self.cleaned_data.get('username').lower()
        return username