from datetime import datetime

from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, \
    UserChangeForm
from django.forms import HiddenInput, FileInput

from authapp.models import User


class UserLoginForm(AuthenticationForm):
    """Форма для аутентификации"""

    class Meta:
        model = User
        fields = ('username', 'password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(UserCreationForm):
    """Форма для регистрации"""
    Captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_email(self):
        email_user = self.cleaned_data['email']
        email_data = User.objects.filter(email=email_user)
        if email_data:
            raise forms.ValidationError(
                'Пользователь с таким email уже зарегистрирован'
            )
        return email_user


class UserEditForm(UserChangeForm):
    """форма для редактирования юзера"""

    class Meta:
        now = int(datetime.now().year)
        model = User
        fields = (
            'avatar', 'first_name', 'last_name',
            'email', 'gender', 'birth_date', 'about_me',
        )
        widgets = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['class'] = 'form-group'
            self.fields['about_me'].widget.attrs['rows'] = 4
            field.help_text = ''
            if field_name == 'password':
                field.widget = HiddenInput()
            if field_name == 'avatar':
                field.widget = FileInput()

    def clean_birth_date(self):
        now = datetime.now().year
        date_data = self.cleaned_data['birth_date']
        if date_data:
            if 1920 < date_data.year < now:
                return date_data
            raise forms.ValidationError(
                'Неверная дата'
            )
